# Farbpalette

Basis-UI-Farben identisch zum Kalender-Projekt, plus eine eigene Farbe pro Studienbereich
(statt einer Farbe pro Modul, da 28 Module sonst zu unruhig gewirkt hätten).

## Basis-UI

| Name | Hex |
|---|---|
| Hintergrund | `#F7F6F3` |
| Fläche | `#FFFFFF` |
| Rahmen | `#E2E0D8` |
| Text | `#1A1A18` |
| Gedämpft | `#7A7870` |
| Akzent-Lila | `#5B3FC8` |

## Studienbereiche (7 + "ohne Zuordnung")

| Studienbereich | Farbe | Hex | Herkunft |
|---|---|---|---|
| 1 · Grundlagen der Sozialen Arbeit als Disziplin und Profession | Smaragdgrün | `#2E8B57` | vom Kalender übernommen (bisher M09) |
| 2 · Zielgruppen und Arbeitsfelder der Sozialen Arbeit | Lila | `#5B3FC8` | vom Kalender übernommen (bisher M07), identisch zum Akzent-Lila |
| 3 · Gesellschaftliche Rahmenbedingungen | Petrol/Grün | `#1A8C70` | vom Kalender übernommen (bisher M06) |
| 4 · Bezugsdisziplinen | Gold | `#C48A00` | vom Kalender übernommen (bisher M08) |
| 5 · Schlüsselqualifikationen | Blau | `#2050C8` | vom Kalender übernommen (bisher M02) |
| 6 · Sozialarbeiterische Handlungskompetenzen | Terrakotta | `#CC6B3F` | neu, da alle 6 bisherigen Kalenderfarben bereits anderen Bereichen zugeordnet waren |
| 7 · Reflexion und Evaluation der Sozialen Arbeit | Pink | `#C41A50` | vom Kalender übernommen (bisher M10) |
| Ohne spezifische Zuordnung (Modul 28) | Grau | `#777775` | vom Kalender übernommen (bisher ZA) |

Jede Farbe wird im selben Vierer-Set wie im Kalender verwendet: Hintergrund (pastellig), Text (dunkel),
Rahmen (mittlerer Ton), Punkt/Akzent (kräftig) – siehe `index.html`, Objekt `STUDIENBEREICHE`.

## Formate zum Kopieren

- CSV

```
F7F6F3,FFFFFF,E2E0D8,1A1A18,7A7870,5B3FC8,2E8B57,5B3FC8,1A8C70,C48A00,2050C8,CC6B3F,C41A50,777775
```

- With #

```
#F7F6F3, #FFFFFF, #E2E0D8, #1A1A18, #7A7870, #5B3FC8, #2E8B57, #5B3FC8, #1A8C70, #C48A00, #2050C8, #CC6B3F, #C41A50, #777775
```

Ausführliche Werte (RGB/CMYK/HSB/HSL/Lab) siehe [PALETTE.md im Kalender-Repo](https://github.com/peppermieta/Kalender/blob/main/PALETTE.md) – dieselbe Methodik, hier aus Aufwandsgründen nicht dupliziert.
