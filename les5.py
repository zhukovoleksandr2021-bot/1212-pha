class Parent:
    def __init__(self):
        self.height = 180
        self.weight = 90

    def intro(self):
        print(f"My height is {self.height}")

    def hz(self):
        print(f"My weight is {self.weight}")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.height += 5
        self.intro()
        self.weight -= 15
        self.hz()

johan = Parent()
mark_5 = Child()
