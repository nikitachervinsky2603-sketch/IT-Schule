import random

counter = 0

for i in range(5):
    zahl = random.randint(1, 6)
    counter = counter + 1

    print(zahl)
    print("Anzahl der Würfel:", counter)
