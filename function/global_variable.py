#nonlocal is used to modif variable from inner function that declared/initialized from outer function
#global is used to modify variables from/inside function that declared out of function 

y = z = 5

def outer_function():
    x = 10  # Variable in the enclosing function
    global y
    y = 10
    def inner_function():
        nonlocal x  # Using nonlocal to modify x from the enclosing function
        x += 5  # Modifying the value of x

    inner_function()  # Calling the nested function
    print("Modified value of x from inner function:", x)
outer_function()
print(f"Y is global variable and modified to: {y}")