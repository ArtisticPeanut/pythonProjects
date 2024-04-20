import vlc
import pygame
import threading
import speech_recognition as sr
import pyttsx3

# Function to play video in full-screen mode
def play_video(video_path):
    instance = vlc.Instance('--no-xlib')  # Use --no-xlib to avoid conflicts with pygame
    player = instance.media_player_new()
    media = instance.media_new(video_path)
    media.get_mrl()
    player.set_media(media)

    player.set_fullscreen(True)
    player.play()

    while True:
        pass

# Function to play audio
def play_audio(audio_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Function for the virtual assistant
def virtual_assistant():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    while True:
        with sr.Microphone() as source:
            print("Listening for a command...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "hello" in command:
                engine.say("Hi!")
                engine.runAndWait()

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Main function
def main():
    # Replace 'path/to/your/video.mp4' and 'path/to/your/audio.mp3' with the actual paths
    video_path = 'C:/Users/HomePC/Desktop/python tutorials/system_project.mp4'
    audio_path = 'C:/Users/HomePC/Desktop/python tutorials/systemaudio.mp3'

    # Start a thread to play videochat.openai.com
    
    video_thread = threading.Thread(target=play_video, args=(video_path,))
    video_thread.start()

    # Start a thread for the virtual assistant
    assistant_thread = threading.Thread(target=virtual_assistant)
    assistant_thread.start()

    # Play audio in the main thread
    play_audio(audio_path)

if __name__ == "__main__":
    main()
