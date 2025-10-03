import chess
import numpy as np
import chess.pgn

piece_eval = np.array([100,300,300,500,900])
def complete_eval(board):
    total = 0
    total += evaluate_scalar(board)
    total += consider_end(board)
    return total
def evaluate_scalar(board):
    """Evaluates the board only piece-wise."""
    white_pieces = np.array([len(board.pieces(chess.PAWN, chess.WHITE)), len(board.pieces(chess.KNIGHT, chess.WHITE)), len(board.pieces(chess.BISHOP, chess.WHITE)), len(board.pieces(chess.ROOK, chess.WHITE)), len(board.pieces(chess.QUEEN, chess.WHITE))])
    black_pieces = np.array([len(board.pieces(chess.PAWN, chess.BLACK)), len(board.pieces(chess.KNIGHT, chess.BLACK)), len(board.pieces(chess.BISHOP, chess.BLACK)), len(board.pieces(chess.ROOK, chess.BLACK)), len(board.pieces(chess.QUEEN, chess.BLACK))]) 
    return sum(white_pieces*piece_eval - black_pieces*piece_eval)

def consider_end(board):
    if(board.is_checkmate()):
        if(board.turn == chess.WHITE):
            return float("-inf")
        else: 
            return float("inf")
    elif(board.is_stalemate()):
        return -10
    return 0
        
    
    
    
    
    
    