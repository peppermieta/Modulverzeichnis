# Farbpalette

Basis-UI (Hintergrund, Fläche, Rahmen, Text, Gedämpft) jeweils in einer Hell- und einer
Dark-Mode-Variante, plus eine eigene Akzentfarbe pro Studienbereich – statt einer Farbe pro
Modul, da 28 einzelne Modulfarben zu unruhig gewirkt hätten. Jeder Studienbereich hat dabei
im Dark Mode eine eigens abgestimmte dunkle Variante (nicht einfach invertiert), die hier aus
Übersichtsgründen nicht einzeln aufgeführt ist – siehe `build.py` für die exakten Werte.
Details zur Modul-Zuordnung siehe [PLANUNG_Modulverzeichnis-v2.md](https://github.com/peppermieta/Kalender/blob/main/PLANUNG_Modulverzeichnis-v2.md)
im Kalender-Repo.

![Website-Farbpalette](docs/website-palette.svg)

Der lila Akzent ("Akzent-Lila") wird für Links, Fokus-Zustände und das aktuelle Semester in
der Semesterauswahl verwendet und ist identisch mit der Farbe von Studienbereich 2. Die
Header-Leiste ganz oben (kurzer Disclaimer-Hinweis) nutzt bewusst "Pink Orchid" aus der
persönlichen Lieblingspalette statt einer der Studienbereichs- oder UI-Farben, um sich davon
optisch abzusetzen. Warnrot kommt einzig beim kurzen Aufblinken der Voraussetzungen zum
Einsatz, wenn ein Modul manuell auf "vorgemerkt" oder "offen" gesetzt wird.

## Formate zum Kopieren

Alle Werte auch als reine Textdatei verfügbar: [`docs/website-palette.txt`](docs/website-palette.txt) (CSV, Hex, Array, Object, Extended Array, XML).

- CSV

```
f7f6f3,ffffff,e2e0d8,1a1a18,7a7870,18171a,221f24,383540,edebe8,a6a29e,5b3fc8,a692f0,dfbbea,403f4c,362a3e,efd6f4,2e8b57,1a8c70,c48a00,2050c8,cc6b3f,c41a50,777775,dc2626
```

- With #

```
#f7f6f3, #ffffff, #e2e0d8, #1a1a18, #7a7870, #18171a, #221f24, #383540, #edebe8, #a6a29e, #5b3fc8, #a692f0, #dfbbea, #403f4c, #362a3e, #efd6f4, #2e8b57, #1a8c70, #c48a00, #2050c8, #cc6b3f, #c41a50, #777775, #dc2626
```

- Object

```json
{"Hintergrund": "f7f6f3", "Flaeche": "ffffff", "Rahmen": "e2e0d8", "Text": "1a1a18", "Gedaempft": "7a7870", "Hintergrund Dunkel": "18171a", "Flaeche Dunkel": "221f24", "Rahmen Dunkel": "383540", "Text Dunkel": "edebe8", "Gedaempft Dunkel": "a6a29e", "Akzent-Lila Hell / SB 2": "5b3fc8", "Akzent-Lila Dunkel": "a692f0", "Header Hell (Pink Orchid)": "dfbbea", "Header Hell-Text": "403f4c", "Header Dunkel": "362a3e", "Header Dunkel-Text": "efd6f4", "SB 1 - Grundlagen": "2e8b57", "SB 3 - Rahmenbed.": "1a8c70", "SB 4 - Bezugsdisz.": "c48a00", "SB 5 - Schluesselq.": "2050c8", "SB 6 - Handl.komp.": "cc6b3f", "SB 7 - Reflexion": "c41a50", "Ohne Zuordnung": "777775", "Warnrot (Voraussetzungen)": "dc2626"}
```

Ausführlichere Formate (Array, Extended Array mit RGB/CMYK/HSB/HSL/Lab, XML) stehen in
[`docs/website-palette.txt`](docs/website-palette.txt).
