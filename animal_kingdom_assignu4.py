class animal_kingdom:
    def __init__(self, name):
        self.name =  name
    def eat(self):
        print(f"{self.name} is eating.")
class dog(animal_kingdom):
    def bark(self):
        print("woof!")

my_dog = dog("buddy")
my_dog.eat()
my_dog.bark()