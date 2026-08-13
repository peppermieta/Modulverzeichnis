# Modulverzeichnis – Planung

Offene technische Punkte, noch nicht umgesetzt.
*(Stand: 9. August 2026)*

> **Pflege-Hinweis, bewusst anders als bei der Kalender-Ideensammlung:**
> Erledigte Punkte werden hier nicht als "✅ Umgesetzt" markiert und
> stehen gelassen, sondern nach Umsetzung komplett aus der Datei entfernt.

## ♿ Barrierefreiheit (oberflächlicher Check, keine visuellen Änderungen)

Basiert auf einem extern erstellten Barrierefreiheits-Bericht, gemeinsam
durchgegangen und geschärft. Ziel bewusst nur unsichtbare Verbesserungen
(ARIA, Tastatur, Fokus) – am sichtbaren Erscheinungsbild der Seite soll
sich nichts bis möglichst wenig ändern.

- **Suchfeld-Label** – `<input id="searchInput">` hat nur einen
  Placeholder, kein semantisches Label. `aria-label="Modul suchen"`
  ergänzen, Suchicon (`🔍`) mit `aria-hidden="true"` vor Screenreadern
  verstecken.
- **Status-Dropdown-Labels** – der Text "Mein Status:" steht lose in
  einem `<div>`, nicht mit dem zugehörigen `<select>` verknüpft.
  Entweder echtes `<label for="…">` oder `aria-label` direkt am
  `<select>`.
- **Merkliste-Toggle-Zustand** – Button `#merklisteToggle` zeigt seinen
  An/Aus-Zustand nur visuell über `.active`. `aria-pressed="true"/
  "false"` per JS mitführen.
- **Symbole/Badges mit Alternativtext** – ★/✓/○ sowie das Mail-Icon
  (`✉`) werden von Screenreadern oft unsinnig vorgelesen. Symbole per
  `aria-hidden="true"` verstecken, stattdessen sinnvollen Text/
  `aria-label` am umschließenden Element anbieten. Aufwändigster Punkt
  der Liste, da mehrere Einzelstellen betroffen sind. (Das
  Kalender-Logo-SVG im Untertitel wurde ebenfalls geprüft – hat bereits
  ein korrektes `aria-label`, hier ist nichts zu tun.)
- **Live-Suche ankündigen** – `#searchResults` bekommt
  `aria-live="polite"`, damit Screenreader über neue Trefferlisten
  informiert werden. Dabei Geschwätzigkeit vermeiden: kurze Verzögerung
  einbauen, bevor vorgelesen wird, statt bei jedem Tastendruck neu
  anzukündigen.
- **Fokus-Sichtbarkeit** – bisher nur beim Suchfeld ein expliziter
  Fokus-Zustand definiert, sonst Browser-Standard (im Dark Mode ggf.
  schlecht sichtbar). Globale `:focus-visible`-Regel ergänzen (Rahmen
  in `var(--accent)`, etwas `outline-offset`). **Vorher:** kurzer
  Tastatur-Erreichbarkeits-Check – falls irgendwo klickbare `<div>`s
  statt echter `<button>`/`<a>`-Elemente verwendet werden, helfen
  Fokus-Styles allein nichts.
- **Kontrastprüfung** – reiner Check gegen WCAG-AA-Mindestkontrast
  (4.5:1 für normalen Text), keine Garantie für eine Code-Änderung.
  Falls etwas durchfällt: erst melden, keine Farbe ohne Rückfrage
  ändern.
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

Wenn wir Barrierefreiheit + Code-Qualität gemeinsam umsetzen: alles
dort oben ohne sichtbare Änderung möglich, bis auf die Kontrastprüfung
(dort ggf. Rückfrage vor einer Farbänderung).
