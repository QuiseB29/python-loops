for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
    continue
for j in range(6,12):
    print(j)
#code correction

import random
moods = ["Happy", "Sad", "Angry", "Hopeful", "Guilty"]
lunchtime = 12
    
for hour in range(24):
        if hour == lunchtime:
            continue
        
        mood = random.choice(moods)
        print(f"At {hour}:00 im feeling {mood}")
        #Mood swings
        
        numbers = [2, 8, 6 , 5 , 7]
        target_number = 6
      
for num in numbers:
 if num == target_number:
    print(f"Number {target_number} is found")
    break
else:
 print(f"number {target_number} is not found")
 #Target number

            