
import time
import webbrowser
import random


def zahlenraten():
    geheimzahl = random.randint(1, 100)
    counter = 0

    print("\nWillkommen beim Zahlenraten!")
    print("Du hast 6 Versuche!")

    while counter < 6:
        tipp = int(input("Rate die Zahl: "))
        counter = counter + 1

        if tipp < geheimzahl:
            print("Zu niedrig, du Landratte!")

        elif tipp > geheimzahl:
            print("Zu hoch!")

        else:
            print("Glückwunsch! Du hast gewonnen!")
            break

    if counter == 6 and tipp != geheimzahl:
        print("Game over!")
        print("Die Zahl war:", geheimzahl)


def main():
    gesamtzeit = int(input("Wie viele Stunden möchtest du lernen? "))
    lernrhythmus = float(input("Wie viele Minuten möchtest du lernen? "))

    arbeitszeit = 0
    gesamtzeit = gesamtzeit * 60

    while arbeitszeit < gesamtzeit:

        restzeit = gesamtzeit - arbeitszeit

        if restzeit >= lernrhythmus:
            print("\nArbeitszeit beginnt!")
            time.sleep(lernrhythmus * 60)
            arbeitszeit = arbeitszeit + lernrhythmus

        else:
            print("\nLetzte Arbeitsphase beginnt!")
            time.sleep(restzeit * 60)
            arbeitszeit = arbeitszeit + restzeit

        if arbeitszeit < gesamtzeit:
            print("\nPause beginnt!")

            webbrowser.open("https://www.youtube.com/watch?v=XFkzRNyygfk&list=RDXFkzRNyygfk&start_radio=1")

            time.sleep(7.5 * 60)

            print("Pause beendet!")

            warmup = input("Möchtest du ein Warm-Up spielen? (ja/nein): ").strip().lower()

            if warmup == "ja":
                zahlenraten()

            elif warmup == "nein":
                print("Okay! Weiter arbeiten!")

    print("\nDer Arbeitstag ist beendet!")


main()
