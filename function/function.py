def user_info(name, age = None):
    print(name)
    if age:
        print(age)
    return age * 2

print(user_info(name ="abebe", age = 32))
