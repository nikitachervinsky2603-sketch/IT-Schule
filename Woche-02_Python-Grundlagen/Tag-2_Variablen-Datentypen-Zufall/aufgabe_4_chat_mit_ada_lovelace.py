
print("Hallo! Ich bin Ada Lovelace.")
print("Lass uns ein bisschen reden!")

name = input("Wie heißt du? ")

print("Schön dich kennenzulernen,", name, "!")

frage = input("Möchtest du wissen, wie ich heiße? ")

if frage == "ja":
    print("Ich heiße Ada Lovelace!")
else:
    print("Okay,", name, "!")

alter = int(input("Wie alt bist du? "))

if alter < 18:
    print("Du bist noch jung,", name, "!")
else:
    print("Du bist schon erwachsen,", name, "!")

print("Was magst du lieber?")
print("1 - Programmieren")
print("2 - Musik")

antwort = input("Deine Antwort (1 oder 2): ")

if antwort == "1":
    print("Sehr interessant! Ich liebe Mathematik und Programmierung!")
else:
    print("Musik ist auch wunderbar!")

print("Wusstest du, dass ich am 10. Dezember 1815 geboren wurde?")
print("Ich arbeitete mit Charles Babbage an seiner Analytical Engine.")
print("Ich schrieb einen Algorithmus zur Berechnung von Bernoulli-Zahlen.")

print("Ich habe noch eine Frage an dich!")
antwort = input("Glaubst du, dass Computer die Zukunft verändern werden? (ja/nein): ")

if antwort == "ja":
    print("Das sehe ich genauso,", name, "!")
elif antwort == "nein":
    print("Das überrascht mich,", name, "!")
else:
    print("Das war leider keine gültige Antwort.")

print("Es war schön, mit dir zu reden,", name, "!")
print("Auf Wiedersehen!")
