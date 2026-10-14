import chess
import random
import time as t
from Engines import engine_random
random_moves = engine_random.random_engine
from paranoid_king_v1.paranoid_king import Negamax_ab_it as pkv1


board = chess.Board()


def play_game(engine1, engine2, num_of_games, max_moves=2000, 
              thinking_time = 0.02, game_time = None):
    """Plays two engines agains each other. Parameters specify the number of games, 
    maximum moves per game and the thinking time for each move for each engine
    (Possibly change later) to switch to whole game time."""
    win_rate = [0, 0, 0]  # [engine1 wins, draws, engine2 wins]
    moves_average = 0
    tic = t.monotonic()
    for i in range(num_of_games):
        game_start= t.monotonic()
        board.reset()
        engine1_is_white = bool(random.getrandbits(1))
        move_count = 0
        moves_this_game=[]
        while not board.is_game_over() and move_count < max_moves:
            if board.turn:
                move = engine1(board,engine1_is_white, thinking_time) if engine1_is_white else engine2(board,not engine1_is_white, thinking_time)
                moves_this_game.append(move)
            else:
                move = engine2(board,not engine1_is_white, thinking_time) if engine1_is_white else engine1(board,engine1_is_white, thinking_time)
                moves_this_game.append(move)
            if move is None or move not in board.legal_moves:
                raise ValueError(f"Engine returned invalid move {move} for {board.fen()}")
            board.push(move)
            move_count += 1
        print(f"Game {i} over")
        with open("games_played.txt", 'a') as file:
            file.write(str(engine1.__name__) + " vs "+ str(engine2.__name__) + " | " 
                        + "Number of moves: " + str(len(moves_this_game)) + " | " + "engine1 is white: " 
                        +  str(engine1_is_white) + " | " + "Time Elapsed: " + f"{(t.monotonic() - game_start):.2f}"  '\n')
            file.write(" ".join([str(i) for i in moves_this_game if i])+ '\n')
        moves_average +=len(moves_this_game)
        if(board.is_checkmate()): #Update results
            if(board.turn):
                if(engine1_is_white):
                    win_rate[-1] +=1
                else:
                    win_rate[0] +=1
            else:
                if(engine1_is_white):
                    win_rate[0] +=1
                else:
                    win_rate[-1] +=1
        else:
            win_rate[1] +=1
    with open('filename.txt', 'a') as file:
        file.write('\n')
        file.write(engine1.__name__ + " " + engine2.__name__ +" "+ str(win_rate))
        print(engine1.__name__ + " " + engine2.__name__ +" "+ str(win_rate) + " ")
    print("Average moves: ", moves_average/num_of_games)
    score_rate = (win_rate[2] + 0.5 * win_rate[1]) / num_of_games
    print(f"Engine 2 score percentage: {score_rate:.1%}")
    print(f"Average seconds per game: {(t.monotonic() - tic) / num_of_games:.2f}")
    
if __name__ == "__main__":
    play_game(random_moves, pkv1, 10, thinking_time=0.005)