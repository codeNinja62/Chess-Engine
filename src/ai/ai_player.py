# src/ai/ai_player.py

from src.ai.minimax import best_move
from src.ai.move_generator import generate_moves
from src.ai.evaluation import evaluate_board

class AIPlayer:
    def __init__(self, color):
        self.color = color  # The color of the AI ('white' or 'black')

    def get_move(self, board):
        """
        Get the best move for the AI based on the current board position.
        
        Args:
        - board: The current board position.
        
        Returns:
        - best_move: The best move for the AI to play.
        """
        return best_move(board, self.color)

    def evaluate_position(self, board):
        """
        Evaluate the current board position.
        
        Args:
        - board: The current board position.
        
        Returns:
        - evaluation_score: The evaluation score of the current position.
        """
        return evaluate_board(board)
