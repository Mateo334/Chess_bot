import chess
import random
import os
import time as t
import numpy as np


# def gather_engines():
#     engine_list = []
#     for file in os.listdir("Engines"):
#         if ".py" in file and "init" not in file:
#             engine_list.append(file[:-3])
#             print(file[:-3])
# gather_engines()
    
def new_engine_play():
    return 0
board = chess.Board()

# def clear_screen():
#     # Clear the terminal screen based on the operating system
#     os.system("cls") 
# clear_screen()
def play_game(number_of_games):
    """Plays two engines against each other. Currently the first move in alphabetical order
    and random."""
    moves_played = []
    tic = t.time()
    for i in range (0,number_of_games):
        moves_this_game = []
        board.reset()
        while not board.is_game_over():
            if(board.turn):# Its white turn to move eg. move 1
                
                legal_moves = list(board.legal_moves)
                first_move = legal_moves[0]
                board.push(first_move)
                moves_this_game.append(first_move)
            else:
                legal_moves = tuple(board.legal_moves)
                random_move = random.choice(legal_moves)
                board.push(random_move)
                moves_this_game.append(random_move)
        if(moves_this_game): #Write all moves played into file
            with open("games_played.txt", 'a') as file:
                file.write("Engine1" + " vs "+ "Engine2" + " | " + "Number of moves: " + str(len(moves_this_game)) + '\n')
                file.write(" ".join([str(i) for i in moves_this_game if i])+ '\n')
        if i%50==0:
            print("Percentage played",100*i/number_of_games, str(len(moves_this_game)))
    total_games_time = t.time()-tic
    print(board)  # Display the final position
    print("Total time: ", total_games_time)
    print("Avg time per game: ", total_games_time/number_of_games)
    print("Games played: ", number_of_games)
    print("Game Over!")  
    with open("game_optimization.txt", 'a') as file:
        file.write(f"Games: {number_of_games:}" +"  "+  f"Total time: {total_games_time:.4}" + " "
                   + f"Avg time[ms]: {1000*total_games_time/number_of_games:.4}" + '\n')
    print(moves_played)
# play_game(100)
# Indicate the game has finished
