import random
from typing import Counter
import numpy as np

import ChessEngine

piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}




# Define the openings with their move sequences
openings_moves = {
    "Sicilian Defense": [
        ["e4", ["c7","c5"]],
        ["Nf3", ["d7","d6"]],
        ["d4", ["c5","d4"]],
        ["Nxd4", "Nf6"]
    ],
    "King's Gambit": [
        ["e4", ["e7","e5"]],
        ["f4", ["e5","f4"]],
        ["Nf3", ["d7","d5"]],
        ["Nc3", ["Ng8","Nf6"]],
    ],
    "Queen's Gambit": [
        ["d4", ["d7","d5"]],
        ["c4",[ "c7","c6"]],
    ],
    # "Caro-Kann Defense": [
    #     ["e4", ["c7","c6"]],
    #     ["d4", ["d7","d5"]],
    # ],
    # "Ruy Lopez": [
    #     ["e4", ["e7","e5"]],
    #     ["Nf3", ["Nb8","Nc6"]],
    # ],
    # "French Defense": [
    #     ["e4", ["e7","e6"]],
    #     ["d4", ["d7","d5"]],
    #     ["Nc3", ["Ng8","Nf6"]]
    # ],
    # "Pirc Defense": [
    #     ["e4", ["d7","d6"]],
    #     ["d4", ["Ng8","Nf6"]],
    #     ["Nc3", ["g7","g6"]]
    # ],
    "King's Indian Attack": [
        ["Nf3", ["g7","g6"]],
        ["g3", ["Bf8","Bg7"]],
    ],
    "Nimzo-Larsen Attack": [
        ["b3", ["e7","e5"]],
        ["Bb2",["Nb8","Nc6"]]
    ]
}







