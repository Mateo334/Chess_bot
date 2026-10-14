from .evaluation import evaluate
from .ordering import order_moves
import sys
import time as t


t_table = {} #Need the position, depth reached from it and the evaluation 

def board_hash(board):
    return board.fen()


def Negamax_ab_it(board, color, time_limit):
    """Negamax with alpha beta pruning and Iterative Deepening."""
    deadline = t.monotonic() + time_limit
    if board.is_game_over():
        return None
    move = next(iter(board.legal_moves), None)
    pv_move = None
    global t_table 
    for depth in range(1, 40): #Calling the recursive function through all values of depth
        try:
            pos_move, _, _pv = nega_ab_it(board, color, depth, -sys.maxsize, sys.maxsize, depth, pv_move, deadline=deadline)
        except TimeoutError:
            break
        if pos_move is not None:
            move = pos_move
            pv_move = move
    return move
# What do i need
# A list of values assigned to the n+1 nodes - to pass as the PV
# int depth to know how far we want to go next - iterate with +1

def nega_ab_it(board, color, depth, alpha, beta, depth_called ,pv_move = None, deadline=None):
    """Negamax recursive function with alpha beta and iterative deepening"""
    global t_table
    if deadline is not None and t.monotonic() >= deadline:
        raise TimeoutError
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
        if deadline is not None and t.monotonic() >= deadline:
            raise TimeoutError
        board.push(move)
        try:
            # b_hash = board_hash(board)
            board_key = board_hash(board)
            b_hash = t_table.get(board_key)
            if(not b_hash or b_hash["depth"] < depth_called):
                _, score, child_pv = nega_ab_it(board, not color, depth-1, -beta, -alpha, depth_called, deadline=deadline)
                t_table[board_key] = {"depth":depth, "score": -score}
                score = -score
            else:
                if(not color):
                    score = b_hash["score"]
                else:
                    score = -b_hash["score"]
                print("Board used! with depth: ", b_hash["depth"])
                child_pv = []
        finally:
            board.pop()
        if best_move is None or score > maximum:
            maximum = score 
            best_move = move
            pv = [move] + child_pv
            alpha = max(alpha, score)
        if(score >= beta):
            break
    return best_move, maximum, pv


