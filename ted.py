import json
from difflib import get_close_matches
import random as r 
 

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list) -> str:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str:
    if question in knowledge_base['questions']:
        return knowledge_base['questions'][question]
    return None

def chatbot(user_input):
    knowledge_base_path = 'knowledge_base.json'
    knowledge_base = load_knowledge_base(knowledge_base_path)

    while True:
        if user_input.lower() == 'quit':
            break

        

        best_match = find_best_match(user_input, knowledge_base['questions'])
        
        if best_match :
            answer = get_answer_for_question(best_match, knowledge_base)
            return(f'Bot: {answer}  ')
            
        else:
            print("Bot: I don't know the answer. Can you teach me?")

            new_answer = input('You: Type the answer or type "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base['questions'][user_input] = new_answer
                save_knowledge_base(knowledge_base_path, knowledge_base)
                print('Bot: Thank you! I learned a new response.')
                return new_answer





    
