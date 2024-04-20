import PyPDF2
from datetime import datetime, timedelta
import time
from pushbullet import Pushbullet
import re
from datetime import datetime, timedelta
from pushbullet import Pushbullet

def send_notification(title, body):
    # Replace with your Pushbullet API key
    pb = Pushbullet("o.hfSU0YeVUEBdpjT7uimYg7xwuhBF3HvZ")
    push = pb.push_note(title, body)

def check_class_schedule(class_schedule):
    current_time = datetime.now()
    current_day = current_time.strftime("%A")
    current_hour_minute = current_time.strftime("%H:%M")

    alert_message = "No classes at the moment."

    for class_info in class_schedule:
        if class_info['day'] == current_day:
            class_start, class_end = class_info['time_range'].split(' to ')
            print(class_start,class_end)
            if class_start <= current_hour_minute <= class_end:
                alert_message = f"Class Alert!\n{class_info['class_name']} {class_info['class_code']} with {class_info['lecturer']} at {class_info['venue']}"
                send_notification("Class Alert", alert_message)
                print(alert_message)
                break
            else:
                alert_message = "Your free, I'll notify you of the next class"

    return alert_message        

def get_today_classes(class_schedule):
    current_time = datetime.now()
    current_day = current_time.strftime("%A")

    classes_today = []

    for class_info in class_schedule:
        if class_info['day'] == current_day:
            classes_today.append(f"{class_info['class_name']} ({class_info['class_code']}) with {class_info['lecturer']} at {class_info['time_range']} in {class_info['venue']}")

    if not classes_today:
        return "No classes today, enjoy your free time!"
    else:
        return "\n".join(classes_today)

class_schedule = [
    {'day': 'Monday', 'time_range': '7:00 to 10:00', 'class_name': 'BCT', 'class_code': '2301', 'lecturer': 'NANCY CHEMUTAI', 'venue': 'EG-28'},
    {'day': 'Monday', 'time_range': '10:00 to 13:00', 'class_name': 'BIT', 'class_code': '2115', 'lecturer': 'MUTURI', 'venue': 'ONLINE'},
    {'day': 'Monday', 'time_range': '14:00 to 17:00', 'class_name': 'BIT', 'class_code': '2118', 'lecturer': 'NJIRU', 'venue': 'LAB B-06'},

    {'day': 'Tuesday', 'time_range': '10:00 to 13:00', 'class_name': 'BCT', 'class_code': '2302', 'lecturer': 'KINUTHIA', 'venue': 'A-03'},

    {'day': 'Wednesday', 'time_range': '7 to 10', 'class_name': 'SMA', 'class_code': '2101', 'lecturer': 'FELICIAN', 'venue': 'EG-30'},
    {'day': 'Wednesday', 'time_range': '10:00 to 13:00', 'class_name': 'ICS', 'class_code': '2203', 'lecturer': 'KINYUA', 'venue': 'EG-02'},
    {'day': 'Wednesday', 'time_range': '14:00 to 17:00', 'class_name': 'BCT', 'class_code': '2309', 'lecturer': 'GACHUI', 'venue': 'LAB B-07'},


    {'day': 'Thursday', 'time_range': '8:00 to 10:00', 'class_name': 'BIT', 'class_code': '2118', 'lecturer': 'NJIRU', 'venue': 'A-03'},
    {'day': 'Thursday', 'time_range': '10:00 to 12:00', 'class_name': 'BCT', 'class_code': '2302', 'lecturer': 'KINUTHIA', 'venue': 'A-03'},
    {'day': 'Thursday', 'time_range': '14:00 to 13:00', 'class_name': 'BIT', 'class_code': '2115', 'lecturer': 'MUTURI', 'venue': 'B-06'},


    {'day': 'Friday', 'time_range': '7:00 to 10:00', 'class_name': 'ICS', 'class_code': '2105', 'lecturer': 'KARIS', 'venue': 'A-03'},
    {'day': 'Friday', 'time_range': '10:00 to 13:00', 'class_name': 'ICS', 'class_code': '2105', 'lecturer': 'KARIS', 'venue': 'A-03'},

]


alert_me = check_class_schedule(class_schedule)
today_classes_message = get_today_classes(class_schedule)
print(today_classes_message)