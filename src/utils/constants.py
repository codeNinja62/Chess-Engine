# src/utils/constants.py

# Piece symbols (uppercase for white, lowercase for black)
PIECE_KING = 'K'
PIECE_QUEEN = 'Q'
PIECE_ROOK = 'R'
PIECE_BISHOP = 'B'
PIECE_KNIGHT = 'N'
PIECE_PAWN = 'P'

# Directions for piece movement (simplified, in terms of row and column changes)
# For example, the rook can move any number of squares along the row or column, so it has multiple directions.

DIRECTIONS = {
    'king': [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)],
    'queen': [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)],
    'rook': [(1, 0), (0, 1), (-1, 0), (0, -1)],  # Rooks move along rows and columns
    'bishop': [(1, 1), (-1, 1), (1, -1), (-1, -1)],  # Bishops move diagonally
    'knight': [
        (2, 1), (2, -1), (-2, 1), (-2, -1),  # Two squares in one direction, one square perpendicular
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ],
    'pawn_white': [(1, 0), (1, 1), (1, -1)],  # White pawn moves downwards (1 step forward, captures diagonally)
    'pawn_black': [(-1, 0), (-1, 1), (-1, -1)]  # Black pawn moves upwards (1 step forward, captures diagonally)
}

# Piece values (used in evaluation)
PIECE_VALUES = {
    'P': 1,  # Pawn
    'N': 3,  # Knight
    'B': 3,  # Bishop
    'R': 5,  # Rook
    'Q': 9,  # Queen
    'K': 1000  # King (invaluable)
}

# Castling directions
CASTLING_DIRECTIONS = {
    'white_king': [(7, 4), (7, 6)],  # White king castling moves (king starts at e1, moves to g1)
    'white_queen': [(7, 4), (7, 2)],  # White queen castling moves (king starts at e1, moves to c1)
    'black_king': [(0, 4), (0, 6)],  # Black king castling moves (king starts at e8, moves to g8)
    'black_queen': [(0, 4), (0, 2)],  # Black queen castling moves (king starts at e8, moves to c8)
}

# En Passant capture direction
EN_PASSANT = {
    'white': [(1, -1), (1, 1)],  # White pawns can capture en passant diagonally (down-left or down-right)
    'black': [(-1, -1), (-1, 1)]  # Black pawns can capture en passant diagonally (up-left or up-right)
}

# Pawn promotion ranks
PAWN_PROMOTION_RANKS = {
    'white': 7,  # White pawns promote when they reach rank 7 (row 7)
    'black': 0   # Black pawns promote when they reach rank 0 (row 0)
}
