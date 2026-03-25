# 50 Chess Puzzles: FEN + solution + rating + themes

PUZZLES = [
    {
        "fen": "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4",
        "moves": ["h5f7"],
        "rating": 1800,
        "themes": ["short", "mate", "scholars_mate", "advanced_pawn"]
    },
    {
        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR b KQkq - 5 4",
        "moves": ["d8f6"],
        "rating": 1850,
        "themes": ["defense", "attack", "pin"]
    },
    {
        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 0 5",
        "moves": ["f3g5", "d8g5", "c4f7"],
        "rating": 1900,
        "themes": ["sacrifice", "fork", "opening_trap"]
    },
    {
        "fen": "r3k2r/ppp2ppp/2nqbn2/3pp3/2B1P1b1/2NP1N2/PPPQ1PPP/R3K2R w KQkq - 0 8",
        "moves": ["c4d5", "e6d5", "e4d5"],
        "rating": 1950,
        "themes": ["opening", "discovered_attack", "pawn_structure"]
    },
    {
        "fen": "2kr3r/ppp2ppp/2nqbn2/3p4/3P4/2N2N2/PPP2PPP/R2QK2R w KQ - 0 12",
        "moves": ["d4d5", "c6d4", "f3d4"],
        "rating": 2000,
        "themes": ["pawn_advance", "outpost", "knight"]
    },
    {
        "fen": "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 5 4",
        "moves": ["d7d5", "e4d5", "c6a5"],
        "rating": 1820,
        "themes": ["gambit", "pawn", "center_control"]
    },
    {
        "fen": "rnbqkb1r/pppp1ppp/4pn2/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3",
        "moves": ["d1b3", "g8f6", "b3b7"],
        "rating": 1880,
        "themes": ["pin", "attack_king", "queen_sacrifice"]
    },
    {
        "fen": "r1bqkbnr/ppp2ppp/2np4/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 4",
        "moves": ["f3e5", "d6e5", "c4f7"],
        "rating": 1920,
        "themes": ["tactic", "sacrifice", "king_attack"]
    },
    {
        "fen": "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq d6 0 3",
        "moves": ["d4d5", "e6d5", "c1g5"],
        "rating": 1860,
        "themes": ["pin", "pawn_structure", "space"]
    },
    {
        "fen": "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P2q/8/PPPP1PPP/RNB1K1NR w KQkq - 6 4",
        "moves": ["h5h7"],
        "rating": 1810,
        "themes": ["mate", "short", "queen"]
    },
    {
        "fen": "r2qkb1r/ppp1pppp/2n2n2/3p1b2/3P1B2/2N2N2/PPP1PPPP/R2QKB1R w KQkq - 4 6",
        "moves": ["f3e5", "f6e4", "d3e4"],
        "rating": 1930,
        "themes": ["exchange", "tactic", "bishop_pair"]
    },
    {
        "fen": "r1bqr1k1/pppp1ppp/2n2n2/2b1p3/2B1P2q/2N2N2/PPPP1PPP/R1BQR1K1 w - - 8 8",
        "moves": ["f3g5", "h4g5", "c4f7"],
        "rating": 1970,
        "themes": ["sacrifice", "mate_threat", "castling"]
    },
    {
        "fen": "r3k2r/pppbqppp/2n1bn2/3pp3/2B1P3/2NP1N2/PPP2PPP/R1BQK2R w KQkq - 0 8",
        "moves": ["c4d5", "e6d5", "e4d5"],
        "rating": 2010,
        "themes": ["exchange", "pawn", "center"]
    },
    {
        "fen": "2rqkb1r/pp1npppp/2p2n2/3p1b2/3P1B2/2NBPN2/PP3PPP/R2QK2R b KQk - 0 9",
        "moves": ["f5g4", "f3e5", "c7e5"],
        "rating": 1955,
        "themes": ["bishop", "fork", "attack"]
    },
    {
        "fen": "r1bq1rk1/ppp2ppp/2n2n2/3p4/1b1NP3/2N5/PPP1BPPP/R1BQK2R w KQ - 0 9",
        "moves": ["e4e5", "d5d4", "c3d4"],
        "rating": 1890,
        "themes": ["pawn_gambit", "space", "attack"]
    },
    {
        "fen": "rnbqk1nr/pppp1ppp/4p3/8/1bPP4/8/PP2PPPP/RNBQKBNR w KQkq - 1 3",
        "moves": ["c4c5", "b4c3", "b1c3"],
        "rating": 1840,
        "themes": ["opening", "mobility", "bishop_pair"]
    },
    {
        "fen": "r1bqkb1r/ppppnppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4",
        "moves": ["f3g5", "h7h6", "g5f7"],
        "rating": 1905,
        "themes": ["sacrifice", "castling", "king_safety"]
    },
    {
        "fen": "r3k2r/ppp1qppp/2npbn2/4p3/2B1P3/2NP1N2/PPP2PPP/R1BQK2R w KQkq - 0 8",
        "moves": ["e4e5", "d6d5", "c4d5"],
        "rating": 1960,
        "themes": ["gambit", "initiative", "attack"]
    },
    {
        "fen": "2rq1rk1/ppp2ppp/2n1bn2/3p4/3P4/2NBPN2/PP3PPP/R2QK2R w KQ - 0 11",
        "moves": ["d3d4", "e5d4", "e3d4"],
        "rating": 1910,
        "themes": ["pawn", "center", "space"]
    },
    {
        "fen": "rnbqkb1r/pppppppp/5n2/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq - 1 2",
        "moves": ["e7e5", "d4e5", "f6e4"],
        "rating": 1875,
        "themes": ["gambit", "counter", "development"]
    },
    {
        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 0 5",
        "moves": ["c4d5", "f6d5", "d1b3"],
        "rating": 1945,
        "themes": ["opening", "pin", "queen"]
    },
    {
        "fen": "rnbqkb1r/pp1ppppp/5n2/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 2 3",
        "moves": ["d7d5", "e4d5", "f6d5"],
        "rating": 1830,
        "themes": ["gambit", "center", "development"]
    },
    {
        "fen": "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K2R b KQkq - 5 4",
        "moves": ["f6g4", "f3f7"],
        "rating": 1885,
        "themes": ["defense", "tactic", "bishop"]
    },
    {
        "fen": "r3k2r/ppp2ppp/2n1bn2/3qp3/2B1P2b/2NP1N2/PPP2PPP/R1BQK2R w KQkq - 0 8",
        "moves": ["e4e5", "d5d4", "c3d4"],
        "rating": 1980,
        "themes": ["gambit", "pawn", "initiative"]
    },
    {
        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 b kq - 5 5",
        "moves": ["d7d5", "e4d5", "c6a5"],
        "rating": 1855,
        "themes": ["gambit", "center", "counter"]
    },
    {
        "fen": "2rqkb1r/pp1npppp/2p2n2/3p1b2/3P1B2/2NBPN2/PP3PPP/R2QK2R w KQk - 0 9",
        "moves": ["f3e5", "f6e4", "d3e4"],
        "rating": 1925,
        "themes": ["exchange", "knight", "center"]
    },
    {
        "fen": "r1bqkbnr/pppppppp/2n5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 2 2",
        "moves": ["d2d4", "g8f6", "c1g5"],
        "rating": 1805,
        "themes": ["opening", "development", "pin"]
    },
    {
        "fen": "r1bqk2r/ppp2ppp/2n1pn2/3p4/1bPP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 0 5",
        "moves": ["c4c5", "b4c3", "b1c3"],
        "rating": 1895,
        "themes": ["opening", "bishop_pair", "space"]
    },
    {
        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 0 4",
        "moves": ["c4d5", "f6d5", "c3d5"],
        "rating": 1915,
        "themes": ["opening", "pawn", "exchange"]
    },
    {
        "fen": "r3kb1r/pppqpppp/2n2n2/3p1b2/3P1B2/2NBPN2/PPP2PPP/R2QK2R b KQkq - 0 8",
        "moves": ["f5g4", "f3e5", "c6e5"],
        "rating": 1965,
        "themes": ["tactic", "bishop", "knight"]
    },
    {
        "fen": "r1bq1rk1/ppp2ppp/2np1n2/2b1p3/2B1P3/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 0 8",
        "moves": ["c4d5", "e6d5", "e4d5"],
        "rating": 1990,
        "themes": ["gambit", "center", "attack"]
    },
    {
        "fen": "rnbqkb1r/pp2pppp/3p1n2/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 4",
        "moves": ["c2c3", "d7d5", "e4e5"],
        "rating": 1845,
        "themes": ["opening", "center", "development"]
    },
    {
        "fen": "r1bqr1k1/pppp1ppp/2n2n2/2b1p3/2B1P2q/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 8 8",
        "moves": ["f3g5", "h4g5", "c4f7"],
        "rating": 2020,
        "themes": ["sacrifice", "mate", "castling"]
    },
    {
        "fen": "rnbqkbnr/pppp1ppp/4p3/8/4PP2/8/PPPP2PP/RNBQKBNR b KQkq f3 0 2",
        "moves": ["d7d5", "f4d6"],
        "rating": 1825,
        "themes": ["gambit", "pawn", "development"]
    },
    {
        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2BPP3/5N2/PPP2PPP/RNBQK2R b KQkq d3 0 4",
        "moves": ["d5d4", "e3d4", "c6a5"],
        "rating": 1870,
        "themes": ["gambit", "opening", "center"]
    },
    {
        "fen": "2rq1rk1/ppp2ppp/2n1bn2/3pp3/2B1P2b/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 0 9",
        "moves": ["e4d5", "e6d5", "c4d5"],
        "rating": 1940,
        "themes": ["exchange", "pawn", "attack"]
    },
    {
        "fen": "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4",
        "moves": ["f3e5", "f6e4", "d1h5"],
        "rating": 1900,
        "themes": ["tactic", "fork", "attack"]
    },
    {
        "fen": "r1bq1rk1/ppp1nppp/2n1b3/3pp3/2B1P3/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 0 9",
        "moves": ["c4d5", "e6d5", "e4e5"],
        "rating": 1975,
        "themes": ["exchange", "pawn", "center"]
    },
    {
        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/6P1/PP2PP1P/RNBQKBNR w KQkq - 0 4",
        "moves": ["c4d5", "f6d5", "c1g5"],
        "rating": 1865,
        "themes": ["opening", "pin", "development"]
    },
    {
        "fen": "r3k2r/ppp1qppp/2n1bn2/3pp3/2B1P3/2NP1N2/PPP2PPP/R1BQK2R w KQkq - 0 8",
        "moves": ["e4e5", "d5d4", "c3d4"],
        "rating": 2005,
        "themes": ["gambit", "initiative", "attack"]
    },
    {
        "fen": "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
        "moves": ["f3e5", "f6e4", "d1h5"],
        "rating": 1835,
        "themes": ["tactic", "knight", "queen"]
    },
    {
        "fen": "r1bqr1k1/pppp1ppp/2n2n2/2b1p3/2B1P2q/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 6 8",
        "moves": ["c4d5", "e6d5", "f3g5"],
        "rating": 1995,
        "themes": ["gambit", "attack", "castling"]
    },
    {
        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 2",
        "moves": ["d7d5", "e3d4"],
        "rating": 1800,
        "themes": ["opening", "center", "development"]
    },
    {
        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 0 5",
        "moves": ["c4d5", "f6d5", "d1b3"],
        "rating": 1935,
        "themes": ["opening", "tactic", "queen"]
    },
    {
        "fen": "2rqkb1r/pp1npppp/2p2n2/3p1b2/3P1B2/2N2N2/PPP1PPPP/R2QKB1R w KQk - 4 6",
        "moves": ["f3e5", "f6e4", "d3e4"],
        "rating": 1880,
        "themes": ["exchange", "knight", "bishop"]
    },
    {
        "fen": "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4",
        "moves": ["f3g5", "d7d6", "c4f7"],
        "rating": 1910,
        "themes": ["sacrifice", "king_attack", "castling"]
    },
    {
        "fen": "rnbqkbnr/ppp2ppp/8/3pp3/2B1P3/8/PPPP1PPP/RNBQK1NR w KQkq d6 0 3",
        "moves": ["d2d4", "d5d4", "c3d4"],
        "rating": 1850,
        "themes": ["opening", "center", "pawn"]
    },
    {
        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 b kq - 5 5",
        "moves": ["d7d5", "e4d5", "c6a5"],
        "rating": 1890,
        "themes": ["gambit", "center", "counter"]
    },
    {
        "fen": "r3k2r/pppbqppp/2n1bn2/3pp3/2B1P3/2NP1N2/PPP2PPP/R1BQK2R w KQkq - 0 8",
        "moves": ["e4e5", "d5d4", "c3d4"],
        "rating": 2015,
        "themes": ["gambit", "pawn", "attack"]
    }
]


