# src/utils/logger.py

import logging

# Setup the logger
logging.basicConfig(filename='game.log', level=logging.DEBUG)

def log_move(move, color):
    """
    Log a move made by a player.
    """
    logging.info(f"{color} player made move: {move}")
