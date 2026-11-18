import random

counter = 0

while counter < 30:
    zahl = random.randint(1, 6)
    counter = counter + 1

    print(zahl)
    print("Anzahl der Würfel:", counter)

print("Fertig!")