import json
from chatbot_library import ChatBot

# Install necessary packages
# pip install some_library

# Load dataset from Yahoo Answers
with open('nfl6.json', 'r') as file:
    data = json.load(file)

# Extract questions and answers
questions = [entry['question'] for entry in data[:1000]]
answers = [entry['answer'] for entry in data[:1000]]

# Train the chatbot
chatbot = ChatBot()
for question, answer in zip(questions, answers):
    chatbot.train(question, answer)

# Ask some questions
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
