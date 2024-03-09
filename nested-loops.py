for i in range(3):
    for j in range(3):
        print("*", end=" ")  
    print() 
  
  #lesson 2
import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Melancholic", "Relaxed"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days_of_week:
    print(f"{day}:")
    for time in ["Morning", "Afternoon", "Evening"]:
        mood = random.choice(moods) 
        print(f"{time}: {mood}")
    print()  
#lesson 3

for i in range (1,6):
    for  j in range (1,6):
        print(i * j, end="\t")
        print()
