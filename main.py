
import sys
import speech_recognition as sr 
import datetime
import pyttsx3 as pytt
import requests
import subprocess
import json
import random
import operator
import os
import time
import pyjokes
import shutil
import smtplib
import ctypes
import wikipedia
import tkinter
import webbrowser
import Bea



engine = pytt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Bonjour CONDOR !")
    elif hour >= 12 and hour < 18 :
        speak("Bonsoir CONDOR")
    else:
        speak("Bonsoir CONDOR")

    assname = ("Condor Vocal")
    speak("Je suis votre assistant")
    speak(assname)

def username():
    speak("What Should i call your sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizing")
        query = r.recognize_google(audio, language="fr-FR")
        print(f"User said: {query}\n")
    except Exception as ex:
        print(ex)
        print("Unable to recognize your voice")
        return None
    return query


WishMe()

