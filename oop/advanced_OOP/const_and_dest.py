class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Good bye")

person1 = Person("Abebe", 28)

# del person1

print(person1.name)