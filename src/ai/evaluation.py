# src/ai/evaluation.py

# Piece values (simplified evaluation for each piece type)
PIECE_VALUES = {
    'K': 1000,  # King is invaluable, high value to avoid checkmate
    'Q': 9,     # Queen
    'R': 5,     # Rook
    'B': 3,     # Bishop
    'N': 3,     # Knight
    'P': 1,     # Pawn
}

def evaluate_board(board):
    """
    Evaluate the current board position.
    Positive value is good for white, negative is good for black.
    
    Args:
    - board: 2D list representing the chessboard. Each element is a string like 'P', 'p', 'Q', etc.
    
    Returns:
    - evaluation_score: An integer score representing the position evaluation.
    """
    evaluation_score = 0
    
    for row in board:
        for piece in row:
            if piece.isupper():  # White pieces
                evaluation_score += PIECE_VALUES.get(piece.upper(), 0)
            elif piece.islower():  # Black pieces
                evaluation_score -= PIECE_VALUES.get(piece.lower(), 0)

    return evaluation_score
