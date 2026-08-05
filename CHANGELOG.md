# Changelog

Alle nennenswerten Änderungen an diesem Projekt werden hier dokumentiert.
Format angelehnt an [Keep a Changelog](https://keepachangelog.com/de/1.0.0/).

## [1.6.0] - 2026-08-05

### Added
- **Suchfunktion**: Suchfeld unter dem Intro-Text, durchsucht Modulname,
  Modulnummer (z. B. "M07" oder "7") und Modulverantwortliche live während
  der Eingabe. Dropdown mit bis zu 8 Treffern (Nummer, Name, Studienbereich),
  Klick springt zum passenden Modul.
- **Ankunfts-Hervorhebung bei Modulkarten**: Jede Detailkarte blendet beim
  Ansteuern per Anker (Suche, Voraussetzungs-Verlinkung oder direkter Link)
  kurz einen Akzent-Rahmen ein und wieder aus (`:target`, gleiches Muster
  wie das Footer-Highlight) – macht sichtbar, welche Karte gemeint ist,
  statt dass man sie erst suchen muss.

## [1.5.0] - 2026-08-05

### Added
- **Dark Mode**: Schalter links neben der Semesterauswahl im Header, schaltet
  das komplette Farbschema um (inkl. aller 8 Studienbereichs-Farben mit
  eigens abgestimmten Dunkel-Varianten statt reiner Invertierung, Disclaimer-
  Leiste, Wahlpflicht-/PL-Badges, Semester-Status-Pills). Einstellung wird in
  `localStorage` gespeichert und bleibt über Besuche hinweg erhalten; ein
  kleines Inline-Script ganz am Anfang von `<head>` verhindert das Aufblitzen
  des hellen Modus beim Laden. `color-scheme` wird mitgesetzt, damit auch
  native Elemente (Semester-Dropdown, Scrollbar) dunkel gerendert werden.

## [1.4.1] - 2026-08-05

### Added
- **Footer-Highlight beim Sprung von "mehr dazu"**: Per CSS `:target` blendet
  der Footer kurz in Pink Orchid ein und wieder aus (2,5s, keine JS nötig).
  Löst das Problem, dass man nach dem Sprung durch die große Modul-28-Karte
  direkt darüber nicht erkannt hat, dass der (kleingedruckte) Footer das
  eigentliche Ziel ist.

### Changed
- Kontakt-Box: Satz "Über Hinweise zu Fehlern oder Ergänzungen freuen wir
  uns" wieder ergänzt (bei der letzten Umstrukturierung gekürzt worden,
  auf Wunsch zurückgeholt).
- Footer: Hinweis "Alle Angaben wurden nach bestem Wissen übertragen,
  Fehler sind aber nicht ausgeschlossen" wieder ergänzt (ebenfalls bei der
  letzten Umstrukturierung gestrichen worden, auf Wunsch zurückgeholt).

## [1.4.0] - 2026-08-05

