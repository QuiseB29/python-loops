numbers = [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_number = 6

index = 0
while index <len(numbers):
    if numbers[index] == target_number:
        print(f"Number {target_number} is found")
        break
    index += 1
    
else:
    print("Number not found")
    #Check to see if a specific number can be found. Else statement provide in altenative if number cant be found.
   
n = 20
while n > 0:
    n -= 1
    if n % 3 == 0:
        continue
    print(n)
    print("Loop is finished") # continue allow to skip pass the numbers that't multple of 3 and continue to the next iteration .

x = 0
while x < 10:
    if x == 5:
        pass
    else:
        print(x)
        x += 1 #Pass is a placeholder. Somewhat stalling just so if they needed to be change it can once ready.
