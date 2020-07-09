import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

print("Hi im Zappy im here to chat with you!")
say("Hi im Zappy im here to chat with you!")
say("  ")
print("come on lets chat!")
say("come on lets chat!")
t=""
while(t!="bye"):
    t = input("Speak: ")
    print("Zappy: "+t)
    say(text=t)
