from fastapi import APIRouter, HTTPException
from models.schemas import (
    PositionEvalRequest,
    PositionEvalResponse,
    GameAnnotateResponse,
    Blunder,
    Mistake,
    Inaccuracy,
)
import chess
import chess.pgn

router = APIRouter(prefix="/api/v1", tags=["evaluation"])

# Piece values for simple material eval
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0,
}


def material_eval(board: chess.Board) -> int:
    """Return centipawn advantage for white (positive = white ahead)."""
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            val = PIECE_VALUES[piece.piece_type]
            score += val if piece.color == chess.WHITE else -val
    return score


def classify_eval(cp: int) -> str:
    """Classify eval score into a human-readable category."""
    if cp >= 500:
        return "winning"
    elif cp >= 150:
        return "advantage"
    elif cp >= 50:
        return "slight_advantage"
    elif cp >= -50:
        return "equal"
    elif cp >= -150:
        return "slight_disadvantage"
    elif cp >= -500:
        return "disadvantage"
    else:
        return "losing"


def find_best_move(board: chess.Board) -> tuple[str, int]:
    """
    Simple best-move finder using legal move enumeration + basic scoring.
    Returns (uci_move, centipawn_score).
    """
    if board.is_game_over():
        return "none", material_eval(board)

    best_move = None
    best_score = -999999
    current_eval = material_eval(board)
    is_white = board.turn == chess.WHITE

    for move in board.legal_moves:
        board.push(move)
        new_eval = material_eval(board)

        # Score: prefer moves that improve our position
        delta = new_eval - current_eval

        # Bonus for captures
        if board.is_capture(move):
            delta += 20

        # Bonus for checks
        if board.is_check():
            delta += 30

        board.pop()

        if is_white:
            if delta > best_score:
                best_score = delta
                best_move = move
        else:
            if -delta > best_score:
                best_score = -delta
                best_move = move

    uci = best_move.uci() if best_move else "none"
    return uci, material_eval(board)


def analyze_move(board_before: chess.Board, move: chess.Move) -> tuple[int, int]:
    """
    Analyze a single move: eval before, eval after.
    Returns (eval_before, eval_after) in centipawns.
    """
    eval_before = material_eval(board_before)

    board_before.push(move)
    eval_after = material_eval(board_before)
    board_before.pop()

    return eval_before, eval_after


@router.post("/eval/position", response_model=PositionEvalResponse)
async def eval_position(req: PositionEvalRequest):
    """
    Evaluate a FEN position.
    Returns: eval_score_centipawns, best_move_uci, classification.
    """
    try:
        board = chess.Board(req.fen)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid FEN notation")

    if board.is_game_over():
        raise HTTPException(status_code=400, detail="Game is already over")

    best_move_uci, eval_cp = find_best_move(board)
    classification = classify_eval(eval_cp)

    return PositionEvalResponse(
        eval_score_centipawns=eval_cp,
        best_move_uci=best_move_uci,
        classification=classification,
    )


@router.post("/game/annotate", response_model=GameAnnotateResponse)
async def annotate_game(pgn: str = None):
    """
    Analyze a PGN and return blunders, mistakes, and inaccuracies.
    Expects 'pgn' as form field or JSON body.
    """
    if not pgn:
        raise HTTPException(status_code=400, detail="Missing 'pgn' field")

    try:
        game = chess.pgn.read_game(pgn)
        if game is None:
            raise HTTPException(status_code=400, detail="Could not parse PGN")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid PGN format")

    board = chess.Board()
    blunders_list: list[Blunder] = []
    mistakes_list: list[Mistake] = []
    inaccuracies_list: list[Inaccuracy] = []

    move_number = 0
    current_eval = 0

    for node in game.mainline():
        move = node.move
        if move is None:
            break

        board.push(move)
        eval_before = current_eval
        eval_after = material_eval(board)
        current_eval = eval_after

        delta = eval_after - eval_before

        # For black moves, delta is inverted
        if board.turn == chess.WHITE:
            delta = -delta

        abs_delta = abs(delta)

        if abs_delta >= 150:
            blunder = Blunder(
                move_number=move_number,
                move=move.uci(),
                eval_before=eval_before,
                eval_after=eval_after,
                delta=int(delta),
            )
            blunders_list.append(blunder)
        elif abs_delta >= 70:
            mistake = Mistake(
                move_number=move_number,
                move=move.uci(),
                eval_before=eval_before,
                eval_after=eval_after,
                delta=int(delta),
            )
            mistakes_list.append(mistake)
        elif abs_delta >= 30:
            inaccuracy = Inaccuracy(
                move_number=move_number,
                move=move.uci(),
                eval_before=eval_before,
                eval_after=eval_after,
                delta=int(delta),
            )
            inaccuracies_list.append(inaccuracy)

        move_number += 1

    return GameAnnotateResponse(
        blunders=blunders_list,
        mistakes=mistakes_list,
        inaccuracies=inaccuracies_list,
    )
