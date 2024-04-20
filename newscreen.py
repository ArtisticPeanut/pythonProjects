import pytesseract
from PIL import Image
import pyautogui
import time as t

t.sleep(5)

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/HomePC/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

def capture_website_text():
    # Get the position and size of the browser window
    browser_window_position = (0, 0)  # Adjust these values based on your browser's position
    browser_window_size = (1920, 1080)  # Adjust these values based on your browser's size

    # Take a screenshot of the browser window region
    screenshot = pyautogui.screenshot(region=(browser_window_position[0], browser_window_position[1],
                                               browser_window_size[0], browser_window_size[1]))

    # Use Tesseract OCR to extract text from the website screenshot
    text = pytesseract.image_to_string(screenshot)

    # Print the extracted text
    print("Extracted Text:")
    print(text)

    # Note: Finding positions on a website is more complex and may require additional libraries or approaches.

if __name__ == "__main__":
    t.sleep(5)
    capture_website_text()
