import speech_recognition as sr
import pyautogui
#import audio.automator
import re
import pygame


#control = automator.controls() #automation may no longer be needed, but I'm keeping it in for now just in case
r = sr.Recognizer()
print("\n\nThreshold Value Before calibration:" + str(r.energy_threshold)) 

pattern = re.compile(r'^[a-h][1-8]$') 
board = [['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'], #board is a 2D array of the chess board, each element is a string of the square name
         ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'], #we dont need every square, but its good to have them all in case we want to add more functionality
         ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
         ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
         ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
         ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
         ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
         ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']]

keyWords = ["up right", "up left", "down right", "down left", "cancel", "stop program"] #list of keywords to be recognized, if we want to add more keywords, we can just add them to this list

def vocal_select():
    with sr.Microphone() as source:
        while True:
            try:
                audio = r.adjust_for_ambient_noise(source)
                print("Adjusted Threshhold: " + str(r.energy_threshold))
                print("Enter a piece to select: ")
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                if transcript == "Asics" or transcript == "asics" or transcript == "86": #hardcoded similar sounding words
                    transcript = "a6" #forces the program to consider these similar sounds as the same word
                if transcript == "Before" or transcript == "before":
                    transcript = "b4"

                
            except Exception as e: #if the program cannot understand the audio, it will print the error and continue, this is good for silence
                print("Audio Could not be understood, please try again")
                continue
            
            print("Heard: " + transcript) #prints the transcript, this is mostly for us to know what the computer is hearing
                
            for row_idx, rows in enumerate(board):
                    if transcript in rows:
                        col_idx = rows.index(transcript)
                        #prints the position of the square in the board
                        print(f"{transcript} is at position ({row_idx}, {col_idx}) in the board.")
                        return row_idx, col_idx
                    else:
                        #Basically a loading message
                        print("Spoken text not found in board.")

def vocal_move():
    with sr.Microphone() as source:
        while True:
            try:
                audio = r.adjust_for_ambient_noise(source)
                #audio adjusted for ambinent noise
                print("Adjusted Threshhold: " + str(r.energy_threshold))
                print("Make a move: ")
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                
                if(transcript == "uplift"): #hardcoded similar sounding words
                    transcript = "up left"
                if(transcript == "upright"):
                    transcript = "up right"
                
                if transcript in keyWords:
                    print(f"You entered: {transcript}")
                    if transcript == "up left" or transcript == "movement 1":
                        if(transcript == "up left"):
                            print("Moving up left")
                        return 0                    
                    elif transcript == "up right" or transcript == "movement 2":
                        if(transcript == "up right"):
                            print("Moving up right")
                        return 1
                    elif transcript == "down right" or transcript == "movement 3":
                        if(transcript == "down right"):
                            print("Moving down right")
                        return 2
                    elif transcript == "down left" or transcript == "movement 4":
                        if(transcript == "down left"):
                            print("Moving down left")
                        return 3
                    elif transcript == "stop program":
                        print("Stopping program")
                        pygame.quit()
                        break
                else:
                    print("Invalid move, please try again: ")
                    
            except Exception as e:
                print("Audio could not be understood, please try again")
