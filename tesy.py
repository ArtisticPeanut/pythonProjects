from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os

os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/HomePC/Downloads/cacert.pem'

def google_search(query):
    search_results = list(search(query, num=1, stop=1, pause=2))

    if not search_results:
        return None

    first_result_url = search_results[0]

    try:
        page = requests.get(first_result_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        paragraphs = soup.find_all('p')

        response = ""
        for paragraph in paragraphs:
            response += paragraph.text + "\n"

        return response

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")
        return None

# Example usage:
user_question = "Who is Elon Musk?"
answer = google_search(user_question)

if answer:
    print("\nGoogle's Response:")
    print(answer)
else:
    print("No response found.")
