class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} make sound . . .")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        super().make_sound()
        print("Woof...")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        super().make_sound()
        print("Muay...")

class Rabbit(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        super().make_sound()
        print("Fuv fuv...")




cane_corso = Dog("Cane corso")
cane_corso.make_sound()

British_Shorthair = Cat("British Shorthair")
British_Shorthair.make_sound()

flandr = Rabbit("Flandr")
flandr.make_sound()