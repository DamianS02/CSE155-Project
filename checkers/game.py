#handling the game, whose turn, which piece moves etc.
import pygame
import speech_recognition as sr
import audio.speech
from .constants import BLUE, WHITE, YELLOW, SQUARE_SIZE
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.board = Board()
        print("Board initialized.")

    def update(self):
        if(self.board != None):
            self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        #what piece is selected
        self.selected = None
        #blue goes first
        self.turn = BLUE
        #shows current valid moves
        self.valid_moves = {} 
        self.moveset = {}

    def winner(self):
        return self.board.winner()
    
    def reset(self):
        self._init()


    def select(self, row, col):
        pieceSelected = False
        #recursive loop for piece selection
        if self.selected:
            #try to move piece
            result = self._move(row, col)
            #if piece cannot move to selected square
            if not result:
                self.selected = None
                #----reseting selection----
                row, col = audio.speech.get_move(self)
                self.select(row, col)
        #if no empty square is selected and it's your turn
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            self.moveset = self.copy_moveset()
            #print(self.moveset)
            return True
        return False
    
    def copy_moveset(self):
        moveset = self.valid_moves
        count = 0
        for move in moveset:
            moveset[move] = count
            count = count + 1
        return moveset
    
    def get_action(self, action):
        # Access key using element EXAMPLE
        action = 2
        for position, move in self.moveset:
                if move == action:
                    print("The position for action", action, "is", position)
                    break
            #return position as (row, col)
        return position
    


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        #if selected checker is moving to an empty square or move is just valid
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    #draws a circle where piece can move
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves ={}
        if self.turn == BLUE:
            self.turn = WHITE
        else:
            self.turn = BLUE
    
    def get_board(self):
        return self.board
    
    #returns new board after ai moves
    def ai_move(self, board):
        self.board = board
        self.change_turn()

