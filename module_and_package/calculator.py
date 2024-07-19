def add(x,y):
    return x+y

def subtruct(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        z =x/y
        return z
    except ZeroDivisionError:
        z = "Can not divide by zero"
        return z