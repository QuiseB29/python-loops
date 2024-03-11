temperature = 100 
while temperature < 0:
    temperature += 1
    print("Temperature is now " + temperature)
    
print("Temperature was never 0")
#Loop that was never true. 
if temperature > 50: 
    temperature += 1 
    print("Temperature Is now :", + temperature)
    #Loop that becomes true. Basically explaing if the temperature is greater than 50 add 1.
    #In this case temperature is already 100 so it just added 1
    
 
x = 0
y = 5

while x < 10 and y > 0:  # Loop continues as long as both conditions are true
    print("x:", x, "y:", y)
    x += 1
    y -= 1
