bit_version = 110000000000000
evaluation_version = 1000000000
from .evaluation import evaluate
from .ordering import order_moves
import sys
import time as t
# import chess
# from chess import Board
# # Board.generate_legal_moves
# board = chess.Board()
# board.set_fen("r2q1rk1/pp1b1ppp/2n2n2/2bp4/2B1P3/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 0 10")
# Minimax(board)

def Minimax(board, color, bit_version, evaluation_version, *args):
    move, _ = maxi(board, 2, color)
    return move
def maxi(board, depth, color, time=1):
    if(depth==0):
        if(not color):
            return None, -evaluate(board, evaluation_version)
        return None, evaluate(board, evaluation_version)
    maximum = -sys.maxsize
    legal_moves = board.generate_legal_moves()
    best_move = None
    for move in legal_moves:
        board.push(move)
        _, score = mini(board, depth-1, color)  
        board.pop()
        if(score>maximum):
            maximum = score 
            best_move = move
    return best_move, maximum   
def mini(board, depth, color,  time=1):
    if(depth==0):
        if(not color):
            return None, -evaluate(board, evaluation_version)
        return None, evaluate(board, evaluation_version)
    minimum = sys.maxsize
    legal_moves = board.generate_legal_moves()
    best_move = None
    for move in legal_moves:
        board.push(move)
        _, score = maxi(board, depth-1, color)
        board.pop()  
        if(score<minimum):
            minimum = score 
            best_move = move
    return best_move, minimum
    
    
def Negamax(board, color, bit_version, evaluation_version,*args):
    move, _ = maxi(board, 2, color)
    return move
def negamax(board, depth, color, time=1):
    if(depth==0):
        if(not color):
            return None, -evaluate(board, evaluation_version)
        return None, evaluate(board, evaluation_version)
    maximum = -sys.maxsize
    legal_moves = board.generate_legal_moves()
    best_move = None
    for move in legal_moves:
        board.push(move)
        _, score = -negamax(board, depth-1, color)  
        board.pop()
        if(score>maximum):
            maximum = score 
            best_move = move
    return best_move, maximum   
    
# negamax(board)
def Minimax_ab(board, color,bit_version, evaluation_version, *args):
    move, _ = maxi_ab(board, 3,color, -sys.maxsize, sys.maxsize)
    return move
def maxi_ab(board, depth, color, alpha, beta, time=1):
    if(depth==0):
        if(not color):
            return None, -evaluate(board, evaluation_version)
        return None, evaluate(board, evaluation_version)
    maximum = -sys.maxsize
    legal_moves = board.generate_legal_moves()
    best_move = None
    for move in legal_moves:
        board.push(move)
        _, score = mini_ab(board, depth-1, color, alpha, beta) 
        board.pop()
        if(score>maximum):
            maximum = score 
            best_move = move
            if(score>alpha):
                alpha = score
        if(score>beta):
            return None, maximum
    return best_move, maximum   
def mini_ab(board, depth, color,alpha, beta, time=1):
    if(depth==0):
        if(not color):
            return None, -evaluate(board, evaluation_version)
        return None, evaluate(board, evaluation_version)
    minimum = sys.maxsize
    legal_moves = board.generate_legal_moves()
    best_move = None
    for move in legal_moves:
        board.push(move)
        _, score = maxi_ab(board, depth-1, color, alpha, beta)
        board.pop()  
        if(score<minimum):
            minimum = score 
            best_move = move
            if(score<beta):
                beta = score
        if(score<alpha):
            return None, minimum
    return best_move, minimum



def Negamax_ab(board, color, *args):
    """Negamax with alpha beta pruning"""
    move, _ = nega_ab(board, 5,color, -sys.maxsize, sys.maxsize)
    return move
def nega_ab(board, depth, color, alpha, beta, time=1):
    if(depth==0 or board.is_game_over()):
        # if(board.is_game_over()):
        #     print("I see Mate ", depth)
        if(not color):
            return None, -evaluate(board, evaluation_version)
        return None, evaluate(board, evaluation_version)
    maximum = -sys.maxsize
    legal_moves = board.generate_legal_moves()
    
    best_move = None
    legal_moves = order_moves(board, legal_moves, 1111)
    for move in legal_moves:
        board.push(move)
        _, score = nega_ab(board, depth-1, not color, -beta, -alpha)  
        score = -score
        board.pop()
        if(score>maximum):
            maximum = score 
            best_move = move
            if(score >alpha):
                alpha = score
        if(score >= beta):
            return best_move, maximum
    return best_move, maximum 



def Negamax_ab_it(board, color, time_limit):
    """Negamax with alpha beta pruning and Iterative Deepening."""
    start_time = t.time()
    pv_move = []
    for depth in range(1, 40):
        if(t.time() - start_time >= time_limit):
            # print("Depth reached: ", depth)
            print(long_pv)
            return move
        move, _  ,pv = nega_ab_it(board,color,depth, -sys.maxsize, sys.maxsize, pv_move)
        if(move):
            #Using only the next move in the sequence
           pv_move = move 
           long_pv = pv
    
    return move
# What do i need
# A list of values assigned to the n+1 nodes - to pass as the PV
# int depth to know how far we want to go next - iterate with +1

def nega_ab_it(board, color, depth, alpha, beta,  pv_move = None):
    if(depth ==0 or board.is_game_over()):
        if(not color):
            return None, -evaluate(board, evaluation_version), []
        return None, evaluate(board, evaluation_version), []
    pv = []
    maximum = -sys.maxsize
    legal_moves = board.generate_legal_moves()
    best_move = None
    legal_moves = order_moves(board, legal_moves, 1)
    if pv_move in legal_moves:
        legal_moves.remove(pv_move)
        legal_moves.insert(0, pv_move)
    for move in legal_moves:
        board.push(move)
        _, score, child_pv = nega_ab_it(board, not color, depth-1, -beta, -alpha)  
        score = -score
        board.pop()
        if(score>maximum):
            maximum = score 
            best_move = move
            pv = [move] + child_pv
            if(score >alpha):
                alpha = score
        if(score >= beta):
            break
    return best_move, maximum, pv
#NEXT TRY TO SORT THE WHOLE BY THE SCORE OF ALL MOVES IN PREVIOUS DEPTH
#