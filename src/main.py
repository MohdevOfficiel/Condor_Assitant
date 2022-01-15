import os
import  pyjokes
import winshell
import win32com.client as wincl
import sys
import wolframalpha
import wikipedia
import speech_recognition as sr
import datetime
import pyttsx3
import requests
import subprocess
import webbrowser
import json
import random
import operator
import shutil
import smtplib
import time

from twilio.rest import Client
from urllib.request import urlopen



engine = pyttsx3.init()
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
    columns = shutil.get_terminal_size().columns

    print("######################".center(columns))
    print("Welcome Mr.", uname.center(columns))

    speak("How can i Help you, Sir")

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    #Enable low security in gmail
    server.login('mohdevconde@gmail.com', 'Papaconde620')
    server.sendmail('mohdevconde@gmail.com', to, content)
    server.close()



if __name__== '__main__':
    clear = lambda: os.system('cls')

    #This Function will clean any
    #command before execution of this python file
    clear()
    WishMe()
    username()

    while True:

        query = takeCommand().lower()

        #All the commands said by user will be
        #stored here in 'query' and will be
        #converted to lower case for easily
        #recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(result)
        elif 'open youtube' in query :
            speak("Here you go to Youtube\n")
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            speak("Here you go to stack Over Flow.Happy coding")
            webbrowser.open("stackoverflow.com")
        elif 'play music ' in query or 'play song' in query :
            speak("Here you go with music")
            music_dir = "C:\\Users\\USER HP\\Music\download"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, song[1]))
        elif 'the time' in query:
            srTime = datetime.datetime.now().strftime("%H:M M:% S")
            speak(f"Monsieur, the time is {srTime}")
        elif 'email to gaurav ' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as ex:
                print(ex)
                speak("I am no able to send this email")

        elif 'send a mail' in query: 
            try:
                speak("What should i say ?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as ex:
                print(ex)
                speak("I am not able to send this email")

        elif 'how are you ' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fin' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "change my name to " in query :
            query = query.repalce("change my name to", "")
            assname = query
        elif "change name" in query:
            speak("What whould you like to call me, Sir")
            assname = takeCommand()
            speak("Thank for naming me")
        elif "what's your name" in query or "What is your name" in query:
            speak("My Friends call me")
            speak("assname")
            print("My friends call me", assname)
        elif 'exit' in query:
            speak("Thank for giving me your time")
            exit()
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif "calculate" in query:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res =  client.query(''.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            print("The answer is " + answer)

        elif 'search'  in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replaace("play", "")
            webbrowser.open(query)
        elif 'who i am 'in query :
            speak('If you talk then definitely human')
        
           



