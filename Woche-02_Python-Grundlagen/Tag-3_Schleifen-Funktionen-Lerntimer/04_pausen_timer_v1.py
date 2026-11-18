import time
import webbrowser

arbeitszeit = 0

while arbeitszeit < 480:

    print("Arbeitszeit beginnt!")
    time.sleep(90 * 60)

    arbeitszeit = arbeitszeit + 90

    if arbeitszeit < 480:
        print("Pause beginnt!")
        webbrowser.open("https://www.youtube.com/watch?v=XFkzRNyygfk&list=RDXFkzRNyygfk&start_radio=1")

        time.sleep(7.5 * 60)

        print("Pause beendet! Weiter arbeiten!")

print("Der Arbeitstag ist beendet!")