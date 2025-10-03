import chess
import random
import os
import time as t
import itertools
import tracemalloc
from Engines import engine_random, paranoid_king, evaluation
random_moves = engine_random.random_engine
minimax = paranoid_king.Minimax
negamax = paranoid_king.Negamax

minimax_ab = paranoid_king.Minimax_ab
negamax_ab = paranoid_king.Negamax_ab

iterative_negamax = paranoid_king.Negamax_ab_it
# from Engines import evaluation
paranoid_king.bit_version = 110000000000000
paranoid_king.evaluation_version = 111000000000000
# from Engines.paranoid_king import bit_version, evaluation_version
# bit_version =0
# evaluation_version = 0

board = chess.Board()
from san_converter import convert_whole_text

def play_tournament(engine1, engine2, num_of_games, max_moves=2000, thinking_time = 0.02):
    win_rate = [0, 0, 0]  # [engine1 wins, engine2 wins, draw]
    moves_average = 0
    tic = t.time()
    for i in range(num_of_games):
        board.reset()
        engine1_is_white = bool(random.getrandbits(1))
        move_count = 0
        moves_this_game=[]
        while not board.is_game_over() and move_count < max_moves:
            toc = t.time()
            if board.turn:
                move = engine1(board,engine1_is_white, thinking_time) if engine1_is_white else engine2(board,not engine1_is_white, thinking_time)
                moves_this_game.append(move)
            else:
                move = engine2(board,not engine1_is_white, thinking_time) if engine1_is_white else engine1(board,engine1_is_white, thinking_time)
                moves_this_game.append(move)
            if move is None:
                print("NoneType detected")
                # print(board.is_checkmate())
                # print(board.is_game_over())
                print(list(board.generate_legal_moves()))
                print(board)
                # continue
            board.push(move)
            # print(t.time()-toc)
            # print(board)
            move_count += 1
        if i%1==0:
            print(f"Game {i} over")
        if 1:
            with open("games_played.txt", 'a') as file:
                file.write(str(engine1.__name__) + " vs "+ str(engine2.__name__) + " | " 
                           + "Number of moves: " + str(len(moves_this_game)) + " | " + "engine1 is white: " 
                           +  str(engine1_is_white) + " | " + "Time Elapsed: " + f"{(t.time()-tic):.2f}"  '\n')
                file.write(" ".join([str(i) for i in moves_this_game if i])+ '\n')
            moves_average +=len(moves_this_game)
        if(board.is_checkmate()):
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
        # file.write("Time average: " + f"{(t.time()-tic)/num_of_games:.2f}")
    print("Average moves: ", moves_average/num_of_games)
    total_winrate = (win_rate[-1]+0.5*win_rate[0])/num_of_games
    print("Rating of Engine: ", total_winrate+100/moves_average)
    print("Time average: " + f"{(t.time()-tic)/num_of_games:.2f}")
    # with open('against_random')
play_tournament(random_moves, iterative_negamax, 1, thinking_time=0.01)
convert_whole_text()




# def permute_players(num_matches):
#     """Plays the whole tournament. Each engine against each other. Even against the same one."""
#     # Maybe modify it if there is a game, either to skip it, or add to the previous list. Can pass this as a parameter. 
#     player_list = []
#     matches_played = []
#     with open("filename.txt", "r") as file:
#         # lines = file.readlines()
#         for line in file:
#             if(line.strip()):
#                 matches_played.append((line.strip().split())[:2])
#     for played in matches_played:   
#         played[0], played[1] = getattr(engines, played[0]),getattr(engines, played[1])
#     matches_played = [(el[0], el[1]) for el in matches_played]
#     with open('engine_list.txt', 'r') as file:
#         for line in file:
#             player_list.append(getattr(engines, line.strip()))
#     matches = list(itertools.product(player_list, repeat=2))
#     for match in matches:
#         should_continue = 0
#         for el in matches_played:
#             if(match == el):
#                 # print("skipping rally", el)
#                 should_continue = 1
#                 break
#         if(should_continue): continue
#         play_tournament(match[0], match[1],num_matches)
# permute_players(1)
# print(t.time()-tic)
