import pyautogui as pg 
import time as t  
import pyperclip as clip 
query = 'what is 100000/1000'
def move(query):
    t.sleep(2)

    pg.hotkey('win') 

    t.sleep(0.5)
# Type "Chrome" to search for the Chrome app
    pg.typewrite('Chrome')

    t.sleep(0.5)
    pg.click(696,345)

# Wait for a moment to allow the search results to appear
    t.sleep(1)

# Press Enter to open the Chrome app


    pg.click(612,644)

    t.sleep(0.2)

    pg.click(1570,78)

    pg.typewrite("https://chat.openai.com")

    pg.press("Enter")

    t.sleep(4)

    pg.click(37,134)

    t.sleep(1.5)

    pg.typewrite(query)

    pg.press("Enter")

    t.sleep(3)
    start_point = (780, 772)
    end_point = (1026, 936)
    copy_text_from_selected_point(*start_point, *end_point)
    t.sleep(1)
    




def copy_text_from_selected_point(start_x, start_y, end_x, end_y):
    # Move the mouse to the starting point
    pg.moveTo(start_x, start_y, duration=0.5)

    # Click and drag to the ending point to select the text
    pg.mouseDown()
    pg.moveTo(end_x, end_y, duration=1)
    pg.mouseUp()

    # Copy the selected text
    pg.hotkey('ctrl', 'c')

    t.sleep(3)
    selected_text = clip.paste()
    print(selected_text)
    return selected_text

# Example usage:
# Specify the coordinates of the starting and ending points


# Call the function with the specified points


# Optional: Wait for a short time to make sure the copy operation is completed
t.sleep(1)

# Now you can use the copied text as needed, for example, by pasting it somewhere
# (Note: You'll need to implement the paste operation separately based on your requirements)
move(query)








