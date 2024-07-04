import random
secret_number = random.randint(1,10)
counter = 0
guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess from 1 to 10: "))
    counter += 1

print (f"You guessed it in {counter} trial")    