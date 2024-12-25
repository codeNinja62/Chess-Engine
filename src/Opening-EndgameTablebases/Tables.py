import chess
import chess.syzygy
import chess.polyglot
import os
from typing import Optional, Dict

class ChessEngine:
    """
    A simple chess engine with support for:
    - Opening book suggestions
    - Endgame tablebase lookups
    - Basic position evaluation
    """

    def __init__(self, opening_book_path: str, tablebase_path: str):
        # Initialize paths and performance tracking
        self.opening_book_path = opening_book_path if os.path.exists(opening_book_path) else None
        self.tablebase_path = tablebase_path if os.path.exists(tablebase_path) else None
        self.tablebase_handler = None

        # Load resources
        if self.opening_book_path:
            print("Opening book loaded successfully.")
        else:
            print("Opening book not found or invalid path.")

        if self.tablebase_path:
            self.tablebase_handler = chess.syzygy.open_tablebase(self.tablebase_path)
            print("Endgame tablebase loaded successfully.")
        else:
            print("Tablebase directory not found or invalid path.")

    def analyze_position(self, board: chess.Board) -> Dict:
        """
        Analyze a given chess position and provide insights like game phase,
        suggested moves, and evaluations.
        """
        analysis = {}
        
        # Determine the current phase of the game
        analysis['phase'] = self.determine_game_phase(board)

        # Provide suggestions based on game phase
        if analysis['phase'] == 'opening':
            analysis['suggested_move'] = self.get_opening_move(board)
        elif analysis['phase'] == 'endgame':
            analysis['suggested_move'] = self.get_tablebase_move(board)
            analysis['evaluation'] = self.evaluate_endgame(board)

        return analysis

    def determine_game_phase(self, board: chess.Board) -> str:
        """
        Classify the game phase as "opening," "middlegame," or "endgame."
        """
        total_material = len(board.piece_map())
        queens_count = sum(len(board.pieces(chess.QUEEN, color)) for color in [chess.WHITE, chess.BLACK])

        if total_material >= 28 and queens_count == 2:
            return 'opening'
        elif total_material <= 12 or queens_count == 0:
            return 'endgame'
        else:
            return 'middlegame'

    def get_opening_move(self, board: chess.Board) -> Optional[chess.Move]:
        """
        Suggest a move from the opening book if available.
        """
        if not self.opening_book_path:
            return None

        try:
            with chess.polyglot.open_reader(self.opening_book_path) as reader:
                return reader.weighted_choice(board).move
        except Exception as e:
            print(f"Error accessing opening book: {e}")
            return None

    def get_tablebase_move(self, board: chess.Board) -> Optional[chess.Move]:
        """
        Suggest a move using endgame tablebases.
        """
        if not self.tablebase_handler or board.is_game_over():
            return None

        try:
            with self.tablebase_handler as tablebase:
                if len(board.piece_map()) <= 7:
                    tb_result = tablebase.probe_wdl(board)
                    if tb_result is not None:
                        return tablebase.probe_root(board).move
        except Exception as e:
            print(f"Tablebase error: {e}")

        return None

    def evaluate_endgame(self, board: chess.Board) -> int:
        """
        Basic evaluation for endgame positions based on king activity,
        pawn structure, and piece mobility.
        """
        return (
            self.evaluate_king_activity(board) +
            self.evaluate_pawn_structure(board) +
            self.evaluate_piece_mobility(board)
        )

    def evaluate_king_activity(self, board: chess.Board) -> int:
        """
        Score based on king centralization and activity.
        """
        score = 0
        for color in [chess.WHITE, chess.BLACK]:
            king_square = board.king(color)
            multiplier = 1 if color == chess.WHITE else -1

            # Bonus for centralization
            center_distance = abs(3.5 - chess.square_file(king_square)) + abs(3.5 - chess.square_rank(king_square))
            score += multiplier * (10 - int(center_distance))

        return score

    def evaluate_pawn_structure(self, board: chess.Board) -> int:
        """
        Score for passed, isolated, or supported pawns.
        """
        score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.PAWN:
                multiplier = 1 if piece.color == chess.WHITE else -1
                if self.is_passed_pawn(board, square, piece.color):
                    score += multiplier * 50
                if self.is_isolated_pawn(board, square, piece.color):
                    score -= multiplier * 30

        return score

    def is_passed_pawn(self, board: chess.Board, pawn_square: int, color: bool) -> bool:
        """
        Check if a pawn is passed.
        """
        file = chess.square_file(pawn_square)
        rank = chess.square_rank(pawn_square)

        for f in range(max(0, file - 1), min(8, file + 2)):
            ranks = range(rank + 1, 8) if color == chess.WHITE else range(rank - 1, -1, -1)
            for r in ranks:
                opponent_pawn = board.piece_at(chess.square(f, r))
                if opponent_pawn and opponent_pawn.piece_type == chess.PAWN and opponent_pawn.color != color:
                    return False

        return True

    def is_isolated_pawn(self, board: chess.Board, pawn_square: int, color: bool) -> bool:
        """
        Check if a pawn is isolated.
        """
        file = chess.square_file(pawn_square)
        for adj_file in [file - 1, file + 1]:
            if 0 <= adj_file <= 7:
                for rank in range(8):
                    adj_pawn = board.piece_at(chess.square(adj_file, rank))
                    if adj_pawn and adj_pawn.piece_type == chess.PAWN and adj_pawn.color == color:
                        return False

        return True

    def evaluate_piece_mobility(self, board: chess.Board) -> int:
        """
        Score based on the mobility of pieces.
        """
        score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                mobility = len(board.attacks(square))
                multiplier = 1 if piece.color == chess.WHITE else -1
                score += multiplier * mobility

        return score

if __name__ == "__main__":
    # Specify paths for opening book and tablebase
    opening_book = "E:/JOURNEY/3RD SEMESTER/AI/Project/M11.2.bin"
    tablebase = "E:/JOURNEY/3RD SEMESTER/AI/Project/Syzygy345"

    # Create the chess engine
    engine = ChessEngine(opening_book_path=opening_book, tablebase_path=tablebase)

    # Set up the initial board position
    board = chess.Board()

    # Perform analysis
    result = engine.analyze_position(board)

    # Display the results
    print("\nAnalysis:")
    print(f"Game Phase: {result.get('phase')}")
    if result.get('suggested_move'):
        print(f"Suggested Move: {result['suggested_move']}")
    if result.get('evaluation') is not None:
        print(f"Endgame Evaluation Score: {result['evaluation']}")


