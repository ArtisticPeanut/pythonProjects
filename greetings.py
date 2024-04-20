import random
from datetime import datetime

def get_time_greeting():
    current_time = datetime.now().time()
    hour = current_time.hour

    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 17:
        return "Good afternoon!"
    elif 17 <= hour < 21:
        return "Good evening!"
    else:
        return "Good night!"

def generate_random_greeting():
    greetings = [
        "Hello there!",
        "Hi!",
        "Greetings!",
        "Hey!",
        "Howdy!",
        "Salutations!",
        "Hola!",
        "Bonjour!",
        "Ciao!",
        "Namaste!",
        "What's up?",
        "Yo!",
        "Hi there!",
        "How's it going?",
        "Nice to meet you!",
        "Hello, friend!",
        "Hey, buddy!",
        "Hiya!",
        "Top of the morning to you!",
        "Good day!",
        "Hi, neighbor!",
        "Hey, you!",
        "Hello, sunshine!",
        "Hi, pal!",
        "Greetings and salutations!",
        "Hey there, sport!",
        "Sup?",
        "Good to see you!",
        "Hi, everyone!",
        "Hey, handsome/beautiful!",
        "Hello, world!",
        "Hi, lovely people!",
        "Hey, rockstar!",
        "Greetings, Earthling!",
        "Hola amigo!",
        "Hi-de-ho!",
        "Hey, champ!",
        "What's cracking?",
        "Howdy-do!",
        "Greetings, comrade!",
        "Hey, party people!",
        "Hi, sunshine!",
        "Hey, good looking!",
        "How's life treating you?",
        "Hello, gorgeous!",
        "Hi, genius!",
        "Hey, smarty pants!",
        "What's cookin'?",
        "How's the day treating you?",
        "Hi, sweetie!",
        "Hey, cutie!",
        "Greetings, citizen!",
        "What's the word?",
        "Howdy, partner!",
        "Hey, sparkler!",
        "Hi, treasure!",
        "Salut!",
        "Hola, amigo!",
        "Greetings, traveler!",
        "Hey, whiz kid!",
        "Hi, bestie!",
        "How's your day?",
        "Hey, sunshine!",
        "Greetings, amigo!",
        "Hey, smarty!",
        "Hi, superstar!",
        "What's happening?",
        "Howdy, friend!",
        "Hey, adventurer!",
        "Hi, sweetheart!",
        "Greetings, explorer!",
        "Hey, trendsetter!",
        "Hi, chatterbox!",
        "How's everything?",
        "Hey, explorer!",
        "Hi, dreamer!",
        "What's new?",
        "Hey, magician!",
        "Hi, artist!",
        "How's life?",
        "Hey, guru!",
        "Hi, captain!",
        "What's the buzz?",
        "How's the weather?",
        "Hey, hero!",
        "Hi, genius!",
        "What's the plan?",
        "How's your mood?",
        "Hey, winner!",
        "Hi, charmer!",
        "What's the news?",
        "How's your vibe?",
        "Hey, creator!",
        "Hi, legend!",
        "What's the deal?",
        "How's your energy?",
        "Hey, maestro!",
        "Hi, mastermind!",
        "What's the story?"]

    time_greeting = get_time_greeting()
    random_greeting = random.choice(greetings)
    return f"{random_greeting} {time_greeting}"

if __name__ == "__main__":
    random_greeting = generate_random_greeting()
    print(random_greeting)
