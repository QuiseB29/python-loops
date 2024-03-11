import random
Cards =["Clubs", "Ace", "King", "Queen", "Joker"]
random.shuffle(Cards)

for card in Cards:
    print(card)
    #random shuffle can be used by shuffling the list not in the order it appears on your variable list.
    
import random
items = ["Apples", "Cherry", "Kiwi", "Blueberry", "Strawberry"]
    
random_item = random.choice(items)
    
player_guess = input ("Enter you guess:")
if player_guess.lower() == random_item:
        print("Congrats you guess right")
        
else:
    print(f"Sorry the right answer was {random_item}. Better luck next time")
    
    # Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")
