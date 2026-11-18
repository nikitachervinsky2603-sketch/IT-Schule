# 🌐 Woche 3 – Flask Web-Apps

## 🧙 Das Haus des Magiers – Text-Adventure im Browser

| Tag | Ordner | Beschreibung |
|-----|--------|--------------|
| Tag 2 | [Tag-2_Text-Adventure-Flask](Tag-2_Text-Adventure-Flask) | Text-Adventure mit Räumen, Gegenständen, dunklen und verschlossenen Räumen und Charakteren – als Flask-Web-App |
| Tag 3 | [Tag-3_Text-Adventure-mit-KI-Ollama](Tag-3_Text-Adventure-mit-KI-Ollama) | Erweiterung: Charakteren kann man frei Fragen stellen – die Antworten kommen von einer lokalen KI (Ollama, Modell `gemma3:1b`) |

## ▶️ Starten

```bash
cd Tag-2_Text-Adventure-Flask
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Dann im Browser öffnen: <http://127.0.0.1:5000>

**Für Tag 3** zusätzlich [Ollama](https://ollama.com) installieren und das Modell laden:

```bash
ollama pull gemma3:1b
```

## 📁 Aufbau

```
main.py              # Spiel-Logik (Klassen Raum, Spieler, Charakter) + Flask-Route
templates/index.html # HTML-Oberfläche (Jinja2)
static/style.css     # Design
requirements.txt     # benötigte Pakete
```
