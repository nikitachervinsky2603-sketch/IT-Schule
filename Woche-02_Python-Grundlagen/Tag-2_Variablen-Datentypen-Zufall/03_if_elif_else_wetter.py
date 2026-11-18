# -*- coding: utf-8 -*-

print("Willkommen beim Chat mit Ada Lovelace!")

# if - (elseif) -> elif - else
#Kontrollstrukturen

weatherGood = input("Ist das Wetter heute bei dir gut? Tippe ein: Ja oder Nein")

if weatherGood == "Ja":
    print("Cool, dann lass ich meinen Schirm zuhause und nehme das Fahrrad.")
elif weatherGood == "Nein":
    print("Oh no - dann nehme ich die Regenjacke und fahre mit der Bahn.")
else:
    print("Ah okay, das ist auch eine Antwort...")

print("Ende des Programms")