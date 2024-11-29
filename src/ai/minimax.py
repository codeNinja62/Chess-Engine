# src/ai/minimax.py

import random
from src.ai.evaluation import evaluate_board
from src.ai.move_generator import generate_moves

MAX_DEPTH = 3  # Depth of the search tree

def minimax(board, depth, alpha, beta, maximizing_player, color):
    """
    Minimax algorithm with Alpha-Beta pruning to find the best move.
    
    Args:
    - board: The current board position.
    - depth: The current depth of the recursion.
    - alpha: Alpha value for pruning.
    - beta: Beta value for pruning.
    - maximizing_player: Boolean indicating whether the current player is maximizing.
    - color: The current player's color ('white' or 'black').
    
    Returns:
    - best_move: The best move found at this point in the search tree.
    """
    if depth == 0:
        return evaluate_board(board), None

    moves = generate_moves(board, color)
    if not moves:  # No legal moves (e.g., checkmate or stalemate)
        return evaluate_board(board), None

    best_move = None
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            new_board = apply_move(board, move, color)  # A function to apply the move (not shown here)
            evaluation, _ = minimax(new_board, depth-1, alpha, beta, False, 'black')
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval, best_move
    
    else:  # Minimizing player (the opponent)
        min_eval = float('inf')
        for move in moves:
            new_board = apply_move(board, move, color)  # Apply the move for the opponent
            evaluation, _ = minimax(new_board, depth-1, alpha, beta, True, 'white')
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval, best_move

def best_move(board, color):
    """
    Returns the best move for the AI to play.
    
    Args:
    - board: The current board position.
    - color: The current player's color ('white' or 'black').
    
    Returns:
    - best_move: The best move for the AI.
    """
    _, move = minimax(board, MAX_DEPTH, float('-inf'), float('inf'), True, color)
    return move
