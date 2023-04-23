#file for drawing game board
import pygame
from .constants import BLUE, BLACK, WHITE, ROW, SQUARE_SIZE, COLS, OVERLAY, WIDTH, HEIGHT
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.blue_left = self.white_left = 12
        self.blue_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        #drawing checkerboard pattern
        for row in range(ROW):
            for col in range (row % 2, COLS, 2):
                #defines where to draw squares, what color, and how big
                pygame.draw.rect(win, BLUE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        win.blit(OVERLAY,(0,0))

    def evaluate(self):
        return self.white_left - self.blue_left + (self.white_kings * 0.5 - self.blue_kings * 0.5)
    
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
    
    # ----------------MOVING PIECES----------------
    def move(self, piece, row, col):
        #moving selected piece to desired place by swapping indices
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)
        #pieces become king by moving to opposite side of board (row 0 or row 7)
        if row == ROW-1 or row == 0:
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

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLUE:
                    self.blue_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.blue_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return BLUE
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLUE or piece.king:
            moves.update(self._traverse_left(row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row+3, ROW), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row+3, ROW), 1, piece.color, right))
        return moves
    
    #finding valid moves when moving left
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            #decides if double/triple jump is possible
            if current == 0:
                #skipped over a piece and nothing else to skip
                if skipped and not last:
                    break
                #skipped and found something else to skip over
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROW)
                    moves.update(self._traverse_left(r + step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves


    #finding valid moves when moving right
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            #decides if double/triple jump is possible
            if current == 0:
                #skipped over a piece and nothing else to skip
                if skipped and not last:
                    break
                #skipped and found something else to skip over
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROW)
                    moves.update(self._traverse_left(r + step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves