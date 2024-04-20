import vlc
import pygame
import threading
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os
import pyttsx3 as voice
import datetime as t
import speech_recognition as sr
import keyboard
import time as sleep  

os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/HomePC/Downloads/cacert.pem'

def google_search(query):
    search_results = list(search(query, num=1, stop=1, pause=2))

    if not search_results:
        return None

    first_result_url = search_results[0]

    try:
        page = requests.get(first_result_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        paragraphs = soup.find_all('p')

        response = ""
        for paragraph in paragraphs:
            response += paragraph.text + "\n"
        answers = str(response) 
        words = answers.split()

        # Extract the first 70 words
        first_70_words = ' '.join(words[:70])   

        return first_70_words

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")
        return None

TIME = t.datetime.now()

current_time = TIME.strftime("%H%M")

print(current_time)

# Setting the voice engine
engine = voice.init()
engine.setProperty('rate', 150) 
engine.setProperty('volume', 0.9)

recognizer = sr.Recognizer()

def normal():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
       
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    print(query)

    if "my name is" in str(query):
        name_index = query.index("my name is") + len("my name is")
        name = query[name_index:].strip()
        query =  name
    if "Te" in query:
        query = "Tecla"
        engine.say(f"Billy tells me you are very beautiful {query}")
        engine.runAndWait()

    engine.say(f"Nice to Meet you  {query}")
    engine.runAndWait()

    engine.say(" How can I help you ? ")
    engine.runAndWait()

    main()

def check_enter_key():
    print("Press Enter key...")

    while True:
        if keyboard.is_pressed('enter'):
            print("Enter key has been clicked!")
        else:
            engine.say("Sequence initiated")
            engine.runAndWait()
            main()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def play_video(video_path):
    instance = vlc.Instance('--no-xlib')  
    player = instance.media_player_new()
    media = instance.media_new(video_path)
    media.get_mrl()
    player.set_media(media)

    player.set_fullscreen(True)
    player.play()

    while True:
        pass

def play_audio(audio_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    while True:
        command = listen()

        if "time" in command:
            current_time = TIME.strftime("%H %M")
            engine.say(f"The current time is {current_time}")
            engine.runAndWait()
            print(current_time)
        
        elif "have a question" in command:
            engine.say(f"What is your question ?")
            engine.runAndWait()
            query = listen()

            print(query)
            answer = google_search(query)
            if answer:
                print("\nGoogle's Response:")
                print(answer)
                engine.say(answer)
                engine.runAndWait()
                listen()
            else:
                print("No response found.")
                engine.say("Sorry! I have no answer")
                engine.runAndWait()
                 
        elif "exit" in command:
            engine.say("Goodbye!")
            engine.runAndWait()
            break

if __name__ == "__main__":
    video_path = 'C:/Users/HomePC/Desktop/python tutorials/system_project.mp4'
    audio_path = 'C:/Users/HomePC/Desktop/python tutorials/systemaudio.mp3'

    # Start a thread to play video
    video_thread = threading.Thread(target=play_video, args=(video_path,))
    video_thread.start()

    # Play audio in the main thread
    play_audio(audio_path)

    engine.say("Hello, my name is JAVIER, AN Intelligent A I, press 1 for the normal sequence and any other key to skip the normal sequence")
    engine.runAndWait()

    user_input = input("Awaiting User Input : ")
    number = int(user_input)

    if number == 1:
        print("Welcome :)")
        engine.say("Normal sequence initiated. What is your name?")
        engine.runAndWait()
        normal()
    else:
        engine.say("Sequence initiated")
        engine.runAndWait()
        main()
