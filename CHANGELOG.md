# Changelog

Alle nennenswerten Änderungen an diesem Projekt werden hier dokumentiert.
Format angelehnt an [Keep a Changelog](https://keepachangelog.com/de/1.0.0/).

## [Unreleased]

_Noch keine offenen Änderungen._

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
