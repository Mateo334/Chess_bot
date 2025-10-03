import chess
import random
import Later_use.evaluation_minimax as eval_min

def random_moves(board):
    """Playes only random moves."""
    return random.choice(list(board.legal_moves))
def random_mct(board):
    """Playes these in descending priority order - mate, check, takes. Otherwise plays random moves."""
    legal_moves = list(board.legal_moves)
    for move in legal_moves:
        board.push(move)
        if(board.is_checkmate()):
            board.pop()
            return move
        if(board.is_check()):
            board.pop()
            return move
        board.pop()
    if(list(board.generate_legal_captures())):
        return list(board.generate_legal_captures())[0]
    return random.choice(list(board.legal_moves))
def random_mtc(board):
    """Playes these in descending priority order - mate, takes, check. Otherwise plays random moves."""
    legal_moves = list(board.legal_moves)
    for move in legal_moves:
        board.push(move)
        if(board.is_checkmate()):
            board.pop()
            return move
        board.pop()
    if(list(board.generate_legal_captures())):
        return list(board.generate_legal_captures())[0]
    for move in legal_moves:
        board.push(move)
        if(board.is_check()):
            board.pop()
            return move
        board.pop()
    return random.choice(list(board.legal_moves))
    

def minimax(board, depth, maxdepth = 2):
    """"""
    total = 0
    if(depth == 0):
        return eval_min.complete_eval(board)
    legal_moves = list(board.legal_moves)
    best_move = None
    if(board.turn): #maximizing
        maximum = float("-inf")
        for move in legal_moves:
            board.push(move)
            total = minimax(board, depth-1)
            board.pop()
            if(total > maximum):
                maximum = total
                best_move = move
        return best_move if depth==maxdepth else maximum
    elif(not board.turn): #minimizing
        minimum = float("inf")  
        for move in legal_moves:
            board.push(move)
            total = minimax(board, depth-1)
            board.pop()
            if(total < minimum):
                minimum = total
                best_move = move
        
        return best_move if depth==maxdepth else minimum
    return best_move

def negamax(board, depth, maxdepth = 2):
    """"""
    if(depth == 0):
        return eval_min.complete_eval(board)
    legal_moves = list(board.legal_moves)
    best_move = None
    maximum = float("-inf")
    for move in legal_moves:
        board.push(move)
        total = -minimax(board, depth-1)
        board.pop()
        if(total > maximum):
            maximum = total
            best_move = move
    return best_move if depth==maxdepth else maximum
    # return best_move

    



# def minimax
# def negamax
# def minimax alpha beta
# def negamax alpha beta
# def iterative minimax alpha beta
# def iterative negamax alpha beta