# 20 Opening Positions (ECO A-E)

OPENINGS = [
    {
        "eco": "A00",
        "name": "Van Creborn Opening",
        "moves": ["d4", "d5", "c4", "c6", "Nf3", "Nf6", "Nc3", "e6"],
        "description": "A solid transposition from the Queen's Gambit Declined. Black delays development to solidify the center.",
        "middlegame_plans": "Content for equality with flexible pawn structure. Seek piece activity and watch for minor piece exchanges."
    },
    {
        "eco": "A10",
        "name": "English Opening",
        "moves": ["c4"],
        "description": "Asymmetric opening claiming space on the queenside while Black establishes a classical center with e7-e5 or e7-e6.",
        "middlegame_plans": "Play on queenside with b2-b4. Target c5, c6. If Black plays ...d7-d5, consider cxd5 followed by Nc3."
    },
    {
        "eco": "A40",
        "name": "Modern Defense",
        "moves": ["d4", "g6"],
        "description": "Black ignores the center and prepares to fianchetto the bishop on g7, creating a solid but passive setup.",
        "middlegame_plans": "Highlight the weakened b6 square. Build queenside majority. Avoid being pushed back by the g7 bishop."
    },
    {
        "eco": "A45",
        "name": "Trompowsky Attack",
        "moves": ["d4", "Nf6", "Bg5"],
        "description": "White immediately attacks theNf6 knight, restraining Black's development and often transposing into English Attack structures.",
        "middlegame_plans": "Exchange on f6 and play e2-e4. Maintain bishop on g5 to pressure h7. Castle queenside for attacking chances."
    },
    {
        "eco": "A50",
        "name": "Indian Defense",
        "moves": ["d4", "Nf6", "c4", "b6"],
        "description": "Black immediately challenges White's center with a fianchetto setup, aiming to undermine the c4 pawn.",
        "middlegame_plans": "Respond to ...Bb7. Trade bishops. Use e2-e4 to challenge Black's center. Target the b6 bishop."
    },
    {
        "eco": "A52",
        "name": "Budapest Gambit",
        "moves": ["d4", "Nf6", "c4", "e5"],
        "description": "Aggressive pawn sacrifice: Black strikes at White's center immediately, sacrificing a pawn for active piece play.",
        "middlegame_plans": "Keep the pawn with d4xe5. Develop pieces quickly. Don't let Black's pieces become too active."
    },
    {
        "eco": "A80",
        "name": "Dutch Defense",
        "moves": ["d4", "f5"],
        "description": "Black immediately claims space on the kingside and prepares to build an impressive pawn center with ...e7-e6 and ...d7-d6.",
        "middlegame_plans": "Challenge the f5 pawn with e2-e4. Target the e6 pawn weakness. Castle queenside for attacking chances."
    },
    {
        "eco": "A90",
        "name": "Dutch Stonewall",
        "moves": ["d4", "f5", "c4", "Nf6", "Nc3", "e6", "e4", "fg4"],
        "description": "Black builds a solid pawn structure with ...d7-d5, ...e7-e6, and ...c7-c5, controlling the center with pawns.",
        "middlegame_plans": "Control e5 outpost. Target the weak e6 pawn. Blockade the d5 pawn if advanced. Be patient."
    },
    {
        "eco": "B00",
        "name": "King's Pawn Game",
        "moves": ["e4"],
        "description": "The most common opening move. White fights for central control and prepares to develop knights toward the center.",
        "middlegame_plans": "Control the center, develop knights to f3 and c3, bishop to c4 or f4. Aim for kingside castling."
    },
    {
        "eco": "B10",
        "name": "Caro-Kann Defense",
        "moves": ["e4", "c6"],
        "description": "A solid defense: Black strikes at White's center pawn while maintaining a strong pawn structure. Very reliable.",
        "middlegame_plans": "Play c4xd5 and then push the e-pawn. Use the d5 square as an outpost. Development is key."
    },
    {
        "eco": "B15",
        "name": "Caro-Kann Gambit",
        "moves": ["e4", "c6", "d4", "d5", "Nc3", "dxe4", "Nxe4", "Bf5"],
        "description": "White wins a pawn but Black's pieces develop actively. The g7 bishop becomes dangerous.",
        "middlegame_plans": "Hold the extra pawn. Develop kingside. Castle queenside. Watch for Black's active bishops."
    },
    {
        "eco": "B20",
        "name": "Sicilian Defense",
        "moves": ["e4", "c5"],
        "description": "The most popular response to 1.e4. Black fights for the center asymmetrically, creating imbalanced positions.",
        "middlegame_plans": "For White: play d4xd4 and c2-c3. For Black: develop with d7-d6, Nf6, Bg7, and 0-0. Attack on the wings."
    },
    {
        "eco": "B40",
        "name": "Sicilian: 2...e6",
        "moves": ["e4", "c5", "Nf3", "e6"],
        "description": "The 'Scheveningen' setup: solid pawn structure with piece development. Black prepares ...d7-d5.",
        "middlegame_plans": "White can try e4-e5 or c4xd5. Black aims for ...d7-d5 break. Both sides have good chances."
    },
    {
        "eco": "B70",
        "name": "Dragon Variation",
        "moves": ["e4", "c5", "Nf3", "d6", "d4", "cxd4", "Nxd4", "Nf6", "Nc3", "g6"],
        "description": "Black fianchettoes the bishop to g7, creating a pawn chain and targeting the d4 square.",
        "middlegame_plans": "White plays Bc4, Qd2, 0-0-0. Attack the d6 pawn. Black looks for ...b7-b5 and ...d6-d5 breaks."
    },
    {
        "eco": "B90",
        "name": "Sicilian: Najdorf Variation",
        "moves": ["e4", "c5", "Nf3", "d6", "d4", "cxd4", "Nxd4", "Nf6", "Nc3", "a6"],
        "description": "The most aggressive Sicilian. Black prevents Bb5 and plans ...e7-e5 or ...b7-b5 queenside counterplay.",
        "middlegame_plans": "White: Bc4, f3, Be3, Qd2, 0-0-0. Attack the kingside. Black: ...e7-e5, ...b7-b5, ...Qb6."
    },
    {
        "eco": "C00",
        "name": "French Defense",
        "moves": ["e4", "e6"],
        "description": "Solid and strategic: Black builds a pawn chain and aims to challenge the center with ...d7-d5.",
        "middlegame_plans": "White plays d4-d5 or exchanges with exd5. Black seeks ...c7-c5 break. The c8 bishop is blocked."
    },
    {
        "eco": "C20",
        "name": "King's Gambit",
        "moves": ["e4", "e5", "f4"],
        "description": "White sacrifices a pawn for rapid development and kingside attacking chances. Romantic era favorite.",
        "middlegame_plans": "White: Bc4, Nf3, Qh5. Attack f7. Black accepts and seeks to hold the pawn with ...d7-d5."
    },
    {
        "eco": "C50",
        "name": "Italian Game",
        "moves": ["e4", "e5", "Nf3", "Nc6", "Bc4", "Bc5"],
        "description": "Classic development: both sides fight for the e5 square. The bishops eye the opponent's weaknesses.",
        "middlegame_plans": "White: d4 or c3. Attack f7. Black: ...d6, ...Nf6, ...0-0. Watch for tactics on f7."
    },
    {
        "eco": "C60",
        "name": "Ruy Lopez",
        "moves": ["e4", "e5", "Nf3", "Nc6", "Bb5"],
        "description": "The 'Spanish Game': White attacks the e5 pawn indirectly, fighting for the central squares.",
        "middlegame_plans": "White seeks to exchange on c6 and play d4. Black plays ...a6, ...b5, ...d6. The Marshall Attack is sharp."
    },
    {
        "eco": "E00",
        "name": "Catalan Opening",
        "moves": ["d4", "Nf6", "c4", "e6", "g3"],
        "description": "White combines queen pawn opening with kingside fianchetto, playing for a slight spatial advantage.",
        "middlegame_plans": "Build a strong center with Nc3, Bg2, 0-0. Play on the queenside. Black aims for ...d7-d5 counter."
    }
]


def get_puzzle_by_rating(min_rating: int = 1800, max_rating: int = 3000):
    """Return puzzles filtered by rating."""
    return [p for p in PUZZLES if min_rating <= p["rating"] <= max_rating]


def get_opening_by_eco(eco: str):
    """Return opening by ECO code."""
    for o in OPENINGS:
        if o["eco"].upper() == eco.upper():
            return o
    return None


def get_opening_by_name(name: str):
    """Return opening by name (fuzzy match)."""
    name_lower = name.lower()
    for o in OPENINGS:
        if name_lower in o["name"].lower() or o["name"].lower() in name_lower:
            return o
    return None
