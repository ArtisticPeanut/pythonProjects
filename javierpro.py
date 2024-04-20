from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os
import pyttsx3 as voice

import speech_recognition as sr
import keyboard
import re
import pygame
import sys
import cv2
import threading
import tkinter as tk
from tkinter import simpledialog

import datetime
import pyautogui as pg 
import time as t  
import datetime as dt

import pyperclip as clip







os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/HomePC/Downloads/cacert.pem'


pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("J.A.R.V.I.S.")

# Set up colors
white = (0, 0, 0)



##def greet():
    ##engine.say("Hello! How can I assist you today?")
    ##engine.runAndWait()

#def respond_to_greeting():
   # engine.say("I'm doing well, thank you. How about you?")
    #engine.runAndWait()
 
def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while True:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (width, height))
            pygame_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            pygame_surface = pygame.surfarray.make_surface(pygame_frame)
            screen.blit(pygame_surface, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cap.release()
                    pygame.quit()
                    sys.exit()

        # Video reached the end, rewind and continue
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cap.release()

def play_audio(audio_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

def move(query):
    t.sleep(2)

    pg.hotkey('win')

    t.sleep(0.5)
# Type "Chrome" to search for the Chrome app
    pg.typewrite('Chrome')

    t.sleep(0.5)
    pg.click(696,345)

# Wait for a moment to allow the search results to appear
    t.sleep(1)

# Press Enter to open the Chrome app


    pg.click(612,644)

    t.sleep(1)

    pg.click(1570,78)
    
    t.sleep(0.5)

    pg.typewrite("https://chat.openai.com")

    t.sleep(0.5)

    pg.press("Enter")

    t.sleep(6)

    pg.click(37,134)

    t.sleep(2)

    pg.typewrite(query)
    print(query)

    pg.press("Enter")

    t.sleep(3)
    
    selected_text=copy_text_from_selected_point(*start_point, *end_point)
    t.sleep(1)
    return selected_text






def copy_text_from_selected_point(start_x, start_y, end_x, end_y):
    # Move the mouse to the starting point
    pg.moveTo(start_x, start_y, duration=1.5)

    # Click and drag to the ending point to select the text
    pg.mouseDown()
    pg.moveTo(end_x, end_y, duration=1.5)
    pg.mouseUp()

    # Copy the selected text
    pg.hotkey('ctrl', 'c')
    selected_text = clip.paste()

    t.sleep(3)
    print(selected_text)

    return selected_text





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



TIME=dt.datetime.now()

current_time = TIME.strftime("%H%M")

print(current_time)

## setting the voice engine
engine = voice.init()
engine.setProperty('rate', 150) 
 # Speed of speech
engine.setProperty('volume', 0.9)

recognizer = sr.Recognizer()


def greet_based_on_time():
    # Get the current time
    current_time = datetime.datetime.now().time()

    # Extract the hour from the current time
    current_hour = current_time.hour

    # Greet based on the time of day
    if 5 <= current_hour < 12:
        print("Good morning! ☀️")
        engine.say("Good Morning Boss!")
    elif 12 <= current_hour < 18:
        engine.say("Good afternoon Boss! ")
    else:
        print("Good evening! 🌙")
        engine.say("Good Evening Boss!")

# Call the function to greet based on the time

            

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
    if "Billy" in query:
        greet_based_on_time()
        



    engine.say(f"Nice to Meet you  {query}")
    engine.runAndWait()

    engine.say(" How can I help you ? ")
    engine.runAndWait()

    main()
    
    
def process_request(command):
    # Define patterns for different ways users might request to play a song
    play_patterns = [
        r"play\s+me\s+(?:the\s+)?song\s+(?P<song_name>.+)",
        r"play\s+(?P<song_name>.+)\s+song",
        r"play\s+(?P<song_name>.+)",
        r"play\s+song\s+(?P<song_name>.+)",
    ]
    

    # Try to match the command with each pattern
    for pattern in play_patterns:
        match = re.search(pattern, command, re.IGNORECASE)
        if match:
            song_name = match.group("song_name")
            return song_name.strip()

    # If no match is found, return None
    return None


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

def whatElse():
    engine.say("How else Can I help you")
    engine.runAndWait()


def check_input():
    user_input = simpledialog.askinteger("Awaiting User Input", "Declare the squence:")

    if user_input is not None and user_input == 1:
    
        print("Welcome :)")
        engine.say("Normal sequence initiated, what is your name ?")
        engine.runAndWait()
        normal()
    else:
        
        engine.say("Sequence initiated")
        engine.runAndWait()
        main()  

            
def main():
    
   
    
    
    while True:
        command = listen()

        if "time" in command:
            current_time = TIME.strftime("%H %M")

            
            engine.say(f"The current time is {current_time}")
            engine.runAndWait()
            print(current_time)
            whatElse()
        
        elif "have a question" in command:
            engine.say(f"What is your question ?")
            engine.runAndWait()
            query =listen()
            print(query)

            t.sleep(1)


            
        

            print(query)
           
            if query:
                 answer=move(query)
                 
                 engine.say(answer)
                 engine.runAndWait()
                 listen()

            else:
                 print("No response found.")
                 engine.say("sorry! I have no answer")
                 engine.runAndWait()
        elif "check if i have a class" in command:
            import timetable as timetable
            timetable.alert_me
            print(timetable.alert_me)
            engine.say(timetable.alert_me) 
            engine.runAndWait()
        elif "read me today's classes" in command:
            import timetable as timetable
            timetable.today_classes_message
            print(timetable.today_classes_message)
            engine.say(timetable.today_classes_message) 
            engine.runAndWait()


        elif  "play" in command:
            newcommand =process_request(command)
            import song 
            song.play_song(newcommand)
        elif "wake up" in command:
            engine.say("Initialising begin sequence")
            engine.runAndWait()
            main()

        
            


        elif "exit" in command:
            engine.say("Good bye!")
            engine.runAndWait()
            break

        elif "let's chat" in command:
           import chek
           engine.say("Sure thing! I'm listening!")
           engine.runAndWait()
           while True:
               command = listen()

               if  "stop chat" in command:
                   engine.say("Stopping chat.")
                   engine.runAndWait()
                   break
               elif  "command" in command:
                   main()
               print(command)
               response = chek.main(command)
               engine.say(response)
               engine.runAndWait()




video_path = "C:/Users/HomePC/Desktop/python tutorials/system_project.mp4"  # Replace with the path to your video file
audio_path = "C:/Users/HomePC/Desktop/python tutorials/systemaudio.mp3"  # Replace with the path to your audio file

video_thread = threading.Thread(target=play_video, args=(video_path,))
audio_thread = threading.Thread(target=play_audio, args=(audio_path,))

video_thread.start()
audio_thread.start()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

        # Draw UI elements here (you can use pygame.draw, pygame.font, etc.)

    pygame.display.flip()


start_point = (780, 772)
end_point = (1026, 936)

engine.say("Hello, my name is JAVIER , AN Intelligent A I , press 1  for normal sequence and any other to skip normal sequence")

engine.runAndWait()

root = tk.Tk()


# Create and pack the widget
check_button = tk.Button(root, text="Declare sequence", command=check_input)
check_button.pack(pady=10)

# Run the main loop
root.mainloop()