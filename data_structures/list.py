how_many = int(input("How many fruits you want to enter? "))

favourite_fruits = []
i = 0
while i <= how_many-1 :
    fruit = input("Enter fav fruit: ")
    favourite_fruits.append(fruit)
    i+=1
print(favourite_fruits)
print(favourite_fruits[1])