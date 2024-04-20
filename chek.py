import re
import random
from ted import chatbot  # Assuming ted is in the same directory as check.py

def load_offensive_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().splitlines()
    return content

def return_offensive_word(offensive_words):
    return random.choice(offensive_words)
def check_for_offensive(input_text, offensive_words):
    user_words = input_text.lower().replace(" ", "")  # Remove spaces from user input

    for word in offensive_words:
        if f" {word} " in f" {user_words} ":  # Add spaces around words
            print("present")
            print(word)
            return True

    print("Absent")
    return False

           
   

def main(user_input):
    file_path = "offensive.txt"  # Update with the correct path to your file
    offensive_words = load_offensive_words(file_path)

    if check_for_offensive(user_input, offensive_words) == True:
        offensive_word = return_offensive_word(offensive_words)
        response =  offensive_word
        print(response)
        return response,True
    else:
        print("No offensive words found. Proceed with the input.")
        response = chatbot(user_input)
        print(response)
        if response:
            return response
        else:
            new_quote = "I have learnt a new word"
        return new_quote,response