knight_scores = np.array([
    [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
    [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
    [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
    [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
    [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
    [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
    [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
    [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]
])

bishop_scores = np.array([
    [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
    [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
    [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
    [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
    [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
    [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
    [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
    [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]
])

rook_scores = np.array([
    [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
    [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
    [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]
])

queen_scores = np.array([
    [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
    [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
    [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
    [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
    [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
    [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
    [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
    [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]
])
ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4,
                     "5": 3, "6": 2, "7": 1, "8": 0}
files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3,
                     "e": 4, "f": 5, "g": 6, "h": 7}
pawn_scores = np.array([
    [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
    [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
    [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
    [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
    [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
    [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
    [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
    [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
])

piece_position_scores = {
    "wN": knight_scores,
    "bN": np.flipud(knight_scores),
    "wB": bishop_scores,
    "bB": np.flipud(bishop_scores),
    "wQ": queen_scores,
    "bQ": np.flipud(queen_scores),
    "wR": rook_scores,
    "bR": np.flipud(rook_scores),
    "wp": pawn_scores,
    "bp": np.flipud(pawn_scores)
}

CHECKMATE = float('inf')
STALEMATE = 0
DEPTH = 3
transposition_table = {}
counter = 0
def findBestMove(game_state, valid_moves, return_queue):
    global next_move
    next_move = None
    
    move_log = game_state.move_log
    move_texts = []
    for i in range(0, len(move_log), 2):
        move_string = [str(move_log[i])]
        if i + 1 < len(move_log):
            move_string.append(str(move_log[i + 1]))
        move_texts.append(move_string)
    t = False
    k = ''
    if len(move_texts) >= 10:
        global DEPTH
        DEPTH = 4
    for open in openings_moves.values():
        if t:
            break
        for i in range(len(move_texts)):
            if len(move_texts) > len(open):
                break
            if i==len(move_texts)-1 and move_texts[i][0] == open[i][0] and len(open[i])>1:
                k = open[i][1]
                mo = ChessEngine.Move((ranks_to_rows[open[i][1][0][-1]],files_to_cols[open[i][1][0][-2]]), (ranks_to_rows[open[i][1][1][-1]],files_to_cols[open[i][1][1][-2]]), game_state.board)
                return_queue.put(mo)
                t = True
                break
                
            if move_texts[i][0] != open[i][0] or (len(open[i])>1 and move_texts[i][1] != open[i][1][1]):
                break 
    if not t:
        random.shuffle(valid_moves)
        findMoveNegaMaxAlphaBeta(game_state, valid_moves, DEPTH, -CHECKMATE, CHECKMATE, 1 if game_state.white_to_move else -1)
        print(counter,next_move,type(next_move),k,type(k))
        return_queue.put(next_move)

                
        
    
    
    
def board_to_fen(board):
    fen = ""
    for row in board:
        empty_count = 0
        for square in row:
            if square == "--":
                empty_count += 1
            else:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
                fen += square[1].upper() if square[0] == "w" else square[1]
        if empty_count > 0:
            fen += str(empty_count)
        fen += "/"
    fen = fen[:-1]
    return fen

def findMoveNegaMaxAlphaBeta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    global counter
    counter += 1
    global next_move
    fen = board_to_fen(game_state.board)
    key = (fen, depth, alpha, beta, turn_multiplier)
    
    if key in transposition_table:
        return transposition_table[key]
    
    if depth == 0:
        score = turn_multiplier * scoreBoard(game_state)
        transposition_table[key] = score
        return score
    
    max_score = -CHECKMATE
    for move in valid_moves:
        game_state.makeMove(move)
        next_moves = game_state.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        game_state.undoMove()
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        if max_score > alpha:
            alpha = max_score
        if alpha >= beta:
            break
    
    transposition_table[key] = max_score
    return max_score
    
#depricated
# def findMoveNegaMaxAlphaBeta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
#     global counter
#     counter += 1
#     global next_move
#     if depth == 0:
#         return turn_multiplier * scoreBoard(game_state)
    
    
#     max_score = -CHECKMATE
#     for move in valid_moves:
#         game_state.makeMove(move)
#         next_moves = game_state.getValidMoves()
#         score = -findMoveNegaMaxAlphaBeta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
#         if score > max_score:
#             max_score = score
#             if depth == DEPTH:
#                 next_move = move
#         game_state.undoMove()
#         if max_score > alpha:  # pruning
#             alpha = max_score
#         if alpha >= beta:
#             break
#     return max_score

def findRandomMove(valid_moves):
    """
    Picks and returns a random valid move.
    """
    return random.choice(valid_moves)

def scoreBoard(game_state):
    if game_state.checkmate:
        if game_state.white_to_move:
            return -CHECKMATE  # black wins
        else:
            return CHECKMATE  # white wins
    elif game_state.stalemate:
        return STALEMATE

    score = 0
    total_material = 0
    board = game_state.board

    # Material and positional evaluation
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece != "--":
                piece_position_score = piece_position_scores.get(piece, np.zeros((8,8)))
                if piece[0] == 'w':
                    score += piece_score[piece[1]] + piece_position_score[row][col]
                    total_material += piece_score[piece[1]]
                elif piece[0] == 'b':
                    score -= piece_score[piece[1]] + piece_position_score[row][col]
                    total_material += piece_score[piece[1]]

    # Pawn structure evaluation
    score += evaluatePawnStructure(board)

    # Game phase adjustments
    
    if total_material > 19:  # Opening or middlegame
        score += evaluateOpening(board)
    else:  # Endgame
        
        score += evaluateEndgame(board)

    return score

def evaluatePawnStructure(board):
    score = 0
    white_pawn_positions = []
    black_pawn_positions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece == 'wp':
                white_pawn_positions.append((row, col))
            elif piece == 'bp':
                black_pawn_positions.append((row, col))
    score += evaluatePawns(white_pawn_positions, 'w')
    score -= evaluatePawns(black_pawn_positions, 'b')
    return score

def evaluatePawns(pawn_positions, color):
    score = 0
    for pos in pawn_positions:
        row, col = pos
        # Double pawns
        if pawn_positions.count((row, col)) > 1:
            score -= 0.5
        # Isolated pawns
        if not ((row-1, col) in pawn_positions or
                   (row+1, col) in pawn_positions or
                   (row, col-1) in pawn_positions or
                   (row, col+1) in pawn_positions):
            score -= 0.5
        # Passed pawns
        if color == 'w' and all(r < row for r, c in pawn_positions):
            score += 1
        if color == 'b' and all(r > row for r, c in pawn_positions):
            score += 1
    return score

def evaluateOpening(board):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece != "--":
                # Center control
                if piece in 'PpNnBb' and (row in [3, 4] and col in [3, 4]):
                    score += 0.2 if piece[0] == 'w' else -0.2
                # King safety
                if piece == 'wK' and (row > 1 and row < 6) and (col > 1 and col < 6):
                    score -= 0.5
                if piece == 'bK' and (row > 1 and row < 6) and (col > 1 and col < 6):
                    score += 0.5
    return score

def evaluateEndgame(board):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece != "--":
                # King activity
                if piece == 'wK' and (row in [0, 1, 6, 7] or col in [0, 1, 6, 7]):
                    score -= 0.5
                if piece == 'bK' and (row in [0, 1, 6, 7] or col in [0, 1, 6, 7]):
                    score += 0.5
                # Pawn promotion potential
                if piece == 'wp' and row == 7:
                    score += 1
                if piece == 'bp' and row == 1:
                    score -= 1
    return score