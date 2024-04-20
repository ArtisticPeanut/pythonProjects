import pyttsx3
import pywhatkit
import speech_recognition as sr
import re
engine = pyttsx3.init()
engine.setProperty('rate', 150) 
 # Speed of speech
engine.setProperty('volume', 0.9)

def text_to_speech(text):
    
   
    # Convert text to speech
    
    engine.say(text)
    engine.runAndWait()


def play_song(song_name):
    # Convert text to speech
    engine = pyttsx3.init()
    engine.say(f"Playing {song_name} on YouTube.")
    engine.runAndWait()

    # Play the song on YouTube
 
 
    pywhatkit.playonyt(song_name + " lyrics")


def get_song_name():
    # Use speech recognition to get the song name
    recognizer = sr.Recognizer()
   
    with sr.Microphone() as source:
        text_to_speech("Please say the name of the song.")
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=3)
        

    try:
        song_name = recognizer.recognize_google(audio)
        return song_name
    except sr.UnknownValueError:
        text_to_speech("Sorry, I couldn't understand the song name. Please type it instead.")
        return input("Enter the name of the song: ")





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

def CommandPlay():
    # Example usage
    user_command = get_song_name()

    song_name = process_request(user_command)
    if song_name:
        print(f"User wants to play the song: {song_name}")
        play_song(song_name)
        
        # Call your play_song function with the extracted song_name
    else:
        print("Sorry, I couldn't understand the command.")

