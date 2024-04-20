import pyautogui as pg 
import time as t 

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

t.sleep(1)
pg.click(1570,78)
    
t.sleep(0.5)

pg.typewrite("https://elearning.mmu.ac.ke/login")
t.sleep(4)
pg.hotkey("enter")

pg.click(741,442)
t.sleep(0.80)
pg.typewrite("cit-222-007/2022")
t.sleep(1)
