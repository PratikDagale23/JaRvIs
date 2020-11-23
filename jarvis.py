import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty ("voice")
print(voices[2])
engine.setProperty('voice', voices[2])

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!") 
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")   

    speak("I am Jarvis, Sir. Please tell me  How Can I help you?")     

def takeCommand():
    #It takes mircophone input from the user and returns steing output

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
   

if __name__ == "__main__" :
    wishMe()
    while True :
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query =  query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query :
            webbrowser.open("youtube.com")
        
        elif 'open Google' in query :
            webbrowser.open("google.com")
            
        elif 'play music' in query :
            music_dir = 'E:\\Backup Songs\\Downloads'
            songs = os.listdir (music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs.randint[0, 163]))

        elif 'open player' in query :
            vlcPlayer = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcPlayer)

        elif 'shutdown'  in query :
            os.system("shutdown /s")