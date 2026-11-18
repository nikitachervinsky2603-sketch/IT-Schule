print("Hi, wie heißt du?")
Name = input("Hier kannst du deine Name rein schreiben: ")
print("Oh, so eine Wunderschöne Name hast du, " + Name)
print("Und wie alt bist du " + Name + "?")
Alter = input("Schreib hier deinen Alter: ")
if Alter == "18":
    print("Du bist schon Volljärig, cool!")
elif Alter == "17":
    print("Noch bisschen, aber ist auch Okey!")
else: 
    print("Damit hatte ich nicht gerechnet, dass du sowas sagst!")