for i in  range(-5,-2):
    print(i)
    
import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm","Shy"]

# Define days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week
for day in days_of_week:
    # Randomly select a mood for the day
    mood = random.choice(moods)
    # Print the mood for the day
    print(f"On {day}, I am feeling {mood}.")
    
    timer = 10
    # Countdown timer starting from 10
for i in range(10, 0, -1):
    print(i)

