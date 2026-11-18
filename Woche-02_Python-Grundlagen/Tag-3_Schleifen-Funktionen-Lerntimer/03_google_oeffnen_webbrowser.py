
import webbrowser

eingabe = input("Was möchtest du machen? ")

if eingabe == "suchen":
    print("Google wird geöffnet...")
    webbrowser.open("https://www.google.com")

else:
    print("Unbekannter Befehl!")
