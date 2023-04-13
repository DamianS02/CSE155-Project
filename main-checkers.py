#main file for rendering and drawing checkers
import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
FPS = 60

#set up display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Vocal Checkers')

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()


