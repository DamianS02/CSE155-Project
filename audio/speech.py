import speech_recognition as sr
import pygame
import sys


def get_move(game):
    r = sr.Recognizer()
    # set sample rate to 48000 and chunk size to 512 for faster audio processing
    mic = sr.Microphone(device_index=0, sample_rate=48000, chunk_size=512)
    with mic as source:
        r.adjust_for_ambient_noise(source)
    while True:
        game.update()
        try:
            with sr.Microphone(device_index=0, sample_rate=48000, chunk_size=512) as source:
                audio = r.listen(source, timeout=5)
            transcript = r.recognize_google(audio).lower()
            if transcript == "quit":
                pygame.quit()
                sys.exit()
            transcript = transcript[0:2]
            if len(transcript) == 2 and transcript[0] in "abcdefgh" and transcript[1] in "12345678":
                row = int(transcript[1]) - 1
                col = ord(transcript[0]) - ord('a')
                print("Row: ", row, " Column: ", col)
                return row, col
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}") 
        except sr.WaitTimeoutError:
            print("No audio input received. Please try again.")

