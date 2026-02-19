class Parent:
    def __init__(self):
        self.height = 180

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.height += 5
        print(self.height)

johan = Parent()
mark_5 = Child()
