import speech_recognition as sr
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer()
mic = sr.Microphone(device_index=0)

print("Hi im Zappy im here to chat with you!")
say("Hi im Zappy im here to chat with you!")
say("  ")
print("come on lets chat!")
say("come on lets chat!")
t=""
while(t!="bye"):
    print("speak:-")
    with mic as source:
        audio = r.listen(source)
    print("done")
    try:
        t=r.recognize_google(audio)
        audio=None
    except:
        t="i didn't understand that"
        audio=None
    print("Zappy: "+t)
    say(text=t)
