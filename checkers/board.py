#file for drawing game board
import pygame
from .constants import BLUE, BLACK, WHITE, ROW, SQUARE_SIZE, COLS
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.blue_left = self.white_left = 12
        self.blue_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        #drawing checkerboard pattern
        for row in range(ROW):
            for col in range (row % 2, ROW, 2):
                #defines where to draw squares, what color, and how big
                pygame.draw.rect(win, BLUE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # ----------------MOVING PIECES----------------
    def move(self, piece, row, col):
        #moving selected piece to desired place by swapping indices
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)
        #pieces become king by moving to opposite side of board (row 0 or row 7)
        if row == ROW or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.blue_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]




    #sets up pieces on board when created
    def create_board(self):
        for row in range(ROW):
            self.board.append([]) #shows what is in each row
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0) #no pieces in rows 3 or 4
                else:
                    self.board[row].append(0)
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROW):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)


