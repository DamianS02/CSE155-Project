import pyautogui
import speech_recognition as sr
fast = 100
slow = 10

# Speech recognition controls
class controls:
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        
    def leftClick(self):
        print("Left Click Heard: ")
        pyautogui.click()
        
    def rightClick(self):
        print("Right Click Heard: ")
        pyautogui.click(button='right')
        
    def doubleClick(self):
        print("Double Click Heard: ")
        pyautogui.doubleClick()
        
    def middleClick(self):
        print("Middle Click Heard: ")
        pyautogui.click(button='middle')
        
    def scrollUp(self, r, source):
        while True:
            # Performing scroll up controls
            transcript = ""
            pyautogui.scroll(400)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
            
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
        
    def scrollDown(self, r, source):
        while True:
            # Performing scroll down controls
            transcript = ""
            pyautogui.scroll(-600)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
            
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
    # Mouse movement (up, down, left, right, up-left, up-right, down-left, down-right)
    def moveUp(self, r, source):
        while True:
            transcript = ""
            pyautogui.moveRel(0, -1 * slow, duration=0.25)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
                
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
            
            elif transcript == "faster" or transcript == "quicker" or transcript == "speed up" or transcript == "go faster":
                pyautogui.moveRel(0, -1 * fast, duration = 0.25)
                
            elif transcript == "slower" or transcript == "go slower" or transcript == "slow down":
                pyautogui.moveRel(0, -1 * slow, duration = 0.25)
                
    def moveDown(self, r, source):
        while True:
            transcript = ""
            pyautogui.moveRel(0, slow, duration=0.25)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
                
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
            
            elif transcript == "faster" or transcript == "quicker" or transcript == "speed up" or transcript == "go faster":
                pyautogui.moveRel(0, fast, duration = 0.25)
                
            elif transcript == "slower" or transcript == "go slower" or transcript == "slow down":
                pyautogui.moveRel(0, slow, duration = 0.25)
                
    def moveLeft(self, r, source):
        while True:
            transcript = ""
            pyautogui.moveRel(-1 * slow, 0, duration=0.25)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
                
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
            
            elif transcript == "faster" or transcript == "quicker" or transcript == "speed up" or transcript == "go faster":
                pyautogui.moveRel(-1 * fast, 0, duration = 0.25)
                
            elif transcript == "slower" or transcript == "go slower" or transcript == "slow down":
                pyautogui.moveRel(-1 * slow, 0, duration = 0.25)
                
    def moveRight(self, r, source):
        while True:
            transcript = ""
            pyautogui.moveRel(slow, 0, duration=0.25)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
                
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
            
            elif transcript == "faster" or transcript == "quicker" or transcript == "speed up" or transcript == "go faster":
                pyautogui.moveRel(fast, 0, duration = 0.25)
                
            elif transcript == "slower" or transcript == "go slower" or transcript == "slow down":
                pyautogui.moveRel(slow, 0, duration = 0.25)
                
    def moveUpLeft(self, r, source):
        while True:
            transcript = ""
            pyautogui.moveRel(-1 * slow, -1 * slow, duration=0.25)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
                
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
            
            elif transcript == "faster" or transcript == "quicker" or transcript == "speed up" or transcript == "go faster":
                pyautogui.moveRel(-1 * fast, -1 * fast, duration = 0.25)
                
            elif transcript == "slower" or transcript == "go slower" or transcript == "slow down":
                pyautogui.moveRel(-1 * slow, -1 * slow, duration = 0.25)
                
    def moveUpRight(self, r, source):
        while True:
            transcript = ""
            pyautogui.moveRel(slow, -1 * slow, duration=0.25)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
                
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
            
            elif transcript == "faster" or transcript == "quicker" or transcript == "speed up" or transcript == "go faster":
                pyautogui.moveRel(fast, -1 * fast, duration = 0.25)
                
            elif transcript == "slower" or transcript == "go slower" or transcript == "slow down":
                pyautogui.moveRel(slow, -1 * slow, duration = 0.25)
                
    def moveDownLeft(self, r, source):
        while True:
            transcript = ""
            pyautogui.moveRel(-1 * slow, slow, duration=0.25)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
                
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
            
            elif transcript == "faster" or transcript == "quicker" or transcript == "speed up" or transcript == "go faster":
                pyautogui.moveRel(-1 * fast, fast, duration = 0.25)
                
            elif transcript == "slower" or transcript == "go slower" or transcript == "slow down":
                pyautogui.moveRel(-1 * slow, slow, duration = 0.25)
                
    def moveDownRight(self, r, source):
        while True:
            transcript = ""
            pyautogui.moveRel(slow, slow, duration=0.25)
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                print("I heard: " + transcript)
                
            except sr.UnknownValueError:
                print("I could not understand audio")
                pass
            
            if transcript == "stop":
                break
            
            elif transcript == "faster" or transcript == "quicker" or transcript == "speed up" or transcript == "go faster":
                pyautogui.moveRel(fast, fast, duration = 0.25)
                
            elif transcript == "slower" or transcript == "go slower" or transcript == "slow down":
                pyautogui.moveRel(slow, slow, duration = 0.25)