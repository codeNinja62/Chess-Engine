# src/game/game_state.py

class GameState:
    def __init__(self):
        self.board = Board()
        self.is_game_over = False
        self.winner = None

    def update_game_state(self, move, color):
        """
        Update the game state after a move.
        
        Args:
        - move: A tuple (start_pos, end_pos) representing the move.
        - color: The color of the player making the move ('white' or 'black').
        """
        start_pos, end_pos = move
        piece = self.board.get_board()[start_pos[0]][start_pos[1]]

        # Apply the move (simple version, you can enhance this)
        self.board.get_board()[end_pos[0]][end_pos[1]] = piece
        self.board.get_board()[start_pos[0]][start_pos[1]] = ' '
        
        # Switch turn after move
        self.board.switch_turn()
