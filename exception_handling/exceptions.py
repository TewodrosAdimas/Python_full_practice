#Custom exception

class ValueTooHighError(Exception):
    def __init__(self, num):
        self.user_num = num

    def __str__(self):
        return f"Sorry, the item '{self.user_num}' is greater than 100."

def numCheck(user_num):
    if user_num > 100:
        raise ValueTooHighError(user_num)
    else:
        print("Correct")

#Check custom exception
try:
    numCheck(500)  
except ValueTooHighError as e:
    print(e)


def zeroError():
    x = 5
    y = 0
    try:
        print(x/y)

    except ZeroDivisionError as e:
        print(e)


def fileNotFound():
    try:
        file = open("files.txt")
        read = file.read()
        print(read)
    except FileNotFoundError as e:
        print (e)

