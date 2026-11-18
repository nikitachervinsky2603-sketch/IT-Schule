import random
import ollama
from flask import Flask, render_template, request

MODELL = "gemma3:1b"



class Raum:
    def __init__(self, name, beschreibung, dunkel=False, verschlossen=False):
        self.name = name
        self.beschreibung = beschreibung
        self.ausgaenge = {}
        self.gegenstaende = []
        self.dunkel = dunkel             
        self.verschlossen = verschlossen  


class Spieler:
    def __init__(self, name, raum):
        self.name = name
        self.raum = raum
        self.inventar = []
        self.schritte = 0

    def gehe(self, richtung):
        if richtung not in self.raum.ausgaenge:
            return "In diese Richtung gibt es keinen Ausgang."

        ziel = self.raum.ausgaenge[richtung]

        if ziel.verschlossen:
            if "schlüssel" in self.inventar:
                ziel.verschlossen = False
                self.raum = ziel
                self.schritte += 1
                return "Du schließt die Tür mit dem Schlüssel auf. Knarr..."
            return "Die Tür ist verschlossen. Du brauchst einen Schlüssel."

        self.raum = ziel
        self.schritte += 1
        return f"Du gehst nach {richtung}."

    def nimm(self, gegenstand):
        if self.raum.dunkel and "kerze" not in self.inventar:
            return "Es ist zu dunkel, du findest nichts."
        if gegenstand in self.raum.gegenstaende:
            self.raum.gegenstaende.remove(gegenstand)
            self.inventar.append(gegenstand)
            return f"Du nimmst: {gegenstand}."
        return "Das gibt es hier nicht."






class Charakter:
    def __init__(self, name, raum, art, saetze, wissen="", wunsch=None, belohnung=None, dank=""):
        self.name = name
        self.raum = raum
        self.art = art
        self.saetze = saetze
        self.wunsch = wunsch
        self.belohnung = belohnung
        self.dank = dank
        self.zufrieden = False

        # Regeln für die KI (system prompt)
        regeln = (
            f"Du bist {self.name} in einem deutschen Textadventure 'Das Haus des Magiers'. "
            f"Du bist {self.art}. Du befindest dich im Raum '{self.raum.name}'. "
            "Du sprichst mit der Spielerin Ada. "
            "Antworte immer auf Deutsch, in 1 bis 3 kurzen Sätzen, und bleib in deiner Rolle. "
            "Im Haus gibt es nur diese Räume: Wohnzimmer, Flur, Küche, Garten, Keller und ein Geheimzimmer. "
            "Erfinde keine anderen Räume und keine anderen Gegenstände. Du darfst nicht lügen. "
            f"Typische Sätze von dir sind: {' / '.join(self.saetze)} "
            f"{wissen}"
        )
        if self.wunsch:
            regeln += (f"Du wünschst dir sehr: {self.wunsch}. "
                       "Wenn Ada es dir bringt, bist du dankbar. ")
        self.verlauf = [{"role": "system", "content": regeln}]
        self.chat = []   # nur für die Anzeige auf der Webseite: (wer, text)

    def sprich(self, spieler):
        if self.raum is not spieler.raum:
            return f"{self.name} ist nicht hier."


        if self.wunsch and not self.zufrieden and self.wunsch in spieler.inventar:
            spieler.inventar.remove(self.wunsch)
            self.zufrieden = True
            text = f"{self.name}: {self.dank}"
            if self.belohnung:
                spieler.inventar.append(self.belohnung)
                text += f" (Du bekommst: {self.belohnung})"
            # Die KI soll wissen, dass der Wunsch erfüllt ist
            self.verlauf.append({"role": "system", "content":
                                 f"Ada hat dir {self.wunsch} gegeben. Dein Wunsch ist erfüllt, du bist glücklich."})
            return text

        if self.zufrieden:
            return f"{self.name}: Danke nochmal, {spieler.name}!"

        return f"{self.name}: {random.choice(self.saetze)}"

    def frage(self, spieler, frage):
        """Spieler stellt eine Frage, die KI (Ollama) antwortet als dieser Charakter."""
        if self.raum is not spieler.raum:
            return f"{self.name} ist nicht hier."

        nachrichten = self.verlauf + [{"role": "user", "content": frage}]
        try:
            antwort = ollama.chat(model=MODELL, messages=nachrichten)
            text = antwort.message.content.strip()
        except Exception as fehler:
            print("Ollama-Fehler:", fehler)
            text = random.choice(self.saetze) + " (KI nicht erreichbar)"

        self.verlauf = nachrichten + [{"role": "assistant", "content": text}]
        self.chat.append((spieler.name, frage))
        self.chat.append((self.name, text))
        return f"{self.name}: {text}"






