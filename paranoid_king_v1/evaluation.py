import chess
from chess import Board
board = chess.Board()
board.set_fen("r2q1rk1/pp1b1ppp/2n2n2/2bp4/2B1P3/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 0 10")
import sys
from .square_tables import *

def evaluate(board, bit_string, *optional_string): #White has a positive evaluation score
    bit_string = str(bit_string)
    optional_string = str(optional_string)
    """Evaluates based on the bit string given. 1 = True for the given level.
    Level progression is: Scalar(Fixed vals), Piece tables(Fixed vals), Mobility, King safety, Pawn structure, 
    Piece coordination(rook in open files...), Tactical pieces(bishop attacking which piece...),
    Phase dependency, ML..."""
    eval_value = 0
    if(bit_string[0]):
        cur_val = 0
        values = [1,3,3,5,9,10000]
        for piece_type in chess.PIECE_TYPES:# Iterating over all pieces
            white_piece_pos = board.pieces(piece_type, chess.WHITE)
            black_piece_pos = board.pieces(piece_type, chess.BLACK)
            cur_val += values[piece_type-1]*len(white_piece_pos)
            cur_val -= values[piece_type-1]*len(black_piece_pos)
        eval_value +=cur_val
    if(bit_string[1]):
        if(board.is_checkmate()):
            # print("checkmate")
            if(board.turn):#White to move
                return -sys.maxsize
            else:
                return sys.maxsize
        elif(board.is_stalemate()):
            if(eval_value>0):
                return -1
            elif(eval_value<0):
                return 0#Modify later
    if(bit_string[2]):
        #Piece square tables
        opening = [pawn_open,knight_open, bishop_open, rook_open, queen_open, king_open]
        for i, piece_type in enumerate(chess.PIECE_TYPES):
            white_piece_pos = board.pieces(piece_type, chess.WHITE)
            black_piece_pos = board.pieces(piece_type, chess.BLACK)
            white_piece = list(white_piece_pos)
            black_piece = list(black_piece_pos) 
            eval_value += sum([opening[i][piece] for piece in white_piece])/10000
            eval_value -= sum([opening[i][chess.square_mirror(piece)] for piece in black_piece])/10000
            # print("Eval value: ", sum([opening[i][chess.square_mirror(piece)] for piece in black_piece])/100)
    return eval_value
# evaluate(board, 1, 1)