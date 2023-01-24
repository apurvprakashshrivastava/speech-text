import speech_recognition as sr
import pyaudio
r=sr.Recognizer()

with sr.Microphone() as source:
    print("Start Speaking: ")
    audio=r.listen(source)

try:
    text=r.recognize_google(audio)
    print("Converted :- {}".format(text))
except:
    print("Time-Out, Retry Again! ")
