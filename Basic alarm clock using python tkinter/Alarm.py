import datetime
from playsound import playsound

# Get the alarm time from the user
alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minutes: "))
alarmAm = input("am / pm: ")

# Convert the alarm time to 12-hour format if the user specified am or pm
if alarmAm == "pm":
    alarmHour += 12

# Start a while loop to check if the current time matches the alarm time
while True:

    # Get the current time
    currentTime = datetime.datetime.now()

    # Check if the alarm time matches the current time
    if alarmHour == currentTime.hour and alarmMin == currentTime.minute:

        # Print a message to the user
        print("Playing the alarm.....")

        # Play the alarm sound
        playsound("Alarm.mp3")

        # Break out of the while loop
        break
