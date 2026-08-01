#First we import all the required libraries 
import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx 
import musicLibrary
import requests
import pygame
import os
import yt_dlp
import vlc
import time
import threading
import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
from gtts import gTTS
from musicPlayer import MusicPlayer

#recognizer object , it will recognize what we will talk
recognizer = sr.Recognizer()
#load the environment variable form .env
load_dotenv()
#pyttsx is initialised
engine = pyttsx3.init()
#news api 
newsapi = os.getenv("NEWS_API_KEY")

#speak function , it will take a text and make it audible(talk) 
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    print("Converting text to speech...")

    tts = gTTS(text)
    tts.save('temp.mp3')

    print("Playing audio...")

#Initialize pygame mixer 
    pygame.mixer.init()
#Load the MP3 file
    pygame.mixer.music.load('temp.mp3')
#Play the MP3 file
    pygame.mixer.music.play()
#Keep the program running while the music or bot is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.quit()

    os.remove('temp.mp3')
    print("Done.")

def play_song(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']

    player = vlc.MediaPlayer(audio_url)
    player.audio_set_volume(125)
    player.play()

    speak("Playing your song.")

    while True:
        state = player.get_state()

        if state in [vlc.State.Ended, vlc.State.Stopped, vlc.State.Error]:
            break

        time.sleep(1)

def aiProcess(command):
    client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
    print("Sending request to Gemini...")
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents= command,
        config=types.GenerateContentConfig(
        system_instruction="You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant. Give short responses"
    )
)
    print("Received response from Gemini.")
    return response.text

def processCommand(c):
    if "open google" in  c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in  c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in  c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open gmail" in  c.lower():
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    elif c.lower().startswith("play"):
        song = c.lower()[5:].strip()
        if song in musicLibrary.music:
            player.play(musicLibrary.music[song],song)
        else:
            speak("Song not found.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&language=en&apiKey={newsapi}")
        print(r.status_code)
        print(r.text)
        if r.status_code == 200:
            data = r.json()
            #Extract the articles 
            articles = data.get('articles',[])

            #Print the headlines 
            for article in articles:
                print(article["title"])
                print(len(articles))
                speak(article["title"])
    else:
        #let googleai handle the request
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":
    player = MusicPlayer()
    # threading.Thread(target=player.start,daemon=True).start()
    speak("Jarvis is booting up...")
    pass
    while True: 
        # Listen for the wakeup word "Jarvis" 
        # obtain audio from the microphone 
        r = sr.Recognizer()
        #recognize speech using sphinx 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout = 2 , phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Sir.")
            #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))