
import random

geheimzahl = random.randint(1, 100)
counter = 0

print("Willkommen beim Zahlenraten!")
print("Käpt'n Hook hat eine Zahl zwischen 1 und 100 gewählt.")
print("Du hast 7 Versuche!")

while counter < 7:
    tipp = int(input("Rate die Zahl: "))
    counter = counter + 1

    if tipp < geheimzahl:
        print("Zu niedrig, du Landratte!")

    elif tipp > geheimzahl:
        print("Zu hoch!")

    else:
        print("Glückwunsch! Käpt'n Hook gibt dir seinen Schatz!")
        break

if counter == 7 and tipp != geheimzahl:
    print("Game over!")
    print("Die geheime Zahl war:", geheimzahl)
