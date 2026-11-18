import random

class Hauskatze:
    def __init__(self, name):
        self.name = name
        self.hunger = 3

    def fuettern(self):
        if self.hunger == 0:
            print(f"{self.name} ist satt und wirft den Napf vom Tisch.")
            return

        self.hunger -= 1
        print(f"{self.name} frisst und schaut dich kurz dankbar an. Hunger: {self.hunger}")

    def streicheln(self):
        if self.hunger > 0:
            print(f"{self.name} faucht: Erst Futter, dann Kuscheln!")
            return

        if random.randint(1, 3) == 1:
            print(f"{self.name} beißt dich. Einfach so. Weil sie es kann.")
        else:
            print(f"{self.name} schnurrt wie ein Traktor. Mission erfüllt!")


name = input("Wie heißt deine Katze? ")
katze = Hauskatze(name)

while True:
    aktion = input("Was willst du tun? (f = füttern, s = streicheln, q = beenden) ")

    if aktion == "f":
        katze.fuettern()
    elif aktion == "s":
        katze.streicheln()
    elif aktion == "q":
        print("Tschüss!")
        break
    else:
        print(f"{katze.name} versteht dich nicht und leckt sich die Pfote.")