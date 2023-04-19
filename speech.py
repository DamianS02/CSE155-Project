import speech_recognition as sr
import pyautogui
import automator
import re

control = automator.controls() #automation may no longer be needed, but I'm keeping it in for now just in case
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

with sr.Microphone() as source:
    while True:
        try:
            audio = r.adjust_for_ambient_noise(source)
            print("Adjusted Threshhold: " + str(r.energy_threshold))
            print("Say something: ")
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
            
        for row_idx, row in enumerate(board):
                if transcript in row:
                    col_idx = row.index(transcript)
                    print(f"{transcript} is at position ({row_idx}, {col_idx}) in the board.") #prints the position of the square in the board, this is mostly for us to know what the computer is hearing
                    print("Listening for your move: ") 
                    while True:
                        try:
                            audio = r.adjust_for_ambient_noise(source) 
                            print("Adjusted Threshhold: " + str(r.energy_threshold)) #this is to let us know that the audio has been adjusted according to the ambient noise
                            audio = r.listen(source)
                            transcript = r.recognize_google(audio).lower()
                            
                            if(transcript == "uplift"): #hardcoded similar sounding words
                                transcript = "up left"
                            if(transcript == "upright"):
                                transcript = "up right"
                            
                            if transcript in keyWords:
                                print(f"You entered: {transcript}") #From here, We need to connect the commands to the game itself
                                if transcript == "up right":
                                    print("Moving up right") #this is just a test to see if the program is working, we can replace these with the actual commands
                                    #Function calls to move the selected piece to the desired position
                                    #You can make it so that it moves the piece +1 in the x direction and +1 in the y direction
                                    #I assume that the checkers board would have something to hold position data, so you can just use that to move the piece of course.
                                    break
                                elif transcript == "up left":
                                    print("Moving up left")
                                    break
                                elif transcript == "down right":
                                    print("Moving down right")
                                    break
                                elif transcript == "down left":
                                    print("Moving down left")
                                    break
                                elif transcript == "cancel": #cancel should just cancel the chosen peice, allowing you to choose another
                                    print("Cancelling move")
                                    break
                                elif transcript == "stop program": #saying this will just end the game, maybe we can add a "are you sure?" prompt
                                    print("Stopping program")
                                    exit()
                            else:
                                print("Invalid move, please try again: ")
                                
                        except Exception as e:
                            print("Audio could not be understood, please try again")
                else:
                    print("Spoken text not found in board.") #the program spits this out a lot, but it's not a problem, can just be considered a "loading..." message its going through the words I assume
