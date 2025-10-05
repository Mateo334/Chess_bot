from paranoid_king_v1.paranoid_king import Negamax_ab_it as pkv1
from chess import Board
with open("test.txt", 'r') as file:
    a = [x.strip() for x in file.readlines()]

for i,line in enumerate(a):
    if(i%3==0):
        board = Board(line)
    if(i%3==1):
        moves = line
    if(i%3==2):
        elo = line
        ls_moves = moves.split()
        for j in range(len(ls_moves)):
            move = pkv1(board, 1 if j%2 ==0  else 0, 0.1)
            print(board.san(move), ls_moves[j])
            if(board.san(move) != ls_moves[j]):
                # print("Test failed, elo: ", elo)
                print("Test failed, elo: ", elo, "Progress: ", j/(len(ls_moves)))
                break
            board.push(move)
        if(j == len(ls_moves)-1):
            print("Test passed! elo: ", elo)
    
    
    
#https://wtharvey.com/