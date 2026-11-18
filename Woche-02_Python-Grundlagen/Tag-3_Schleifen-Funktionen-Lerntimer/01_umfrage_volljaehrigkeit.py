
def umfrage():
    ageCheck = int(input("Wie alt bist du? "))

    law = input("Lebst du in einem Land, in dem man mit 18 volljährig ist? (ja/nein): ")

    monthBirthday = int(input("In welchem Monat hast du Geburtstag? (1-12): "))

    monthCurrent = int(input("Welcher Monat ist aktuell? (1-12): "))

    monate = (monthBirthday - monthCurrent) % 12

    if ageCheck >= 18:
        adult = True
    else:
        adult = False

    print("Adult:", adult)

    if law == "ja" and adult == True:
        horrormovie = input("Siehst du gerne Horrorfilme ab 18? (ja/nein): ")

        if horrormovie == "ja":
            print("Cool! Du magst Horrorfilme!")
        else:
            print("Kein Problem! Jeder hat andere Interessen.")

    elif ageCheck < 18:
        print("Du bist noch nicht volljährig.")
        print("Komm in", monate, "Monaten wieder.")

    else:
        print("Du bist noch nicht volljährig.")

    print("Danke für deine Teilnahme!")


umfrage()
