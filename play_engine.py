import pygame
import chess
import time as t
import random
# from paranoid_king_v1.paranoid_king import Negamax_ab_it as pkv1
from paranoid_king_v2.paranoid_king import Negamax_ab_it as pkv1


# Constants for the board size and tile size
BOARD_SIZE = 600
TILE_SIZE = BOARD_SIZE // 8

# Load chess piece images based on the given naming convention
PIECE_IMAGES = {
    'K': pygame.transform.scale(pygame.image.load('Later_use/images/white-king.png'), (TILE_SIZE, TILE_SIZE)),
    'Q': pygame.transform.scale(pygame.image.load('Later_use/images/white-queen.png'), (TILE_SIZE, TILE_SIZE)),
    'R': pygame.transform.scale(pygame.image.load('Later_use/images/white-rook.png'), (TILE_SIZE, TILE_SIZE)),
    'B': pygame.transform.scale(pygame.image.load('Later_use/images/white-bishop.png'), (TILE_SIZE, TILE_SIZE)),
    'N': pygame.transform.scale(pygame.image.load('Later_use/images/white-knight.png'), (TILE_SIZE, TILE_SIZE)),
    'P': pygame.transform.scale(pygame.image.load('Later_use/images/white-pawn.png'), (TILE_SIZE, TILE_SIZE)),
    'k': pygame.transform.scale(pygame.image.load('Later_use/images/black-king.png'), (TILE_SIZE, TILE_SIZE)),
    'q': pygame.transform.scale(pygame.image.load('Later_use/images/black-queen.png'), (TILE_SIZE, TILE_SIZE)),
    'r': pygame.transform.scale(pygame.image.load('Later_use/images/black-rook.png'), (TILE_SIZE, TILE_SIZE)),
    'b': pygame.transform.scale(pygame.image.load('Later_use/images/black-bishop.png'), (TILE_SIZE, TILE_SIZE)),
    'n': pygame.transform.scale(pygame.image.load('Later_use/images/black-knight.png'), (TILE_SIZE, TILE_SIZE)),
    'p': pygame.transform.scale(pygame.image.load('Later_use/images/black-pawn.png'), (TILE_SIZE, TILE_SIZE))
}


def draw_board(screen, board, selected_square = None):
    """Draws the board using pygame."""
    for row in range(8):
        for col in range(8):
            color = (255, 255, 255) if (row + col) % 2 == 0 else (125, 135, 150)
            pygame.draw.rect(screen, color, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            piece = board.piece_at(chess.square(col, 7-row))  # Correct orientation
            if piece:
                piece_image = PIECE_IMAGES[piece.symbol()]
                screen.blit(piece_image, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    if selected_square is not None:
        col = chess.square_file(selected_square)
        row = 7 - chess.square_rank(selected_square)
        pygame.draw.rect(screen, (0,255,0), (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE), 4)

# Set up the display
pygame.init()
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Chess Game")


ascii_board = """
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
"""
# ascii_board2 = """
# r n b q k b K r
# p p p p p p K p
# . . . . . . b .
# . . . p . . . .
# . . . . n . B .
# . . . . . . . .
# P P P P P P P P
# R N B Q K B N R
# """
def ascii_to_fen(ascii_board):
    """Converts the ascii board representation to FEN notation."""
    fen_rows = []
    for row in ascii_board.strip().split('\n'):
        fen_row = ''
        empty_count = 0
        for char in row.split():
            if char in '.-':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_row += char
        if empty_count > 0:
            fen_row += str(empty_count)
        fen_rows.append(fen_row)
    return '/'.join(fen_rows) + ' w KQkq - 0 1'

def update_board(ascii_str):
    """Redraws the pygame display based on the ascii string."""
    fen_str = ascii_str
    screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    board = chess.Board(fen_str)
    draw_board(screen, board, selected_square)  # Draw the board for the current FEN
    pygame.display.flip()
    
board = chess.Board(ascii_to_fen(ascii_board))
running = True
selected_square = None
player_is_white = bool(random.getrandbits(1))
player_is_white = 1

def move_player(board, selected_square):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // TILE_SIZE
            row = 7 - (y // TILE_SIZE)
            square = chess.square(col, row)

            if selected_square is None:
                if board.piece_at(square):
                    selected_square = square
            else:
                move = chess.Move(selected_square, square)
                if move in board.legal_moves:
                    board.push(move)
                selected_square = None
    return selected_square
# Main loop
thinking_time = 0.05
selected_square = None
while running:
    if(board.turn):
        if(player_is_white):
            selected_square = move_player(board,selected_square)
        else:
            move = pkv1(board,1, thinking_time)
            board.push(move)
    else:
        if(not player_is_white):
            selected_square = move_player(board, selected_square)
        else:
            move = pkv1(board,0, thinking_time)
            board.push(move)
            
    # screen.fill((0,0,0))
    draw_board(screen, board, selected_square)
    pygame.display.flip()
    if(board.is_game_over()):
        t.sleep(2)
        board = chess.Board(ascii_to_fen(ascii_board))
        # running = False

   