import random
# The Guessing Game
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_number = 18


for _ in range(2,20):
    numbers = random.randint(2,20)
    if target_number == 12:
        print(f"You found {target_number}")
        
    if target_number > 12:
        print (f"Too High ")
        break
    else:
        print(f"Too low")
        break
   
   
   # The Magic 8-Ball
import random
advices = ["Keep your head up", "Stay good ", "Dont lose track", "Stay focus", "Dont judge","Be happy", "Love yourself first"]
user = input ("What is your question?:")

for advice in advices:
    print(random.choice(advices))
    break


import random

suites = ["King", "Queen", "Jack", "Ace","Club", "Heart", "Spades", "Diamonds" ]
rank = [1, 2, 3, 4, 5, 6, 7, 8 ]
user = input ("Enter Card:")

for suit in suites:
    print(random.choice(suites))
    print(random.choice(rank))
    break
