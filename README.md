# streamdeck-stopwatch to Minutes
Some websites (specifically [ShinyHunt](https://www.shinyhunt.com/counters)) store time as minutes. This is a python program to convert [BarRaider's stopwatch plugin's](https://github.com/BarRaider/streamdeck-stopwatch) output to minutes.

# Usage
Configure the settings for your stopwatch to look like this, with the save location being in the same directory as `toMinutes.py` and the file name being `timer.txt`  
![1](img/1.png?raw=true)  
Then add a new `Open` action to your streamdeck and set the application it opens `toMinutes.bat`  
![2](img/2.png?raw=true)  
That's really all there is to it. Now once you click the `Open` action you created it will type out the stopwatch time as minutes.