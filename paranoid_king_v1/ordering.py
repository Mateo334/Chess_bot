# from chess import Board
# board = Board()
# board.set_fen("3B4/1r2p3/r2p1p2/bkp1P1p1/1p1P1PPp/p1P4P/PP1K4/3B4 w - - 0 1")
# board.set_board_fen("3B4/1r2p3/r2p1p2/bkp1P1p1/1p1P1PPp/p1P4P/PP1K4/3B4 w - - 0 1")
# moves = list(board.generate_legal_moves())
# print(moves)
# # print(board)
# print(list(board.generate_legal_captures()))
import chess
def order_moves(board, moves, bit_string, *optional_string):
    """Orders the moves based on the level of the bit_string. Goes like:
    First captures
    
    
    """
    bit_string = str(bit_string)
    legal_captures = list(board.generate_legal_captures())
    #Convert the generator to a list
    moves = list(moves)
    
    if(bit_string[0]):
        #Applies the MVV LVA
        val_list = []
        if legal_captures:
            for move in legal_captures:
                capturing_piece = board.piece_at(move.from_square).piece_type
                if(board.is_en_passant(move)):
                    captured_square = chess.square(chess.square_file(move.to_square),
                                        chess.square_rank(move.from_square))
                    captured_piece = board.piece_at(captured_square).piece_type
                else:
                    captured_square = move.to_square
                    captured_piece = board.piece_at(captured_square).piece_type
                val_list.append(captured_piece-capturing_piece)
        ordered_moves = [move for _, move in sorted(zip(val_list,legal_captures), key=lambda x: x[0], reverse=True)]
        for move in list(moves):
            if move not in ordered_moves:
                ordered_moves.append(move) 
    return ordered_moves

