import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time as t
import io

t.sleep(2)

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
    t.sleep(5)

    # Get the dimensions of the entire page
    page_width = driver.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
                                       "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
                                       "document.documentElement.offsetWidth);")
    page_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
                                        "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
                                        "document.documentElement.offsetHeight);")

    # Take a screenshot of the entire page
    screenshot = driver.get_screenshot_as_png()

    # Convert the screenshot to a PIL Image
    image = Image.open(io.BytesIO(screenshot))

    # Use Tesseract OCR to extract text from the image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print("Extracted Text:")
    print(text)

    # Note: Finding positions on a website using OCR may not be as accurate, consider using other methods for precise position extraction.

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    website_url = "https://www.sololearn.com/"  # Replace with the URL of the website you want to capture
    t.sleep(5)
    capture_website_text(website_url)
