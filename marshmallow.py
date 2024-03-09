marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    #Since marshmallow is placed ahead , it updates with each marshmallow addition.
    
    
    marshmallows = 0
while marshmallows < 5:
   
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1
    #The difference between the two, Example 1 updates normally. Anytime a marshmellow is added it count up.
    #While example 2 doesnt updates, it stays at a consistent number. Even though it execute code, it doesnt have a end.
    

marshmallows_in_bag = 0
while marshmallows_in_bag < 10:
    marshmallows_in_bag += 1
    print("Adding marshmallow to the bag. Total:", marshmallows_in_bag)

print("Bag is full with", marshmallows_in_bag, "marshmallows.")
#This cause the have 11 marshmallows then 10, exceeding the inital count. 

marshmallows_in_bag = 0
while marshmallows_in_bag < 10:
    print("Adding marshmallow to the bag. Total:", marshmallows_in_bag + 1)
    marshmallows_in_bag += 1

print("Bag is full with", marshmallows_in_bag, "marshmallows.")

#The corrected code is stopping the count exactly at 10 and not giving a off by one error 