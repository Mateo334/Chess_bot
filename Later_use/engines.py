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