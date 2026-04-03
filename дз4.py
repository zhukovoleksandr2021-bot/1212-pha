class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} видає звук:")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Гав-гав")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Мяу-мяу")

class Rabbit(Animal):
    def make_sound(self):
        super().make_sound()
        print("Фур-фур")

cane_corso = Dog("Кане-корсо")
british_shorthair = Cat("Британська кішка")
flandr = Rabbit("Фландрс")

cane_corso.make_sound()
british_shorthair.make_sound()
flandr.make_sound()
