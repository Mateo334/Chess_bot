#Converts the games_played to a san format for viewing
import os
import chess
from chess import Board
def convert_to_san(moves):
    board = chess.Board()
    san_moves = []
    for uci in moves:
        move = chess.Move.from_uci(uci)
        san_moves.append(board.san(move))
        board.push(move)
    san_moves = " ".join([f"{i+1}. {a} {b}" for i,(a,b) in enumerate(zip(san_moves[::2], san_moves[1::2]))])
    return san_moves
def convert_whole_text():
    with open('games_played.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        i=1
        for line in infile:
            if i % 2 == 0 and line[0]!='1':
                moves = line.strip().split()
                line = convert_to_san(moves) + '\n'
            outfile.write(line)
            i += 1
    os.replace('output.txt','games_played.txt')
# convert_whole_text()

# def long_to_short_algebraic():
