#main file for rendering and drawing checkers
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board
FPS = 60

#set up display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Vocal Checkers')

#------------------------PIECE SELECTION FINDER------------------------
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board() #creates board
    #event loop
    while run:
        clock.tick(FPS) #sets game to run at 60 frames per second
        for event in pygame.event.get(): #checks if event is triggered
            if event.type == pygame.QUIT:
                run = False #ends game
            #run event if mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        board.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()


