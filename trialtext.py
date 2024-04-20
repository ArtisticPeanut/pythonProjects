import os 
import pyautogui as pg 
import time as t 
import speech_recognition as sr 
import pyttsx3
import csv

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
        pg.hotkey('win')
        t.sleep(0.5)
        pg.typewrite('whatsapp')
        t.sleep(1)
        pg.click(696, 345)
        t.sleep(3)
        pg.click(367, 150)
        t.sleep(0.3)
        pg.typewrite(found_person)
        t.sleep(1)
        pg.doubleClick(265, 238)
        t.sleep(1)
        pg.doubleClick(940, 1058)
        pg.typewrite(message)
        pg.hotkey("enter")
        print("Message sent successfully")
    else:
        print(f"Contact with name pattern '{person}' not found in contacts.csv")

person = input("Enter name: ")
message = input("Enter message: ")

text(person, message)
