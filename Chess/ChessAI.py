import random
import numpy as np

piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

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
DEPTH = 4
transposition_table = {}
def findBestMove(game_state, valid_moves, return_queue):
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    findMoveNegaMaxAlphaBeta(game_state, valid_moves, DEPTH, -CHECKMATE, CHECKMATE, 1 if game_state.white_to_move else -1)
    return_queue.put(next_move)

def findMoveNegaMaxAlphaBeta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    global next_move
    if depth == 0:
        return turn_multiplier * scoreBoard(game_state)
    
    
    max_score = -CHECKMATE
    for move in valid_moves:
        game_state.makeMove(move)
        next_moves = game_state.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        game_state.undoMove()
        if max_score > alpha:  # pruning
            alpha = max_score
        if alpha >= beta:
            break
    return max_score

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