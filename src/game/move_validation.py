# src/game/move_validation.py

def is_valid_move(board, start_pos, end_pos, color):
    """
    Check if a move is valid based on the piece type, game rules, and board state.
    
    Args:
    - board: 2D list representing the board.
    - start_pos: Tuple (row, col) for the piece's starting position.
    - end_pos: Tuple (row, col) for the destination.
    - color: 'white' or 'black', the player's color.
    
    Returns:
    - True if the move is valid, False otherwise.
    """
    piece = board[start_pos[0]][start_pos[1]]
    
    if piece == ' ':
        return False  # No piece to move
    
    if piece.isupper() and color == 'black':
        return False  # White piece, black player
    
    if piece.islower() and color == 'white':
        return False  # Black piece, white player
    
    # Add piece-specific move validation (e.g., for pawns, knights, etc.)
    # Example for pawn movement (simplified):
    if piece.lower() == 'p':
        return is_valid_pawn_move(board, start_pos, end_pos, color)
    
    # More piece-specific checks should be added for Rooks, Knights, Bishops, etc.
    
    return True

def is_valid_pawn_move(board, start_pos, end_pos, color):
    """
    Validate pawn move. Simplified for now (ignores en passant, promotion, etc.)
    
    Args:
    - board: The chessboard.
    - start_pos: The starting position of the pawn.
    - end_pos: The ending position of the pawn.
    - color: 'white' or 'black'.
    
    Returns:
    - True if the move is valid for a pawn, False otherwise.
    """
    direction = 1 if color == 'white' else -1  # White moves up, black moves down
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    
    # Pawn moves one step forward
    if start_col == end_col and board[end_row][end_col] == ' ':
        if (end_row - start_row) == direction:
            return True
    
    # Pawn captures (diagonal)
    if abs(start_col - end_col) == 1 and (end_row - start_row) == direction:
        target = board[end_row][end_col]
        if target != ' ' and target.islower() != board[start_row][start_col].islower():
            return True

    return False
