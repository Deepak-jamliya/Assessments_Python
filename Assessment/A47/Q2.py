class Animal:
    def makeSound(self):
        print("Some generic sound.")


class Dog(Animal):
    def makeSound(self):
        print("Woof Woof.")


class Cat(Animal):
    def makeSound(self):
        print("Meow Meow.")



animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.makeSound()