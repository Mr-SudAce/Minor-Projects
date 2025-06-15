import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
def entrytospeak(text):
    engine.say(text)
    engine.runAndWait()
    



