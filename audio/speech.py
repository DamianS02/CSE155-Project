import speech_recognition as sr

def get_move(game):
    r = sr.Recognizer()
    # set sample rate to 48000 for faster audio processing
    mic = sr.Microphone(device_index=0, sample_rate=48000)
    # reducing chunk size for faster audio processing
    mic.CHUNK = 512
    with mic as source:
        while True:
            game.update()
            try:
                audio = r.adjust_for_ambient_noise(source)
                # print("Adjusted Threshhold: " + str(r.energy_threshold))
                print("Say the name of the square you want to select (e.g. a1):")
                audio = r.listen(source)
                transcript = r.recognize_google(audio).lower()
                #hardcoded similar sounding words
                # if transcript == "Asics" or transcript == "asics" or transcript == "86":
                #     transcript = "a6"
                # if transcript == "Before" or transcript == "before":
                #     transcript = "b4"
                transcript = transcript[0:2]
                if len(transcript) == 2 and transcript[0] in "abcdefgh" and transcript[1] in "12345678":
                    row = int(transcript[1]) - 1
                    col = ord(transcript[0]) - ord('a')
                    return row, col
            except:
                print("Could not understand audio. Please try again.")
