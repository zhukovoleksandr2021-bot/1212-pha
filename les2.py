import random
from random import choice


class Student:

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.skills = 8

    def hello(self):
        print(f"Hi. My name is {self.name}! I am {self.year}")
        print(f"My skills is {self.skills:.2f}")

    def grow_up(self):
        self.year += 1

    def study(self):
        self.skills += 0.3

    def chill(self):
        self.skills -= 0.1

mark_5 = Student("Mark_5", 8)

for day in range(1,366):
    print(f"      Day {day}      ")

    choice = random.randint(0, 1)

    if choice == 0:
        mark_5.study()
        print("Styding......")

    else:
        mark_5.chill()
        print("Chilling.....")

mark_5.grow_up()
mark_5.hello()





