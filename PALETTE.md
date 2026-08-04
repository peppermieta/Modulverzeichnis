# Farbpalette

Basis-UI (Hintergrund, Fläche, Rahmen, Text) identisch zum Kalender-Projekt, plus eine eigene
Farbe pro Studienbereich – statt einer Farbe pro Modul, da 28 einzelne Modulfarben zu unruhig
gewirkt hätten. Details zur Zuordnung siehe [PLANUNG_Modulverzeichnis-v2.md](https://github.com/peppermieta/Kalender/blob/main/PLANUNG_Modulverzeichnis-v2.md) im Kalender-Repo.

![Website-Farbpalette](docs/website-palette.svg)

Der lila Akzent ("Akzent-Lila") wird für Links, Fokus-Zustände und das aktuelle Semester in der
Semesterauswahl verwendet und ist identisch mit der Farbe von Studienbereich 2.

## Formate zum Kopieren

Alle Werte auch als reine Textdatei verfügbar: [`docs/website-palette.txt`](docs/website-palette.txt) (CSV, Hex, Array, Object, Extended Array, XML).

- CSV

```
f7f6f3,ffffff,e2e0d8,1a1a18,7a7870,5b3fc8,2e8b57,1a8c70,c48a00,2050c8,cc6b3f,c41a50,777775
```

- With #

```
#f7f6f3, #ffffff, #e2e0d8, #1a1a18, #7a7870, #5b3fc8, #2e8b57, #1a8c70, #c48a00, #2050c8, #cc6b3f, #c41a50, #777775
```

- Object

```json
{"Hintergrund": "f7f6f3", "Flaeche": "ffffff", "Rahmen": "e2e0d8", "Text": "1a1a18", "Gedaempft": "7a7870", "Akzent-Lila / SB 2": "5b3fc8", "SB 1 - Grundlagen": "2e8b57", "SB 3 - Rahmenbed.": "1a8c70", "SB 4 - Bezugsdisz.": "c48a00", "SB 5 - Schluesselq.": "2050c8", "SB 6 - Handl.komp.": "cc6b3f", "SB 7 - Reflexion": "c41a50", "Ohne Zuordnung": "777775"}
```

Ausführlichere Formate (Array, Extended Array mit RGB/CMYK/HSB/HSL/Lab, XML) stehen in
[`docs/website-palette.txt`](docs/website-palette.txt).
