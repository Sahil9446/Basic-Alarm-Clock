import datetime
from playsound import playsound

alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minutes: "))
alarmAm = input("am / pm: ")

if alarmAm == "pm":
    alarmHour += 12

while True:
    currentTime = datetime.datetime.now()
    if alarmHour == currentTime.hour and alarmMin == currentTime.minute:
        print("Playing the alarm.....")
        playsound("Alarm.mp3")
        break
