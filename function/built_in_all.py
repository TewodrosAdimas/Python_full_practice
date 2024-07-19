numbers = []
iterate = int(input("How many numbers you want to add in a list? "))
count = 0

for i in range(iterate):
    numbers.append(int(input(f"enter index {i}: ")))

if all(n > 2 for n in numbers):
    print("All numbers are greater than 2")
else:
    print("All numbers are not greater than 2") 

if any(n > 2 for n in numbers):
    print(f"There are numbers greater than 2")