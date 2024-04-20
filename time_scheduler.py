import schedule 
import time as tm
from datetime import time , timezone,  datetime

def job():
    print("go do some work")

schedule.every().day.at('12:59').do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)
