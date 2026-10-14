from paranoid_king_v1.paranoid_king import Negamax_ab_it as cur_engine
from chess import Board
from pathlib import Path
with open(Path(__file__).with_name("test.txt"), 'r') as file:
    a = [x.strip() for x in file.readlines()]


time_limit = 1.2
for i,line in enumerate(a):
    if(i%3==0):
        board = Board(line)
    if(i%3==1):
        moves = line
    if(i%3==2):
        elo = line
        ls_moves = moves.split()
        for j in range(len(ls_moves)):
            move = cur_engine(board, board.turn, time_limit)
            if move is None or move not in board.legal_moves:
                print("Test failed: engine returned an invalid move:", move)
                break
            print(board.san(move), ls_moves[j])
            if(board.san(move) != ls_moves[j]):
                # print("Test failed, elo: ", elo)
                print("Test failed, elo: ", elo, "Progress: ", j/(len(ls_moves)))
                break
            board.push(move)
        else:
            print("Test passed! elo: ", elo)
    
    
    
#https://wtharvey.com/