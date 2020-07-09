import speech_recognition as sr

r=sr.Recognizer()
mic = sr.Microphone(device_index=0)
print("speak:")
with mic as source:
    audio = r.listen(source)
print("done")
print(r.recognize_google(audio))
