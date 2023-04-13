#file used for making checkers pieces
import pygame
from .constants import WHITE, BLUE, SQUARE_SIZE, GREY


class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False #if piece is king or not
        self.x = 0
        self.y = 0
        self.calc_pos()
        if self.color == BLUE:
            self.direction = -1 #blue pieces move up (y-axis - 1)
        else:
            self.direction = 1 #white pieces move down (y-axis + 1)



    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        #drawing outline of piece (big outer circle)
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        #drawing regular piece
        pygame.draw.circle(win, self.color, (self.x, self.y), radius - 2)

    #shows how object is represented when printed/returned (for debugging purposes)
    def __repr__(self):
        return str(self.color)
