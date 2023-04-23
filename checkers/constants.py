#constant varibles for checkers game
import pygame

#checker board dimensions 
WIDTH, HEIGHT = 600, 600
ROW, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

BLUE = (56, 152, 255) #main player's color
WHITE = (255, 255, 255) #checker color of opposing player
BLACK = (0, 0, 0) #normal color for checker squares
YELLOW = (255, 220, 0) #color of potential moveset
GREY = (208, 208, 208) #color of checker piece outline

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (54, 30)) #import crown image with adjusted width and height
OVERLAY = pygame.transform.scale(pygame.image.load('assets/Checker_Board_Overlay_Edit.png'), (600, 600)) #import number image for top of board
#color scheme: white, black, light blue, yellow
#light blue: #3898FF
#yellow: #FFDC00