import pygame
import chess
import time

# Initialize pygame
pygame.init()

# Constants for the board size and tile size
BOARD_SIZE = 600
TILE_SIZE = BOARD_SIZE // 8

# Load chess piece images based on the given naming convention
PIECE_IMAGES = {
    'K': pygame.transform.scale(pygame.image.load('images/white-king.png'), (TILE_SIZE, TILE_SIZE)),
    'Q': pygame.transform.scale(pygame.image.load('images/white-queen.png'), (TILE_SIZE, TILE_SIZE)),
    'R': pygame.transform.scale(pygame.image.load('images/white-rook.png'), (TILE_SIZE, TILE_SIZE)),
    'B': pygame.transform.scale(pygame.image.load('images/white-bishop.png'), (TILE_SIZE, TILE_SIZE)),
    'N': pygame.transform.scale(pygame.image.load('images/white-knight.png'), (TILE_SIZE, TILE_SIZE)),
    'P': pygame.transform.scale(pygame.image.load('images/white-pawn.png'), (TILE_SIZE, TILE_SIZE)),
    'k': pygame.transform.scale(pygame.image.load('images/black-king.png'), (TILE_SIZE, TILE_SIZE)),
    'q': pygame.transform.scale(pygame.image.load('images/black-queen.png'), (TILE_SIZE, TILE_SIZE)),
    'r': pygame.transform.scale(pygame.image.load('images/black-rook.png'), (TILE_SIZE, TILE_SIZE)),
    'b': pygame.transform.scale(pygame.image.load('images/black-bishop.png'), (TILE_SIZE, TILE_SIZE)),
    'n': pygame.transform.scale(pygame.image.load('images/black-knight.png'), (TILE_SIZE, TILE_SIZE)),
    'p': pygame.transform.scale(pygame.image.load('images/black-pawn.png'), (TILE_SIZE, TILE_SIZE))
}

# Function to draw the board
def draw_board(screen, board):
    for row in range(8):
        for col in range(8):
            color = (255, 255, 255) if (row + col) % 2 == 0 else (125, 135, 150)
            pygame.draw.rect(screen, color, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            
            piece = board.piece_at(chess.square(col, 7-row))  # Correct orientation
            if piece:
                piece_image = PIECE_IMAGES[piece.symbol()]
                screen.blit(piece_image, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Set up the display
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Realtime Chess Animation")
# Main game loop
running = True
frame_delay = 100  # Time in milliseconds between frames (1 second per frame)
fen_index = 0  # Index to track the current FEN string


# ascii_board = """
# r n b q k b n r
# p p p p p p p p
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# P P P P P P P P
# R N B Q K B N R
# """
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
    # fen_str = ascii_to_fen(ascii_str)
    fen_str = ascii_str
    screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    pygame.display.set_caption("Realtime Chess Animation")
    board = chess.Board(fen_str)
    screen.fill((0, 0, 0))  # Clear the screen
    draw_board(screen, board)  # Draw the board for the current FEN
    pygame.display.flip()
# while(1):
#     update_board(ascii_to_fen(ascii_board))
#     time.sleep(0.2)
#     update_board(ascii_to_fen(ascii_board2))
#     time.sleep(0.2)
#     update_board(ascii_to_fen(ascii_board))