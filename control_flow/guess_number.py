import random
secret_number = random.randint(1,10)
num_trials = 0


def startGame(num_trials):
    guess= int(input("Guess from 1 to 10: "))
    if guess == secret_number:
        print("Congratulations, you guessed it!")
        exit()
    elif guess > secret_number:
        print("Oops, your guess is a bit high. Try again!") 
        if num_trials < 2:
            num_trials=trial(num_trials)
        else:
            print("You lost, limit reached")
    else:
        print("Nope, your guess is a bit low. Give it another shot!")
        if num_trials < 2:
            num_trials=trial(num_trials)
        else:
            print("You lost, limit reached")


def trial(num_trials):
    num_trials= num_trials+1
    print(f"You tried {num_trials} times and left with {3-num_trials} chance(s) ")
    trial = input("(Y) Continue (X) Exit: ").lower()
    match trial:
        case "y":
            startGame(num_trials)
        case "x":
            exit()
        case _:
            print("Invalid Input")
            exit()
    
startGame(num_trials)