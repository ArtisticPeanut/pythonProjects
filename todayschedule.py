import schedule
import time as tm
from datetime import datetime , timedelta
import re

current_time = datetime.now()
current_day = current_time.strftime("%A")
print(current_day)
current_hour_minute = current_time.strftime("%H:%M:%S")


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






command = "plan coding, forex, web development,assignment, and today's classes"

tasks = re.findall(r'([a-zA-Z]+(?:, [a-zA-Z]+)*)', command)

print(tasks)
task_array =[]


new_book_time = datetime.strptime(current_hour_minute, "%H:%M:%S")

for task in tasks:
    task_details = task.split(', ')
    task_name = " ".join(task_details)
    print(task_name)

    start_datetime = datetime.strptime(current_hour_minute, "%H:%M:%S")
    end_datetime = start_datetime + timedelta(hours=2)

    start_time = start_datetime.strftime("%H:%M:%S")
    end_time = end_datetime.strftime("%H:%M:%S")
    duration = end_datetime - start_datetime
    period_hours, remainder = divmod(duration.seconds, 3600)
    period_minutes = remainder // 60

    print(f"Length: {period_hours} hrs :{period_minutes} minutes")
    print(f"Starts at :{start_time}")
    print(f"Ends at :{end_time}")

    keywords = ['code', 'coding', 'forex', 'web']
    if 'plan' not in task_name.lower() and any(keyword in task_name for keyword in keywords):
        print("true")
        print("task", task_name)
        task_array.extend(task_name.split())
    else:
        print("false")

print("Task Array:", task_array)


def is_class_scheduled(class_schedule, day, task_start_time, task_end_time,days_schedule):
    for class_info in class_schedule:
        if class_info['day'] == day:
            class_start, class_end = map(lambda x: datetime.strptime(x, "%H:%M"), class_info['time_range'].split(' to '))
            class_notice = f"class starts: {class_start} and ends at: {class_end}"
            print(class_notice)
            days_schedule.append(class_notice)


            if task_start_time < class_end and task_end_time > class_start:
                return True
    return False



def job(task, start_time, end_time):
    current_time = datetime.now()
    current_day = current_time.strftime("%A")
    print(current_day)
    current_hour_minute = current_time.strftime("%H:%M:%S")

    if current_hour_minute <= "19:00:00" and not is_class_scheduled(class_schedule, current_day, start_time, end_time):
        print(f"Scheduled task: {task} from {start_time} to {end_time}")
        
    else:
        print("Cannot schedule the task at the specified time due to class schedule or it's past 7 pm.")

days_schedule = []
for task in task_array:
    end_datetime = start_datetime + timedelta(hours=2)

    task_start_time = start_datetime
    task_end_time = end_datetime
    
    if is_class_scheduled(class_schedule, current_day, task_start_time, task_end_time,days_schedule):
        statement =f"Class scheduled during task: {task} from {task_start_time.strftime('%H:%M:%S')} to {task_end_time.strftime('%H:%M:%S')}"
        print(statement)
        days_schedule.append(statement)
    else:
        job(task, task_start_time.strftime("%H:%M:%S"), task_end_time.strftime("%H:%M:%S"))

    start_datetime = end_datetime

print(days_schedule,"TOTAL ITEMS ON TODAYS SCHEDULE :" ,len(days_schedule))
