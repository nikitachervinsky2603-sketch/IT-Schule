
import time
import webbrowser

gesamtzeit = int(input("Wie viele Stunden möchtest du lernen? "))
lernrhythmus = int(input("Wie viele Minuten möchtest du lernen, bevor du eine Pause machst? "))

arbeitszeit = 0
gesamtzeit = gesamtzeit * 60

while arbeitszeit < gesamtzeit:

    restzeit = gesamtzeit - arbeitszeit

    if restzeit >= lernrhythmus:
        print("Arbeitszeit beginnt!")
        time.sleep(lernrhythmus * 60)
        arbeitszeit = arbeitszeit + lernrhythmus

    else:
        print("Letzte Arbeitsphase beginnt!")
        time.sleep(restzeit * 60)
        arbeitszeit = arbeitszeit + restzeit

    if arbeitszeit < gesamtzeit:
        print("Pause beginnt!")

        webbrowser.open("https://www.youtube.com/watch?v=XFkzRNyygfk&list=RDXFkzRNyygfk&start_radio=1")

        time.sleep(7.5 * 60)

        print("Pause beendet! Weiter arbeiten!")

print("Der Arbeitstag ist beendet!")
