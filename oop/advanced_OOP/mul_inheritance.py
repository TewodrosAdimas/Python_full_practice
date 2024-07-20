class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"The name of bird is: {self.name} and can fly"


class Mammal:
    def __init__(self, country) :
        self.country = country

    def run(self):
        return f" The country of bird is: {self.country} and can run"


class Bat(Bird, Mammal):
    def __init__(self,name , country):
        super().__init__(name, country)


bird = Bat("bat", "Ethiopia")
print(bird.fly() , bird.run())