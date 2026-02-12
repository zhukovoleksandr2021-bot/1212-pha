from itertools import count


class human:

    def __init__(self, name):
        self.name = name

class car:

    def __init__(self, brand):
        self.brand = brand
        self.pase = []

    def add_pase(self, pase: human):
        count = len(self.pase)
        if count >= 5:
            print(f"Немає місця: {pase.name}")
        else:
            self.pase.append(pase)


    def leave_pase(self, pase: human):
        print(f'Pase {pase.name} left {self.brand}.')
        self.pase.remove(pase)



    def show_pase(self):
        print(f'In {self.brand} ', end='')
        if self.pase:
            print(f'{len(self.pase)} passengers:')
            for pase in self.pase:
                print(pase.name)
        else:
            print("There are not passengers.")

alex = human("Alex")
oleksandr = human("Oleksandr")
anton = human("Anton")
sergey = human("Sergey")
illa = human("Illa")
uran_235 = human("Uran_235")

maserati = car("Maserati GranTurismo")
maserati.add_pase(alex)
maserati.add_pase(oleksandr)
maserati.add_pase(sergey)
maserati.add_pase(uran_235)
maserati.add_pase(illa)
maserati.leave_pase(illa)
maserati.add_pase(anton)
maserati.show_pase()
