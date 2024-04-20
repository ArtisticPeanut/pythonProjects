import os 
import pyautogui as pg 
import time as t 
import speech_recognition as sr 
import pyttsx3
import csv
import re

def find_contact(name, contacts_file):
    with open(contacts_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if name.lower() in row[0].lower():
                return row[0]
    return None

def text(person, message):
    contacts_file = 'contacts.csv'
    
    found_person = find_contact(person, contacts_file)

    if found_person:
        print(f"Contact found: {found_person}")
        # Your messaging code here
        print(f"Message sent successfully to {found_person}")
    else:
        print(f"Contact with name pattern '{person}' not found in contacts.csv")

def voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Processing voice command...")
        command = recognizer.recognize_google(audio).lower()
        print(f"Voice command: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

def main():
    while True:
        command = voice_command()
        gender = {'him', 'her'}
        if command and 'text' in command and any(g in command for g in gender):
            # Extracting person and message from the command using regular expression
            parts = re.split(r'\s*(?:and tell|tell|and ask|ask)\s*', command, flags=re.IGNORECASE)
            
            if len(parts) >= 2:
                person, message = parts[0].strip(), parts[1].strip()
                
                for g in gender:
                    if g in message:
                        message = message.replace(g, '').strip()
                        break

                print(f"Person: {person}")
                print(f"Message: {message}")
                
                text(person, message)
            else:
                print("Invalid voice command format. Please say 'text [person] and tell [message]'.")
        else:
            print("Invalid voice command format. Please say 'text [person] and tell [message]'.")

if __name__ == "__main__":
    main()
