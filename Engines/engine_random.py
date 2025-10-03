import chess
import random
import Later_use.evaluation_minimax as eval_min

def random_engine(board, *args, **kwargs):
    """Playes only random moves."""
    return random.choice(list(board.legal_moves))