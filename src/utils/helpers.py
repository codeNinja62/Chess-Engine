# src/utils/helpers.py

def is_within_bounds(pos):
    """
    Check if the given position is within the board bounds.
    """
    return 0 <= pos[0] < 8 and 0 <= pos[1] < 8
