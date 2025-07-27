# monza-2024-driver-comparison

# F1 Driver Lap Time Comparison using FastF1

Hi again! I'm Pía 🌸 I'm 18 and currently studying engineering — and honestly, I’ve been super obsessed with Formula 1 lately. This little project is part of my learning journey in motorsport analytics.

This time, I made a script that compares two F1 drivers' lap times during the **2024 Italian Grand Prix in Monza**.  
I picked **Yuki Tsunoda** (my favorite 💙) and **Max Verstappen** (who's super consistent and fast), just to compare how their performance looked lap-by-lap.

---

## What this project does

- Loads real race data using [FastF1](https://theoehrly.github.io/Fast-F1/)
- Filters lap data for two drivers
- Detects and marks:
  - **Fastest lap** for each driver (red dot)
  - **Pit stop laps** (purple Xs)
- Generates a graph showing lap time vs lap number for each driver

This is just an example — you can totally change the drivers and analyze anyone you like!

---

## Technologies used

- Python 3.12.5 
- FastF1 (latest version)  
- Matplotlib (for graphs)  
- VS Code (I love it for coding lol)

---

## What I learned

- How to filter and visualize multiple data sets at once  
- How to plot race performance clearly  
- How to detect key moments like pits and best laps  
- And mostly, how exciting it is to explore data from F1 races 

---

##  Output example

Here's an example of what the chart looks like:  
https://github.com/Piekc/monza-2024-driver-comparison/blob/2a209626d524397ae8aeb44614a510d1f058ef87/YukiVer.png 

---

## How to run it

1. Open the option "New Terminal" on python
2. Install FastF1: pip install -U fastf1
3. Code example: https://github.com/Piekc/monza-2024-driver-comparison/blob/af77b2e1405fc9bdca2a69117754ed7f173f897f/YukiVER.py
4. After writing the code open your terminal and run: python Name_of_your_file.py
5. Run the script! It will:
- Load the Monza 2024 race
- Pull all the lap data
- Plot both drivers on the same graph

## How to change the drivers
You’ll find this part in the code:

Just replace 'TSU' and 'VER' with any other F1 driver codes, like:

'HAM' for Lewis Hamilton
'PER' for Sergio Pérez
'LEC' for Charles Leclerc
…and the rest will work the same way.

```python
drivers = {
 'Yuki Tsunoda': 'TSU',
 'Max Verstappen': 'VER'
}
