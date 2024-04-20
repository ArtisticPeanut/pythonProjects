import pytesseract
from PIL import Image
import pyautogui
import ctypes
import os
import time as t

t.sleep(5)


# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/HomePC/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'





def capture_screen_text():
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to grayscale
    screenshot_gray = screenshot.convert('L')

    # Use Tesseract OCR to extract text from the image
    text = pytesseract.image_to_string(screenshot_gray)

    # Print the extracted text
    print("Extracted Text:")
    print(text)

    # Find and print the positions of the text elements
    text_positions = pyautogui.locateAllOnScreen(text)
    print("Text Positions:")
    for position in text_positions:
        print(position)

if __name__ == "__main__":
    t.sleep(5)
    capture_screen_text()
