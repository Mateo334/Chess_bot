import chess
import random
import os
import time as t
from Later_use.engines import *
import Later_use.engines as engines
import itertools
from Later_use.pyview import update_board
# Create a chess board
board = chess.Board()
# chess.Board.fen
def clear_screen():
    # Clear the terminal screen based on the operating system
    os.system("cls" if os.name == "nt" else "clear")  # "nt" is for Windows, "clear" is for macOS/Linux
def play_tournament(engine1, engine2, num_of_games, need_depth1, need_depth2):
    win_rate = [0,0,0]
    for i in range(num_of_games):
        engine1_is_white = random.randint(0,1)
        while not board.is_game_over():
            t.sleep(0.5)
            # clear_screen()  # Clear the screen (refresh the terminal)
            update_board(board.fen())
            if(board.turn == chess.WHITE):# Its whites turn to move eg. move 1
                # t.sleep(0.51)
                
                if(engine1_is_white):
                    # if(need_depth1):
                    #     board.push(engine1(board, 2))
                    #     continue
                    board.push(engine1(board))
                else:
                    # if(need_depth2):
                    board.push(engine2(board))
                        # continue
                # board.push(engine2(board))
            else:
                # t.sleep(0.51)
                if(engine1_is_white):
                    # if(need_depth2):
                    board.push(engine2(board))
                        # continue
                    # board.push(engine2(board))
                else:
                    # if(need_depth1):
                    #     board.push(engine1(board, 2))
                    #     continue
                    board.push(engine1(board))
                    
                
        if(board.is_checkmate()):
            if(board.turn == chess.WHITE):
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
        clear_screen()  # Clear the screen one last time after the game ends
        print(board)  # Display the final position
        print("Game Over!", win_rate, str(engine1.__name__), str(engine2.__name__))  

        board.reset()
    with open('filename.txt', 'a') as file:
        file.write('\n')
        file.write(engine1.__name__ + " " + engine2.__name__ +" "+ str(win_rate))
        # file.write("This is another line.")
tic = t.time()
play_tournament(random_mtc,random_mct,3, 0,1)




def permute_players(num_matches):
    """Plays the whole tournament. Each engine against each other. Even against the same one."""
    # Maybe modify it if there is a game, either to skip it, or add to the previous list. Can pass this as a parameter. 
    player_list = []
    matches_played = []
    with open("filename.txt", "r") as file:
        # lines = file.readlines()
        for line in file:
            if(line.strip()):
                matches_played.append((line.strip().split())[:2])
    for played in matches_played:   
        played[0], played[1] = getattr(engines, played[0]),getattr(engines, played[1])
    matches_played = [(el[0], el[1]) for el in matches_played]
    with open('engine_list.txt', 'r') as file:
        for line in file:
            player_list.append(getattr(engines, line.strip()))
    matches = list(itertools.product(player_list, repeat=2))
    for match in matches:
        should_continue = 0
        for el in matches_played:
            if(match == el):
                # print("skipping rally", el)
                should_continue = 1
                break
        if(should_continue): continue
        play_tournament(match[0], match[1],num_matches)
# permute_players(1)
print(t.time()-tic)
