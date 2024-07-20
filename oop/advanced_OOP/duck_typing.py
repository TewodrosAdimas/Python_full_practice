class Dog:
    def make_sound():
        return "make sound from dog"


class Cat:
    def make_sound():
        return "make sound from cat"


class Bird:
    def make_sound():
        return "make sound from bird"
    

def let_them_speak():
    for speak in (Dog, Cat, Bird):
        print(speak.make_sound())

let_them_speak()