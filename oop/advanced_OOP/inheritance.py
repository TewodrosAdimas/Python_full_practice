class Animal:
    def __init__(self,type, country) :
        self.type = type
        self.country = country

    def eat(self, food):
        self.food = food
        return f"{self.type} eats {food}"

    def sleep(self):
        return "sleep everyday"



class Dog(Animal):
    def __init__(self, type, country, sound):
        super().__init__(type, country)
        self.sound = sound

    def bark(self):
        return f"bark as {self.sound}"

dog1 = Animal("Mamal", "Ethiopia")
print(dog1.eat("meat"))
dog1 = Dog("Mamal", "Ethiopia", "Awwww")
print(dog1.eat("meat"))
