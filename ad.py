import pyautogui as pg
import time as t

# Add a sleep time to give you some time to switch to the screen where the image is expected


# Specify the correct path to your image file


# Try to locate the image on the screen)
image = pg.screenshot('skip_adss.png')
t.sleep(3)
# Print the result
location = pg.locateOnScreen(image)
position = pg.center(location)

print(position)
pg.doubleClick(960,540)