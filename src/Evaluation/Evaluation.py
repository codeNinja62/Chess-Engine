import chess

class ChessEvaluation:
    def __init__(self):
        self.PIECE_VALUES = {
            'P': 100,
            'N': 300,
            'B': 300,
            'R': 500,
            'Q': 900,
            'K': 2000,
        }
        self.KING_SAFETY_PENALTY = 20
        self.PAWN_SHIELD_BONUS = 30
        self.TEMPO_BONUS = 10
        self.CONNECTIVITY_BONUS = 5
        self.ATTACK_UNIT_BONUS = 20
    def evaluate(self, board):
        material_score = self.evaluate_material(board)
        king_safety_score = self.evaluate_king_safety(board)
        center_control_score = self.evaluate_center_control(board)
        space_score = self.evaluate_space(board)
        connectivity_score = self.evaluate_connectivity(board)
        # trapped_pieces_score = self.evaluate_trapped_pieces(board)
        tempo_score = self.evaluate_tempo(board)
        king_tropism_score = self.evaluate_king_tropism(board)
        virtual_mobility_score = self.evaluate_virtual_mobility(board)
        pawn_storm_score = self.evaluate_pawn_storm(board)
        attack_units_score = self.evaluate_attack_units(board)
        total_score = (material_score + king_safety_score + center_control_score + space_score +
                       connectivity_score + tempo_score + king_tropism_score +
                       virtual_mobility_score + pawn_storm_score + attack_units_score)
        return total_score

    def evaluate_material(self, board):
        material_score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                piece_value = self.PIECE_VALUES.get(piece.symbol().upper(), 0)
                if piece.color == chess.WHITE:
                    material_score += piece_value
                else:
                    material_score -= piece_value
        return material_score

    def evaluate_king_safety(self, board):
        king_safety_score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.symbol().upper() == 'K':
                if piece.color == chess.WHITE:
                    # Check for White king's pawn shield
                    if not (board.piece_at(chess.F2) and board.piece_at(chess.G2)):
                        king_safety_score -= self.KING_SAFETY_PENALTY
                elif piece.color == chess.BLACK:
                    # Check for Black king's pawn shield
                    if not (board.piece_at(chess.F7) and board.piece_at(chess.G7)):
                        king_safety_score += self.KING_SAFETY_PENALTY
        return king_safety_score


    def evaluate_center_control(self, board):
        center_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
        control_score = 0
        for square in center_squares:
            piece = board.piece_at(square)
            if piece:
                if piece.color == chess.WHITE:
                    control_score += 10
                else:
                    control_score -= 10
        return control_score

    def evaluate_space(self, board):
        space_score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                if piece.symbol().upper() == 'P':
                    if piece.color == chess.WHITE:
                        if square < chess.E4:
                            space_score += 5
                    elif piece.color == chess.BLACK:
                        if square > chess.D5:
                            space_score -= 5
        return space_score

    def evaluate_connectivity(self, board):
        connectivity_score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                if piece.symbol().upper() == 'P':
                    if piece.color == chess.WHITE:
                        if square % 8 in [1, 2]:
                            connectivity_score += self.CONNECTIVITY_BONUS
                    elif piece.color == chess.BLACK:
                        if square % 8 in [5, 6]:
                            connectivity_score -= self.CONNECTIVITY_BONUS
        return connectivity_score

    # def evaluate_trapped_pieces(self, board):
    #     trapped_score = 0
    #     for square in chess.SQUARES:
    #         piece = board.piece_at(square)
    #         if piece:
    #             if self.is_trapped(board, square):
    #                 penalty = 150
    #                 if piece.color == chess.WHITE:
    #                     trapped_score -= penalty
    #                     print(f"White {piece.symbol()} on {chess.square_name(square)} is trapped (-{penalty})")
    #                 else:
    #                     trapped_score += penalty
    #                     print(f"Black {piece.symbol()} on {chess.square_name(square)} is trapped (+{penalty})")
    #     return trapped_score


    # def is_trapped(self, board, square):
        
    #     piece = board.piece_at(square)
    #     if not piece:
    #         return False

    #     # Generate all legal moves for the current board position
    #     for move in board.legal_moves:
    #         if move.from_square == square:
    #             # Simulate the move and check if it's safe
    #             board.push(move)
    #             is_safe = not board.is_check()  # Simplified: Ensure move doesn't result in check
    #             board.pop()  # Undo the move
    #             if is_safe:
    #                 return False  # Piece has at least one safe move
    #     return True



    def evaluate_tempo(self, board):
        if board.turn == chess.WHITE:
            return self.TEMPO_BONUS
        else:
            return -self.TEMPO_BONUS

    def evaluate_king_tropism(self, board):
        tropism_score = 0
        white_king_square = board.king(chess.WHITE)
        black_king_square = board.king(chess.BLACK)
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                if piece.color == chess.WHITE:
                    tropism_score -= self.calculate_distance(square, black_king_square)
                else:
                    tropism_score += self.calculate_distance(square, white_king_square)
        return tropism_score

    def calculate_distance(self, square1, square2):
        file_distance = abs(chess.square_file(square1) - chess.square_file(square2))
        rank_distance = abs(chess.square_rank(square1) - chess.square_rank(square2))
        return file_distance + rank_distance

    def evaluate_virtual_mobility(self, board):
        mobility_score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                if piece.color == chess.WHITE:
                    mobility_score += len(board.attacks(square))
                else:
                    mobility_score -= len(board.attacks(square))
        return mobility_score

    def evaluate_pawn_storm(self, board):
        pawn_storm_score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.symbol().upper() == 'P':
                if piece.color == chess.WHITE:
                    if square > chess.E4:
                        pawn_storm_score -= 10
                elif piece.color == chess.BLACK:
                    if square < chess.D5:
                        pawn_storm_score += 10
        return pawn_storm_score

    def evaluate_attack_units(self, board):
        attack_units_score = 0
        white_king_square = board.king(chess.WHITE)
        black_king_square = board.king(chess.BLACK)
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                if piece.color == chess.WHITE:
                    if self.is_attacking_king_zone(square, black_king_square):
                        attack_units_score += self.ATTACK_UNIT_BONUS
                else:
                    if self.is_attacking_king_zone(square, white_king_square):
                        attack_units_score -= self.ATTACK_UNIT_BONUS
        return attack_units_score

    def is_attacking_king_zone(self, square, king_square):
        return self.calculate_distance(square, king_square) <= 2

