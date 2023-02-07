import speech_recognition as sr
import pyautogui


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Your Mic is Ready to use: ")
    audio = r.listen(source)
    
    