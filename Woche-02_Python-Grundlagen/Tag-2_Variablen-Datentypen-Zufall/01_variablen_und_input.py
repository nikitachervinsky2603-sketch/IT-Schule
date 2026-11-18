# -*- coding: utf-8 -*-

# Variablen speichert man so: 
name = "irgendein Testname seitens Programmierer:in"
age = 34

# concatenation 
print("Hello", name+"!", "Schön, dich kennenzulernen!")
print("Du bist also", age, "Jahre alt?")

# Datentypen
# string (also eine Zeichenkette)
print("34,00€ & 6,00 Euro")
print("34+6")

# ganze Zahl(en), mit denen Python auch direkt rechnet:
print(34 + 6)

# erster interaktiver Versuch: 
print("Wie ist denn dein Name?")
name = input()

print("Hallo", name+"!", "Schön, dich kennenzulernen!")

# hier machen wir eine TypeConversion, damit wir rechnen können:
age = int(input("Gib dein Alter ein: "))

birthYear = 2026 - age
print("Du bist geboren im Jahr", birthYear)