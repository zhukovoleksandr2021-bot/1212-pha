import random
from random import choice


class Student:

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.skills = 8
        self.money = random.randint(100, 500)

    def hello(self):
        print(f"Hi. My name is {self.name}! I am {self.year}")
        print(f"My skills is {self.skills:.2f}")
        print(f"I have {self.money}")

    def grow_up(self):
        self.year += 1

    def study(self):
        self.skills += 0.3

    def chill(self):
        self.skills -= 0.1
        exp = random.randint(100, 500)
        self.money -= exp
        print(f"-{exp}")


    def work(self):
        self.skills += 0.1
        self.money += 500

mark_5 = Student("Mark_5", 8)

for day in range(1,366):
    print(f"      Day {day}      ")

    choice = random.randint(0, 2)

    if choice == 0:
        mark_5.study()
        print("Styding......")

    elif choice == 1:
        mark_5.work()
        print("Working.....")

    else:
        mark_5.chill()
        print("Chilling.....")


mark_5.grow_up()
mark_5.hello()





