import requests
from bs4 import BeautifulSoup

def copy_text_from_webpage(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse the HTML content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html5lib')

        # Extract text content
        text_content = soup.get_text()

        # Print or do something with the text content
        print(text_content)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example: Replace 'https://example.com' with the URL of the webpage you want to copy
copy_text_from_webpage('https://chat.openai.com/share/e9a69261-cde6-4bf9-9c99-1b7fde2bd084')
