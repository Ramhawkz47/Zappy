import speech_recognition as sr
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()


def hear():
    print(" ")
    with mic as source:
        audio = r.listen(source)
    print(" ")
    try:
        t = r.recognize_google(audio)
    except:
        t = ""
    audio=None
    return t
r=sr.Recognizer()
mic = sr.Microphone(device_index=0)
say("  ")
