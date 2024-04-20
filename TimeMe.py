import time as t

commands = ["time", "me", "for","seconds"]

user_input = str.lower(input("Enter Command : "))
array = []
wordsFound = []
sum = 0
timer = 0
print(user_input.split())
for word in user_input.split():
    print("word : " + word )
    
    array.append(word)
    for command in commands:
        print(command + ".......")
        if word == command:
            wordsFound.append(word)
            print("present")
            sum += 1
if sum > 2:
    for item in array:
       try:
           number = int(item)
           print("timing :", number)
       except ValueError:
           pass
              
    if "minutes" in array:
        timer = number * 60
        end  = "minutes"
    elif "hours" in array:
        timer = number *3600
        end = "hours"
    elif "milliseconds" in array:
        timer = number /60
        end = "milliseconds"
    else:
        end = "seconds"
    




print("Total commands found:", sum)
print("words Found " , wordsFound)
print("Words in the input:", array)
print("timing you for : ",number,end )

def settimer(num):
    
