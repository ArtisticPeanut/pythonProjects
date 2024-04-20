from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os
import pyttsx3

os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/HomePC/Downloads/cacert.pem'

def google_search(query, max_words=70):
    search_results = list(search(query, num=1, stop=1, pause=2))

    if not search_results:
        return None

    first_result_url = search_results[0]

    try:
        page = requests.get(first_result_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        paragraphs = soup.find_all('p')

        response = ""
        word_count = 0

        for paragraph in paragraphs:
            words = paragraph.text.split()
            if word_count + len(words) <= max_words:
                response += paragraph.text + "\n"
                word_count += len(words)
            else:
                break

        return response

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")
        return None

if __name__ == "__main__":
    user_question = "Elon Musk?"
    answer = google_search(user_question)

    if answer:
        print("\nGoogle's Response:")
        print(answer)
        # Additional code for text-to-speech or other actions
    else:
        print("No response found.")