### Changed
- **Disclaimer/Kontakt/Footer grundlegend neu strukturiert** (nach ausführlicher
  Abstimmung, statt der bisherigen schrittweisen Einzeländerungen): Jede der
  6 Meta-Infos (Status, Datenquelle+Version, Kontaktdaten-Quelle, Feedback,
  Lizenz, Rechte an den Inhalten) steht jetzt an genau einer Stelle.
  - Obere Leiste: nur noch "Inoffizielle Seite · mehr dazu" (kein separater
    Kontakt-Link mehr oben).
  - Die bisherige `.disclaimer-full`-Box entfällt komplett, ihr Inhalt ist
    jetzt Teil des Footers (dort standen ohnehin schon Lizenz/Rechte-Angaben).
  - Kontakt-Box enthält nur noch die eigentliche Aufforderung ("Fehler
    gefunden oder Feedback?" + E-Mail), keine Quellenangaben mehr.
  - Footer bündelt jetzt alle Quellen-/Rechte-Angaben (Modulhandbuch-Version,
    Personenverzeichnis, MIT-Lizenz, Datenrechte) und ist zugleich das
    Sprungziel für "mehr dazu" oben.
  - Kleinere sprachliche Dopplung behoben ("Modulhandbuch der EH Ludwigsburg
    (Modulhandbuch 2025 ...)" → "... (Version 2025 ...)").
  - Tote CSS-Regel für die längst ersetzte alte `.disclaimer`-Klasse entfernt.

## [1.3.2] - 2026-08-05

### Changed
- Intro-Text: Verlinkung/Erwähnung des Modulhandbuchs entfernt (redundant,
  steht bereits im Disclaimer oben und unten).
- Untere Disclaimer-Box: Modulhandbuch-Version/Stand ("Modulhandbuch 2025,
  Stand: 27.03.2026") als reiner Text ergänzt (ohne eigenen Link, der
  bestehende Link auf das Handbuch bleibt unverändert).
- Obere Mini-Disclaimer-Leiste farblich hervorgehoben: Hintergrund jetzt
  Pink Orchid (`#dfbbea`) mit Gunmetal-Text (`#403f4c`), beides aus der
  bevorzugten Farbpalette.

## [1.3.1] - 2026-08-05

### Changed
- **Disclaimer/Kontakt/Footer nochmal geschärft**: Oberer Hinweis jetzt ein
  echter Kurztext (Studiengang, Modulhandbuch-Version 2025, Stand
  27.03.2026) mit Sprunglink zur ausführlichen Box unten statt eigenem
  Handbuch-Link. Quellenangabe zu den Modulverantwortlichen-Kontaktdaten
  aus dem Footer in die Kontakt-Box verschoben (thematisch passender).
  "Diese Seite wird ehrenamtlich von Studierenden für Studierende
  gepflegt." aus der Kontakt-Box entfernt. Verweis "siehe Disclaimer oben"
  im Footer entfernt (nicht mehr nötig, da die Lizenzangabe jetzt für sich
  steht).

## [1.3.0] - 2026-08-05

### Fixed
- **Mobiler Anker-Sprung zu Modulen** (`#modul-N`): Auf schmalen Viewports
  bricht das Semester-Dropdown im Header in eine zweite Zeile um, wodurch
  der Header deutlich höher wird (bis zu 131px statt 81px am Desktop). Der
  bisher feste `scroll-margin-top: 90px` war dafür nicht ausreichend, sodass
  der Header den oberen Teil der Zielkarte verdeckte. Jetzt wird die
  tatsächliche Header-Höhe per `ResizeObserver` laufend gemessen und als
  CSS-Variable `--header-h` gesetzt – inkl. Korrektur-Scroll beim direkten
  Öffnen eines Anker-Links, bevor die Messung greift.
- **Feedback-Box auf Mobil**: Der horizontale Innenabstand wurde durch eine
  fehlerhafte Media-Query-Regel auf 0 gesetzt, wodurch der Text direkt am
  Kartenrand klebte. Jetzt konsistentes Padding wie am Desktop.

### Changed
- **Disclaimer neu aufgeteilt**: Oben nur noch ein kurzer, dezenter Hinweis
  (kein grelles Gelb mehr, sondern dezente Farben passend zum restlichen
  Seitendesign) mit Links zu Handbuch und Kontakt. Der ausführliche Text
  steht jetzt unten direkt vor der Kontakt-Box.

## [1.2.1] - 2026-08-04

### Fixed
- README: Tech-Stack nannte fälschlich nur Inter als Schriftart – JetBrains
  Mono (für die Modul-Nummern-Badges) wird ebenfalls verwendet, genau wie
  im Kalender-Repo. Korrigiert.

### Changed
- README: Farbpalette wird jetzt wie im Kalender-Repo direkt als Swatch-Bild
  eingebettet (`docs/website-palette.svg`) statt nur auf PALETTE.md zu
  verweisen.
- Intro-Text: Satz mit dem Link zum Vorlesungskalender entfernt (der
  eigenständige Link im Header oben bleibt bestehen) – wie zuvor
  vereinbart, jetzt gebündelt mit dieser Änderung umgesetzt.

## [1.2.0] - 2026-08-04

### Added
- **Modulverantwortliche mit E-Mail-Adressen**: alle 19 zugehörigen Kontakte
  aus dem [Personenverzeichnis der EH Ludwigsburg](https://www.eh-ludwigsburg.de/hochschule/personenverzeichnis)
  recherchiert und als klickbares Mail-Symbol neben jedem Namen ergänzt
  (bei mehreren Verantwortlichen pro Modul jeweils einzeln verlinkt).
  Quelle im Footer vermerkt.
- **Farbpalette wie im Kalender-Repo**: `docs/website-palette.svg` (visueller
  Swatch, 13 Farben: Basis-UI + 8 Studienbereichsfarben) und
  `docs/website-palette.txt` (CSV, Hex, Array, Object, Extended Array mit
  RGB/CMYK/HSB/HSL/Lab, XML) ergänzt, `PALETTE.md` entsprechend neu
  strukturiert.

### Changed
- Studiengangsleitung (Modul 28) mit der Mail-Adresse des aktuellen
  Studiengangsleiters (Prof. Dr. Rolf Ahlrichs) verknüpft.

## [1.1.1] - 2026-08-04

### Changed
- Favicon von generischem Lila-Punkt auf das eigentliche Kalender-Logo
  umgestellt (Pink-Orchid-Kreis mit Gunmetal-Kalender-Icon), passend zur
  "Textmarker og"-Palette und identisch zum Kalender-App-Icon.
- Hinweis auf die installierbare Android-App aus dem Intro-Text entfernt
  (nicht relevant hier, da rein privates Kalender-Feature) – die Verlinkung
  zum Vorlesungskalender selbst bleibt bestehen.

## [1.1.0] - 2026-08-04

### Added
- Link zum offiziellen PDF-Modulhandbuch der EH Ludwigsburg (extern verlinkt,
  nicht selbst gehostet – Original bleibt bei der Hochschule)
- Hinweis "Farblegende der Studienbereiche" direkt über der Farblegende
- Verlinkung zum Vorlesungskalender (inkl. Hinweis auf die installierbare
  Android-App) im Header und im Intro-Text
- Modulverantwortung für Modul 19 (Praxissemester) nachgetragen: Beatrice
  Gerst (im Original-Handbuch gefunden, Platzhalter "wird nachgetragen"
  entfernt)

### Changed
- Disclaimer-Symbol (⚠️) entfernt, Text bleibt inhaltlich gleich

## [1.0.0] - 2026-08-04

### Added
- Erste vollständige Version des eigenständigen Modulverzeichnisses, losgelöst
  vom privaten Kalender-Repo (dort bisher nur `module.html` mit 6 Modulen,
  fester Vorauswahl 2. Semester, ohne Modulverantwortliche).
- Alle 28 Module des Studiengangs mit vollständigen Daten aus dem
  Modulhandbuch (Stand 03/2026): Bausteine (inkl. PL/UPL), Modulprüfung,
  Modulverantwortung, Workload-Aufteilung (Kontaktzeit/Selbststudium/Praxis),
  Verwendbarkeit in anderen B.A.-Studiengängen, Voraussetzungen.
- Studienverlaufsplan-Grafik: alle Module nach den 7 offiziellen
  Studienbereichen eingefärbt (statt nur 6 Modulfarben wie zuvor) –
  Farbzuordnung dokumentiert in [PALETTE.md](PALETTE.md).
- Interaktive Semesterauswahl (JavaScript): eigenes aktuelles Semester
  wählen, Module färben sich dynamisch nach "abgeschlossen / aktuell /
  kommend"; Auswahl wird lokal im Browser gespeichert (localStorage), kein
  Server, kein Account.
- Voraussetzungen als klickbare Querverweise zwischen Modulen.
- Prominenter Disclaimer am Seitenanfang (inoffizielle Übersicht, keine
  Rechtsverbindlichkeit).
- Kontaktabschnitt für Korrekturen/Feedback (E-Mail-Platzhalter
  `info@peppermięta.de`).
- Footer mit Hinweis auf MIT-Lizenz des Codes und GitHub-Repository.
- `modules_data.py` + `build.py`: Moduldaten und generierte Seite getrennt,
  damit Daten zentral gepflegt werden können, ohne direkt in HTML zu
  editieren.
- README.md, CHANGELOG.md, PALETTE.md, LICENSE (MIT) ergänzt.

### Known Issues
- Modulverantwortung für Modul 19 (Praxissemester) ist im Handbuch nicht
  eindeutig einer Einzelperson zugeordnet – zeigt aktuell Platzhalter
  "wird nachgetragen".
