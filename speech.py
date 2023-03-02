import speech_recognition as sr
import pyautogui
import automator

control = automator.controls()
r = sr.Recognizer()
print("\n\nThreshold Value Before calibration:" + str(r.energy_threshold))

with sr.Microphone() as source:
    while True:
        try:
            audio = r.adjust_for_ambient_noise(source)
            print("Adjusted Threshhold: " + str(r.energy_threshold))
            print("Say something: ")
            audio = r.listen(source)
            transcript = r.recognize_google(audio).lower()
            
        except Exception as e:
            print("Audio Could not be understood, please try again")
            continue
        
        print("Heard: " + transcript)
    
        if transcript == "quit app" or transcript == "exit app":
            break
        
        if transcript == "left click" or transcript == "click":
            control.leftClick()
            
        if transcript == "right click":
            control.rightClick()
            
        if transcript == "double click":
            control.doubleClick()
            
        if transcript == "middle click":
            control.middleClick()
            
        if transcript == "scroll up":
            control.scrollUp(r, source)
        
        if transcrilpt == "scroll down":
            control.scrollDown(r, source)
            
        if transcript == "move up" or transcript == "mouse up" or transcript == "up" or transcript == "up mouse" or transcript == "cursor up":
            control.moveUp(r, source)
            
        if transcript == "move down" or transcript == "mouse down" or transcript == "down" or transcript == "down mouse" or transcript == "cursor down":
            control.moveDown(r, source)
            
        if transcript == "move left" or transcript == "mouse left" or transcript == "left" or transcript == "left mouse" or transcript == "cursor left":
            control.moveLeft(r, source)
            
        if transcript == "move right" or transcript == "mouse right" or transcript == "right" or transcript == "right mouse" or transcript == "cursor right":
            control.moveRight(r, source)
            
        if transcript == "move to top left" or transcript == "mouse to top left" or transcript == "top left" or transcript == "top left mouse" or transcript == "cursor to top left":
            control.moveUpLeft()
            
        if transcript == "move to top right" or transcript == "mouse to top right" or transcript == "top right" or transcript == "top right mouse" or transcript == "cursor to top right":
            control.moveUpRight()
            
        if transcript == "move to bottom left" or transcript == "mouse to bottom left" or transcript == "bottom left" or transcript == "bottom left mouse" or transcript == "cursor to bottom left":
            control.moveDownLeft()
            
        if transcript == "move to bottom right" or transcript == "mouse to bottom right" or transcript == "bottom right" or transcript == "bottom right mouse" or transcript == "cursor to bottom right":
            control.moveDownRight()
            
        
        
        