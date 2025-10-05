from .evaluation import evaluate
from .ordering import order_moves
import sys
import time as t



def Negamax_ab_it(board, color, time_limit):
    """Negamax with alpha beta pruning and Iterative Deepening."""
    start_time = t.time()
    pv_move = []
    for depth in range(1, 40): #Calling the recursive function through all values of depth
        if(t.time() - start_time >= time_limit):
            # print("Depth reached: ", depth)
            # print(long_pv)
            return move
        move, _  ,pv = nega_ab_it(board,color,depth, -sys.maxsize, sys.maxsize, pv_move)
        if(move): #Is not None
            #Using only the next move in the sequence
           pv_move = move 
        #    long_pv = pv
    return move
# What do i need
# A list of values assigned to the n+1 nodes - to pass as the PV
# int depth to know how far we want to go next - iterate with +1

def nega_ab_it(board, color, depth, alpha, beta,  pv_move = None):
    """Negamax recursive function with alpha beta and iterative deepening"""
    if(depth ==0 or board.is_game_over()):
        if(not color):
            return None, -evaluate(board), []
        return None, evaluate(board), []
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