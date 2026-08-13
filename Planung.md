# Modulverzeichnis – Planung

Offene technische Punkte, noch nicht umgesetzt.
*(Stand: 9. August 2026)*

> **Pflege-Hinweis, bewusst anders als bei der Kalender-Ideensammlung:**
> Erledigte Punkte werden hier nicht als "✅ Umgesetzt" markiert und
> stehen gelassen, sondern nach Umsetzung komplett aus der Datei entfernt.

## ♿ Barrierefreiheit (oberflächlicher Check, keine visuellen Änderungen)

- **Tastatur-Erreichbarkeit der Suchergebnisse** – die Suchtreffer
  (`.search-result`) sind aktuell `<div>`-Elemente, keine echten
  `<button>`/`<a>`-Elemente. Per Tastatur (Tab) daher nicht erreichbar,
  unabhängig von Fokus-Styling. Braucht eine kleine Strukturänderung
  (z. B. echte `<button>`-Elemente statt `<div>`s), bewusst noch nicht
  umgesetzt.
- **Kontrastprüfung – Ergebnis:** alle 8 Studienbereichsfarben liegen in
  Hell und Dunkel komfortabel über dem WCAG-AA-Mindestwert 4.5:1.
  Einzig `--muted` (gedämpfter Text, `#7A7870`) fällt im hellen Modus
  knapp durch: 4.09:1 auf dem Hintergrund, 4.42:1 auf weißen Flächen.
  Käme man mit ca. 10 % Abdunkelung (z. B. Richtung `#6D6C64`) locker
  über 4.5:1, optisch kaum wahrnehmbar – bewusst nicht ohne Rückfrage
  geändert.
- ~~Skip-Link~~ – bewusst verworfen, Nutzen bei einer eher kurzen Seite
  zu gering.

## 🔍 Code-Qualität & Sicherheit

- **`setTimeout` in `jumpToModule()` – nur Hinweis, keine Umsetzung
  geplant:** 150ms-Wartezeit vor dem Scrollen (Workaround für mobile
  Tastaturen) ist fehleranfällig, funktioniert aber bisher zuverlässig
  genug. Sauberere Alternative (`visualViewport`-Resize-Event) wäre
  aufwändiger und müsste gut getestet werden – erstmal so lassen, nur
  im Hinterkopf behalten.

---

## 🔭 Langfristige Themen

Weniger dringend, eher strategisch – kein akuter Zeitdruck.

- **Umzug auf eigene Domain (basamodule.info)** – langfristiges Ziel,
  weg von der aktuellen Subdomain unter der Kalender-Domain
  (`module.xn--peppermita-lnb.de`). Wichtig dabei: der Kalender
  verlinkt direkt auf die aktuelle Domain (Modul-Badges im
  Termin-Detail, Header-Link), das ist also kein rein internes
  Modulverzeichnis-Thema, sondern betrifft beide Projekte – bei
  Umsetzung müsste der Umzug in beiden Repos koordiniert erfolgen
  (CNAME, harte Links im Kalender-Code, README/PALETTE.md-Verweise).
- **Update-Konzept für neue Studienordnungen** – was passiert, wenn
  sich die Studienordnung ändert (neue/andere Module, andere
  CP-/SWS-Verteilung)? Bisher ungeklärt, ob die Seite einfach in-place
  aktualisiert wird oder ob es eine Art Versionierung je Jahrgang
  braucht, damit Studierende mit älterer Studienordnung weiterhin die
  für sie gültigen Angaben finden.
- **Anleitung/Vorlage für andere Studiengänge oder Jahrgänge** – hängt
  mit dem Punkt darüber zusammen. Eine Dokumentation, welche Dateien
  (`modules_data.py`, `build.py`, Farbpalette, Branding) für eine
  Übertragung auf einen anderen Studiengang oder Jahrgang angepasst
  werden müssten, damit das nicht bei jedem Mal neu durchdacht werden
  muss.

---

Wenn die Tastatur-Erreichbarkeit der Suche umgesetzt wird: ebenfalls
ohne sichtbare Änderung möglich.
