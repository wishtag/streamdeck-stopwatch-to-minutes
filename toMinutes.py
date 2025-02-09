import pyautogui

with open('timer.txt', 'r') as file:
    for line in file:
        theTime = line.strip()

theTime = theTime.split(":")
if len(theTime) == 3:
    hours = int(theTime[0])
    minutes = int(theTime[1])
    seconds = int(theTime[2])
else:
    hours = 0
    minutes = int(theTime[0])
    seconds = int(theTime[1])

asMinutes = (hours*60) + minutes + (seconds/60)

pyautogui.typewrite(str(asMinutes))