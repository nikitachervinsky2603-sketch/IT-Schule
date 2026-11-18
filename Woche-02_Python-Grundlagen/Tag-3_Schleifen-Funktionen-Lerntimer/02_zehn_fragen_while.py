
import time

counter = 0

while counter < 10:

    counter = counter + 1

    if counter == 1:
        print("Frage 1: Wie heißt du?")
    elif counter == 2:
        print("Frage 2: Wie alt bist du?")
    elif counter == 3:
        print("Frage 3: Wo wohnst du?")
    elif counter == 4:
        print("Frage 4: Was ist deine Lieblingsfarbe?")
    elif counter == 5:
        print("Frage 5: Was ist dein Lieblingsessen?")
    elif counter == 6:
        print("Frage 6: Welche Musik hörst du gerne?")
    elif counter == 7:
        print("Frage 7: Spielst du ein Instrument?")
    elif counter == 8:
        print("Frage 8: Was ist dein Hobby?")
    elif counter == 9:
        print("Frage 9: Was möchtest du später werden?")
    elif counter == 10:
        print("Frage 10: Was ist dein größter Traum?")

    sekunden = 10

    while sekunden > 0:
        print(sekunden)
        time.sleep(1)
        sekunden = sekunden - 1

    antwort = input("Deine Antwort: ")
    print("Deine Antwort war:", antwort)

print("Der Test ist beendet! Danke!")
