# Modulverzeichnis – Planung

Offene technische Punkte, noch nicht umgesetzt.
*(Stand: 9. August 2026)*

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

Basiert auf einem extern erstellten Code-Review, gegen den echten Code
verifiziert.

- **`esc()`-Funktion um Anführungszeichen ergänzen** – escaped bisher
  nur `&`/`<`/`>`, nicht `"`/`'`. Betrifft u. a. den generierten
  Mail-Link-Titel. Geprüft: die zwei anderen Stellen ohne `esc()`
  (Status-Badge, PL/UPL-Badge) sind ungefährlich, da die Werte nur aus
  festen `<select>`-Optionen bzw. fest hinterlegten Strings stammen –
  trotzdem sinnvoll, die Funktion selbst konsistent zu machen.
- **`location.hash`-Absturzschutz** –
  `document.querySelector(location.hash)` am Skript-Ende wirft bei
  ungültigem Hash (z. B. manuell verändertem Link) einen Fehler. Auf
  `getElementById` mit entfernter Raute umstellen (kein Try/Catch
  nötig, gibt bei Fehlschlag einfach `null` zurück).
- **DOM-Elemente in `renderCPProgress()` cachen** –
  `cpRingFillHeader`/`cpRingPctHeader` werden bei jedem Aufruf neu
  gesucht, obwohl sie statisch im Header liegen. Einmalig als
  Konstanten zwischenspeichern (wie `searchInput`).
- **`rel="noopener"` bei externen Links** – vier
  `target="_blank"`-Links (Kalender-Icon, Modulhandbuch-PDF,
  Personenverzeichnis, GitHub) haben kein `rel="noopener"`. Übliche
  Absicherung gegen Zugriff der geöffneten Seite auf den ursprünglichen
  Tab (`window.opener`); bei diesen vier Zielen unkritisch, aber
  günstig mitzunehmen.
- **`setTimeout` in `jumpToModule()` – nur Hinweis, keine Umsetzung
  geplant:** 150ms-Wartezeit vor dem Scrollen (Workaround für mobile
  Tastaturen) ist fehleranfällig, funktioniert aber bisher zuverlässig
  genug. Sauberere Alternative (`visualViewport`-Resize-Event) wäre
  aufwändiger und müsste gut getestet werden – erstmal so lassen, nur
  im Hinterkopf behalten.

---

Wenn wir beides gemeinsam umsetzen: alles oben ohne sichtbare Änderung
möglich, bis auf die Kontrastprüfung (dort ggf. Rückfrage vor einer
Farbänderung).
