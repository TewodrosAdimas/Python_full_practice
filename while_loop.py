age = 0
counter = 0
while age < 18  and counter <3:
  counter += 1
  age = int(input("Enter your age (must be 18 or older): "))

if counter<3 :
    print("You are old enough to proceed.")

else:
   print("You are not old enough")