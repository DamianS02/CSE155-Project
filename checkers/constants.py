#constant varibles for checkers
import pygame

#checker board dimensions 
WIDTH, HEIGHT = 600, 600
ROW, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

BLUE = (56, 152, 255) #instead of red on checker board
WHITE = (255, 255, 255) #normal color for checker squares
BLACK = (0, 0, 0) #checker color of opposing player
YELLOW = (255, 220, 0) #color of potential moveset
GREY = (208, 208, 208) #color of checker piece outline

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (41.4, 23)) #import crown image with adjusted width and height
OVERLAY = pygame.transform.scale(pygame.image.load('assets/Checker_Board_Numbers.png'), (600, 600)) #import number image for top of board
#color scheme: white, black, light blue, yellow
#light blue: #3898FF
#yellow: #FFDC00