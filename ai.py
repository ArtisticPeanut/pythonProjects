import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio

def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

def set_jarvis_voice(engine):
    # Set voice properties to make it sound like J.A.R.V.I.S.
    voices = engine.getProperty('voices')
    for voice in voices:
        if "jarvis" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

def speak(text):
    engine = pyttsx3.init()
    set_jarvis_voice(engine)
    engine.say(text)
    engine.runAndWait()

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

def main():
    speak("Hello! How can I help you?")
    
    while True:
        command = listen()

        if "time" in command:
            current_time = get_current_time()
            speak(f"The current time is {current_time}")

        elif "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
C:/Users/HomePC/Desktop/python tutorials/system_project.mp4