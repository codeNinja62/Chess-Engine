# src/gui/game_window.py

import pygame
from src.game.board import Board

# Define some constants for the board and window size
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# Initialize Pygame
pygame.init()

class GameWindow:
    def __init__(self):
        self.board = Board()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Game")

    def draw_board(self):
        """
        Draw the chessboard and pieces onto the Pygame window.
        """
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else GRAY
                pygame.draw.rect(self.screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
        # Drawing pieces on the board
        for row in range(8):
            for col in range(8):
                piece = self.board.get_board()[row][col]
                if piece != ' ':
                    self.draw_piece(piece, row, col)

    def draw_piece(self, piece, row, col):
        """
        Draw a piece on the board (use a simple placeholder for now).
        """
        font = pygame.font.SysFont(None, 48)
        text = font.render(piece, True, BLACK)
        self.screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4))

    def run(self):
        """
        Run the main game loop to display the board and handle user interaction.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)
            self.draw_board()
            pygame.display.update()

        pygame.quit()
