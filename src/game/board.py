# src/game/board.py

class Board:
    def __init__(self):
        # Initialize an 8x8 chessboard with default pieces
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.castling_rights = {
            'white': {'k': True, 'q': True},  # King-side, Queen-side castling for white
            'black': {'k': True, 'q': True},  # King-side, Queen-side castling for black
        }
        self.en_passant_target = None
        self.turn = 'white'  # white starts the game

    def print_board(self):
        """
        Print the current board to the console.
        """
        for row in self.board:
            print(" ".join(row))
    
    def get_board(self):
        return self.board

    def get_turn(self):
        return self.turn
    
    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'
    
    def reset_board(self):
        """
        Reset the board to the starting position.
        """
        self.__init__()
