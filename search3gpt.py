import pyautogui
import time
import search3gpt as gpt 



def copy_text_from_selected_point(start_x, start_y, end_x, end_y):
    # Move the mouse to the starting point
    pyautogui.moveTo(start_x, start_y, duration=0.5)

    # Click and drag to the ending point to select the text
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=1)
    pyautogui.mouseUp()

    # Copy the selected text
    pyautogui.hotkey('ctrl', 'c')

# Example usage:
# Specify the coordinates of the starting and ending points
start_point = (100, 200)
end_point = (300, 400)

# Call the function with the specified points
copy_text_from_selected_point(*start_point, *end_point)

# Optional: Wait for a short time to make sure the copy operation is completed
time.sleep(1)

# Now you can use the copied text as needed, for example, by pasting it somewhere
# (Note: You'll need to implement the paste operation separately based on your requirements)