def neues_spiel():
    global spieler, figuren, schatz_raum

    wohnzimmer = Raum("Wohnzimmer", "Ein alter Sessel steht vor dem Kamin. Das Feuer knistert.")
    flur = Raum("Flur", "Ein langer, dunkler Flur. Bilder schauen dich an.")
    kueche = Raum("Küche", "Es riecht nach Suppe. Töpfe klappern.")
    garten = Raum("Garten", "Nasses Gras, ein alter Brunnen und viele Blumen.")
    keller = Raum("Keller", "Kalt und feucht. Irgendwo tropft Wasser.", dunkel=True)
    schatz_raum = Raum("Geheimzimmer", "Überall glänzt Gold! Du hast den Schatz gefunden!",
                       verschlossen=True)

    wohnzimmer.ausgaenge["norden"] = flur
    flur.ausgaenge["süden"] = wohnzimmer
    flur.ausgaenge["osten"] = kueche
    kueche.ausgaenge["westen"] = flur
    flur.ausgaenge["norden"] = garten
    garten.ausgaenge["süden"] = flur
    kueche.ausgaenge["unten"] = keller
    keller.ausgaenge["oben"] = kueche
    wohnzimmer.ausgaenge["geheimtür"] = schatz_raum
    schatz_raum.ausgaenge["zurück"] = wohnzimmer

    kueche.gegenstaende.append("kerze")
    keller.gegenstaende.append("hut")
    garten.gegenstaende.append("blume")

    spieler = Spieler("Ada", flur)

    magier = Charakter("Gandalf", wohnzimmer, "weise und vergesslich",
                       ["Ich grüße dich! Hast du meinen Hut gesehen?",
                        "Ohne Hut kann ich nicht zaubern.",
                        "Im Keller war ich lange nicht mehr... vielleicht dort?"],
                       wissen=("Dein Hut liegt im Keller, aber du hast es vergessen und erinnerst dich nur langsam. "
                               "Für den Hut gibst du den Schlüssel für die Geheimtür im Wohnzimmer. "
                               "Verrate das mit dem Schlüssel erst, wenn Ada nett fragt. "),
                       wunsch="hut", belohnung="schlüssel",
                       dank="Mein Hut! Hier, nimm diesen Schlüssel. Die Geheimtür wartet!")

    koechin = Charakter("Berta", kueche, "laut und ungeduldig",
                        ["Raus aus meiner Küche!",
                         "Willst du Suppe? Nein? Dann geh!",
                         "Im Keller ist es stockdunkel. Nimm die Kerze mit!"],
                        wissen=("Du bist die Köchin. In deiner Küche liegt eine Kerze. "
                                "Der Keller ist unter der Küche und stockdunkel. Du liebst Blumen aus dem Garten. "),
                        wunsch="blume",
                        dank="Oh, eine Blume für mich? Du bist ja süß!")

    katze = Charakter("Minka", garten, "faul und frech",
                      ["Miau.", "Mrrrr... *gähn*", "Miau! (Sie schaut zur Küche.)"],
                      wissen=("Du bist eine Katze und kannst NICHT sprechen. Antworte nur mit Miau, Schnurren "
                              "und kurzen Beschreibungen in Klammern, was du tust. Manchmal schaust du Richtung Küche. "))

    figuren = {"gandalf": magier, "berta": koechin, "minka": katze}


neues_spiel()





app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def spiel():
    nachricht = ""

    if request.method == "POST":
        aktion = request.form.get("aktion", "")
        if aktion == "neu":
            neues_spiel()
            nachricht = "Neues Spiel gestartet!"
        elif aktion.startswith("reden_"):
            nachricht = figuren[aktion[6:]].sprich(spieler)
        elif aktion.startswith("frage_"):
            frage = request.form.get("frage", "").strip()
            if frage:
                nachricht = figuren[aktion[6:]].frage(spieler, frage)
        elif aktion.startswith("nimm_"):
            nachricht = spieler.nimm(aktion[5:])
        else:
            nachricht = spieler.gehe(aktion)

    raum = spieler.raum
    sieht_nichts = raum.dunkel and "kerze" not in spieler.inventar
    hier = [key for key, f in figuren.items() if f.raum is raum]
    gewonnen = raum is schatz_raum

    return render_template("index.html",
                           raum=raum,
                           spieler=spieler,
                           hier=hier,
                           figuren=figuren,
                           nachricht=nachricht,
                           sieht_nichts=sieht_nichts,
                           gewonnen=gewonnen)


app.run(debug=True)
