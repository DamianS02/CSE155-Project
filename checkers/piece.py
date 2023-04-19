#file used for making checkers pieces
import pygame
from .constants import WHITE, BLUE, SQUARE_SIZE, GREY, CROWN


class Piece:
    PADDING = 15
    OUTLINE = 3

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


    #calculates the position of the checker piece according to its row and column
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        #drawing outline of piece (big outer circle)
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        #drawing regular piece (inner circle)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        #draw crown if peice is king 
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()



    #shows how object is represented when printed/returned (for debugging purposes)
    def __repr__(self):
        return str(self.color)
