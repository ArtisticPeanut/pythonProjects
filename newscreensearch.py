from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pytesseract
from PIL import Image

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/HomePC/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

def capture_website_text(url):
    # Set up Chrome options to run in headless mode (without opening a browser window)
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Create a WebDriver instance (you need to have ChromeDriver installed)
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the specified URL
    driver.get(url)

    # Wait for the webpage to load (you may need to adjust the waiting time)
    time.sleep(5)

    # Use developer tools to inspect and interact with the elements on the webpage
    # For example, find all paragraphs on the page and store their text and positions
    text_positions = []
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    for paragraph in paragraphs:
        position = paragraph.location
        text = paragraph.text
        text_positions.append({"text": text, "position": position})

    # Check if the word "coding for data" is present in any of the stored text
    keyword = "register"
    keyword_present = any(keyword in entry["text"].lower() for entry in text_positions)

    # Print "Yes" and the position if the word "coding for data" is present
    if keyword_present:
        keyword_positions = [entry["position"] for entry in text_positions if keyword in entry["text"].lower()]
        print(f"Yes, '{keyword}' is present at the following positions:")
        for index, position in enumerate(keyword_positions, start=1):
            print(f"Position {index}: {position}")
    else:
        print(f"No, '{keyword}' is not present.")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    website_url = "https://www.sololearn.com/"  # Replace with the URL of the website you want to capture
    time.sleep(5)
    capture_website_text(website_url)
