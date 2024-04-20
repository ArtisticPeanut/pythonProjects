from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from PIL import Image
import pytesseract

# Set the path to your Tesseract executable (change accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/HomePC/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

def capture_and_ocr(url):
    # Set up the Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

    # Create a Chrome webdriver
    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    # Open the webpage
    driver.get(url)

    # Capture a screenshot of the webpage
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)

    # Use PyTesseract to extract text from the screenshot
    extracted_text = extract_text_from_image(screenshot_path)

    # Find all elements containing text on the webpage
    # Find all elements containing text on the webpage
    text_elements = driver.find_elements(By.XPATH, "//body//*[not(self::script) and not(self::style) and not(self::noscript) and not(self::head)]//*[text()]")

# Iterate over the text elements, extract their text and position, and display them
    for element in text_elements:
        text = element.text
        location = element.location
        size = element.size
        print(f"Text: {text}, Location: {location}, Size: {size}")


    # Close the webdriver
    driver.quit()

def extract_text_from_image(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Use PyTesseract to do OCR on the image with color information
    text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    return text

if __name__ == "__main__":
    # Provide the URL of the webpage you want to capture
    webpage_url = "https://elearning.mmu.ac.ke/login/index.php"

    # Call the function to capture the screenshot and perform OCR
    capture_and_ocr(webpage_url)
