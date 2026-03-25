from pydantic import BaseModel
from typing import Optional


class PuzzleFromPositionRequest(BaseModel):
    fen: str
    difficulty: Optional[int] = 1800


class PuzzleFromPositionResponse(BaseModel):
    puzzle_fen: str
    moves: list[str]
    rating: int
    themes: list[str]


class DailyPuzzleResponse(BaseModel):
    puzzle_fen: str
    moves: list[str]
    rating: int
    themes: list[str]
    hint: str


class PositionEvalRequest(BaseModel):
    fen: str


class PositionEvalResponse(BaseModel):
    eval_score_centipawns: int
    best_move_uci: str
    classification: str


class OpeningResponse(BaseModel):
    eco: str
    name: str
    moves: list[str]
    description: str
    middlegame_plans: str


class Blunder(BaseModel):
    move_number: int
    move: str
    eval_before: int
    eval_after: int
    delta: int


class Mistake(BaseModel):
    move_number: int
    move: str
    eval_before: int
    eval_after: int
    delta: int


class Inaccuracy(BaseModel):
    move_number: int
    move: str
    eval_before: int
    eval_after: int
    delta: int


class GameAnnotateResponse(BaseModel):
    blunders: list[Blunder]
    mistakes: list[Mistake]
    inaccuracies: list[Inaccuracy]
