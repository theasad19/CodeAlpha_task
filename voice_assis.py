import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import os
import shutil
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir !") 
    else:
        speak("Good Evening Sir !") 
    assis_name=("enola")
    speak("I am your Assistant")
    speak(assis_name)
def user_name():
     speak("What should i call you sir")
     myname=takeCommand()
     speak("Welcome Mister")
     speak(myname)
     columns = shutil.get_terminal_size().columns
     print("Welcome Mr.", myname.center(columns))
     speak("How can i Help you, Sir")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...") 
       r.pause_threshold = 1
       r.adjust_for_ambient_noise(source)
       try:
           audio=r.listen(source,timeout=6)
           print("Recognizing...")
           query=r.recognize_google(audio, language='en-GB')
           print(f"User said: {query}")
           return query
       except sr.UnknownValueError:
           print("Google Speech Recognition could not understand the audio")
           return "None"
       except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"
       except Exception as e:
            print(f"Error occurred: {e}")
            return "None"
    clear()
wishme()
user_name()
while True:
     query = takeCommand().lower()
     if 'open youtube' in query: 
         speak("Here you go to Youtube\n")
         webbrowser.open("youtube.com")
     elif 'open instagram' in query: 
           speak("Here you go to instagram\n")
           webbrowser.open("instagram.com")
     elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
     elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
     elif "open wikipedia" in query:
            webbrowser.open("wikipedia.com")
     elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
     elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
     elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()




           




