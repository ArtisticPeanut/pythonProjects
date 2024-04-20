import threading
import time

# Dictionary to store active timers
timers = {}

def timer_callback(timer_name):
    print(f"Timer '{timer_name}' has finished!")

def set_timer(timer_name, duration_seconds,word):
    def timer_thread():
        time.sleep(duration_seconds)
        print(word)
        timer_callback(timer_name)
        del timers[timer_name]  # Remove timer from the dictionary after it's done

    timers[timer_name] = threading.Thread(target=timer_thread)
    timers[timer_name].start()
 
def cancel_timer(timer_name):
    if timer_name in timers:
        timers[timer_name].join()  # Wait for the timer thread to finish
        del timers[timer_name]     # Remove timer from the dictionary
        print(f"Timer '{timer_name}' has been canceled.") 
    else:
        print(f"No active timer with name '{timer_name}'.")

# Example usage:
set_timer("Timer 1", 5,"ola")  # Set a timer for 5 seconds
set_timer("Timer 2", 10, "hello") # Set another timer for 10 seconds

# Wait for user input to cancel a timer
input_timer_name = input("Enter the name of the timer to cancel: ")
cancel_timer(input_timer_name)

# Wait for the remaining timers to finish
time.sleep(15)
