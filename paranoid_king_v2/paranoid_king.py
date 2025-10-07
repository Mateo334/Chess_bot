from .evaluation import evaluate
from .ordering import order_moves
import sys
import time as t


t_table = {} #Need the position, depth reached from it and the evaluation 

def board_hash(board):
    return board.fen()


def Negamax_ab_it(board, color, time_limit):
    """Negamax with alpha beta pruning and Iterative Deepening."""
    start_time = t.time()
    pv_move = []
    global t_table 
    for depth in range(1, 40): #Calling the recursive function through all values of depth
        if(t.time() - start_time >= time_limit):
            # print("Depth reached: ", depth)
            # print(long_pv)
            
            if(depth>6):
                with open("tt.txt", 'a') as file:
                    file.write(str(t_table) + '\n')
            return move
        move, _  ,pv = nega_ab_it(board,color,depth, -sys.maxsize, sys.maxsize,depth, pv_move)
        if(move): #Is not None
            #Using only the next move in the sequence
        #    pv_move = move 
           pv_move = pv[0]
        #    long_pv = pv
    return move
# What do i need
# A list of values assigned to the n+1 nodes - to pass as the PV
# int depth to know how far we want to go next - iterate with +1

def nega_ab_it(board, color, depth, alpha, beta, depth_called ,pv_move = None):
    """Negamax recursive function with alpha beta and iterative deepening"""
    global t_table
    if(depth ==0 or board.is_game_over()):
        b_hash = board_hash(board)
        t_table[b_hash] = {"depth":depth_called, "score": evaluate(board)}
        sc_val = t_table[b_hash]["score"]
        if(not color):
            return None, -sc_val, []
        return None, sc_val, []
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
        # b_hash = board_hash(board)
        board_key = board_hash(board)
        b_hash = t_table.get(board_key)
        if(not b_hash or b_hash["depth"] < depth_called):
            _, score, child_pv = nega_ab_it(board, not color, depth-1, -beta, -alpha, depth_called)
            t_table[board_key] = {"depth":depth, "score": -score}
            score = -score
        else:
            if(not color):
                score = b_hash["score"]
            else:
                score = -b_hash["score"]
            print("Board used! with depth: ", b_hash["depth"])
            child_pv = []
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


