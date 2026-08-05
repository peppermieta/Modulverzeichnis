import sys, json
sys.path.insert(0, '/home/claude/modverz_v2')
from modules_data import MODULES, STUDIENBEREICHE

def esc(s):
    return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

# ─── JS-Datenobjekt bauen (fürs Client-seitige Rendering der Semesterauswahl) ─
js_modules = []
for m in MODULES:
    js_modules.append({
        "nr": m["nr"], "name": m["name"], "sem": m["sem"], "cp": m["cp"], "sws": m["sws"],
        "sb": m["sb"], "verantwortung": m["verantwortung"], "email": m.get("email"),
        "bausteine": m["bausteine"], "pruefung": m["pruefung"], "voraus": m["voraus"],
        "workload": m["workload"], "verwendbarkeit": m["verwendbarkeit"],
        "modulart": m.get("modulart"),
    })
js_sb = {str(k): v for k, v in STUDIENBEREICHE.items()}

MODULES_JSON = json.dumps(js_modules, ensure_ascii=False)
SB_JSON = json.dumps(js_sb, ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Modulverzeichnis – B.A. Soziale Arbeit</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0ODAgNDgwIj4KICA8Y2lyY2xlIGN4PSIyNDAiIGN5PSIyNDAiIHI9IjIyMCIgZmlsbD0iI2RmYmJlYSIvPgogIDxyZWN0IHg9IjE3NCIgeT0iMTU1IiB3aWR0aD0iMTYiIGhlaWdodD0iMzAiIHJ4PSI4IiBmaWxsPSIjNDAzZjRjIi8+CiAgPHJlY3QgeD0iMjkwIiB5PSIxNTUiIHdpZHRoPSIxNiIgaGVpZ2h0PSIzMCIgcng9IjgiIGZpbGw9IiM0MDNmNGMiLz4KICA8cmVjdCB4PSIxNjAiIHk9IjE3NSIgd2lkdGg9IjE2MCIgaGVpZ2h0PSIxNTAiIHJ4PSIyOCIgZmlsbD0iIzQwM2Y0YyIvPgogIDxyZWN0IHg9IjE4MCIgeT0iMTkyIiB3aWR0aD0iMTIwIiBoZWlnaHQ9IjEwIiByeD0iNSIgZmlsbD0iI2RmYmJlYSIvPgogIDxyZWN0IHg9IjE4NiIgeT0iMjIyIiB3aWR0aD0iMjgiIGhlaWdodD0iMjIiIHJ4PSI2IiBmaWxsPSIjZGZiYmVhIi8+CiAgPHJlY3QgeD0iMjI2IiB5PSIyMjIiIHdpZHRoPSIyOCIgaGVpZ2h0PSIyMiIgcng9IjYiIGZpbGw9IiNkZmJiZWEiLz4KICA8cmVjdCB4PSIyNjYiIHk9IjIyMiIgd2lkdGg9IjI4IiBoZWlnaHQ9IjIyIiByeD0iNiIgZmlsbD0iI2RmYmJlYSIvPgogIDxyZWN0IHg9IjE4NiIgeT0iMjU0IiB3aWR0aD0iMjgiIGhlaWdodD0iMjIiIHJ4PSI2IiBmaWxsPSIjZGZiYmVhIi8+CiAgPHJlY3QgeD0iMjI2IiB5PSIyNTQiIHdpZHRoPSIyOCIgaGVpZ2h0PSIyMiIgcng9IjYiIGZpbGw9IiNkZmJiZWEiLz4KICA8cmVjdCB4PSIyNjYiIHk9IjI1NCIgd2lkdGg9IjI4IiBoZWlnaHQ9IjIyIiByeD0iNiIgZmlsbD0iI2RmYmJlYSIvPgo8L3N2Zz4=">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {{
    --bg:       #F7F6F3;
    --surface:  #FFFFFF;
    --border:   #E2E0D8;
    --text:     #1A1A18;
    --muted:    #7A7870;
    --shadow:   0 2px 8px rgba(0,0,0,.07);
    --radius:   10px;
    --accent:   #5B3FC8;
    --header-h: 90px;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--text);
    font-family: 'Inter', sans-serif; -webkit-font-smoothing: antialiased;
  }}

  /* ── DISCLAIMER, oben: kurzer dezenter Hinweis ── */
  .disclaimer-mini {{
    background: #dfbbea; color: #403f4c;
    padding: 9px 24px; font-size: 12px; line-height: 1.5; text-align: center;
  }}
  .disclaimer-mini a {{ color: #403f4c; font-weight: 600; text-decoration: underline; }}

  header {{
    background: var(--surface); border-bottom: 1px solid var(--border);
    padding: 20px 24px; position: sticky; top: 0; z-index: 50;
    display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px;
  }}
  header h1 {{ font-size: 20px; font-weight: 700; margin: 0; letter-spacing: -.3px; }}
  header p {{ font-size: 13px; color: var(--muted); margin: 2px 0 0; }}

  .sem-select-wrap {{ display: flex; align-items: center; gap: 8px; font-size: 13px; }}
  .sem-select-wrap label {{ color: var(--muted); font-weight: 500; }}
  #semSelect {{
    font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 600; color: var(--accent);
    border: 1px solid var(--border); border-radius: 7px; padding: 7px 10px; background: var(--bg);
    cursor: pointer;
  }}

  .intro {{
    max-width: 1100px; margin: 0 auto; padding: 20px 24px 4px;
    font-size: 13.5px; color: var(--muted); line-height: 1.6;
  }}

  /* ── STUDIENVERLAUFSPLAN ── */
  .mv-plan {{ max-width: 1100px; margin: 16px auto 32px; padding: 0 24px; }}
  .mv-row {{ display: flex; align-items: flex-start; gap: 14px; padding: 12px 0; border-bottom: 1px solid var(--border); }}
  .mv-row:last-child {{ border-bottom: none; }}
  .mv-row-label {{ flex: 0 0 100px; display: flex; flex-direction: column; gap: 4px; padding-top: 6px; }}
  .mv-row-sem {{ font-weight: 700; font-size: 13.5px; }}
  .mv-row-status {{
    font-size: 10.5px; font-weight: 600; padding: 2px 7px; border-radius: 20px;
    width: fit-content; text-transform: uppercase; letter-spacing: .3px;
  }}
  .status-done {{ background: #EEEEEC; color: #777775; }}
  .status-current {{ background: var(--accent); color: #fff; }}
  .status-upcoming {{ background: var(--bg); color: var(--muted); border: 1px solid var(--border); }}
  .mv-row-cards {{ display: flex; flex-wrap: wrap; gap: 8px; flex: 1; }}
  .mv-card {{
    display: block; text-decoration: none; color: var(--text);
    background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
    padding: 8px 11px; min-width: 130px; max-width: 190px; transition: transform .1s, box-shadow .1s;
  }}
  .mv-card:hover {{ transform: translateY(-1px); box-shadow: var(--shadow); }}
  .mv-card-nr {{ font-family: 'JetBrains Mono', monospace; font-size: 10.5px; font-weight: 700; opacity: .7; }}
  .mv-card-name {{ font-size: 12px; font-weight: 600; line-height: 1.3; margin-top: 2px; }}
  .mv-card-span {{ font-size: 10px; opacity: .65; margin-top: 3px; }}
  .mv-card-done {{ opacity: .55; }}

  /* ── LEGENDE STUDIENBEREICHE ── */
  .sb-legend {{ display: flex; flex-wrap: wrap; gap: 7px; max-width: 1100px; margin: 0 auto; padding: 0 24px 8px; }}
  .sb-legend-item {{
    display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 500;
    padding: 4px 10px; border-radius: 20px; border: 1px solid;
  }}
  .sb-legend-dot {{ width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }}

  /* ── DETAILKARTEN ── */
  .mv-details {{ max-width: 1100px; margin: 0 auto 40px; padding: 0 24px; }}
  .mv-details > h2 {{ font-size: 15px; margin: 36px 0 14px; padding-top: 20px; border-top: 1px solid var(--border); }}
  .mv-details > h2:first-child {{ border-top: none; margin-top: 0; }}
  .mv-detail {{
    background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
    box-shadow: var(--shadow); padding: 18px 20px; margin-bottom: 14px; scroll-margin-top: var(--header-h);
  }}
  .mv-detail-head {{
    display: flex; justify-content: space-between; align-items: flex-start; gap: 14px; flex-wrap: wrap;
    border-bottom: 1px solid var(--border); padding-bottom: 12px; margin-bottom: 14px;
  }}
  .mv-detail-nr {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 700; color: var(--accent); }}
  .mv-detail-head h3 {{ font-size: 16px; margin: 2px 0 0; line-height: 1.35; }}
  .mv-detail-meta {{ font-size: 12px; color: var(--muted); white-space: nowrap; padding-top: 4px; }}
  .mv-sb-tag {{ display: inline-block; margin-top: 6px; font-size: 10px; font-weight: 700; border-radius: 20px; padding: 2px 9px; }}
  .mv-tag {{
    display: inline-block; margin-left: 6px; font-size: 10px; font-weight: 700;
    background: #FEF3E2; color: #7A5500; border: 1px solid #F5CC80; border-radius: 20px; padding: 1px 7px;
  }}
  .mv-detail-body {{ display: grid; grid-template-columns: 1.5fr 1fr; gap: 22px; }}
  .mv-label {{
    font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: .4px;
    color: var(--muted); margin-bottom: 8px;
  }}
  .mv-baustein {{ display: flex; align-items: center; gap: 8px; font-size: 12.5px; padding: 7px 0; border-bottom: 1px solid var(--border); }}
  .mv-baustein:last-child {{ border-bottom: none; }}
  .mv-baustein-name {{ flex: 1; }}
  .mv-baustein-art {{ font-size: 11px; color: var(--muted); white-space: nowrap; }}
  .mv-pl-badge {{ font-size: 10px; font-weight: 700; background: #FCE8EF; color: #7A1038; border-radius: 5px; padding: 1px 6px; white-space: nowrap; }}
  .mv-pruefung {{ font-size: 13px; font-weight: 600; }}
  .mv-pruefung-note {{ font-weight: 400; color: var(--muted); }}
  .mv-voraus {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .mv-voraus-chip {{ font-size: 11px; padding: 4px 9px; border-radius: 20px; background: var(--bg); border: 1px solid var(--border); color: var(--text); }}
  .mv-voraus-link {{ text-decoration: none; cursor: pointer; }}
  .mv-voraus-link:hover {{ border-color: var(--accent); color: var(--accent); }}
  .mv-voraus-none {{ font-size: 12px; color: var(--muted); font-style: italic; }}
  .mv-verantwortung {{ font-size: 13px; }}
  .mv-verantwortung > div {{ margin-bottom: 2px; }}
  .mv-mail-link {{ text-decoration: none; opacity: .7; }}
  .mv-mail-link:hover {{ opacity: 1; }}
  .mv-verantwortung.placeholder {{ color: var(--muted); font-style: italic; font-size: 12px; }}
  .mv-workload {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: 12px; }}
  .mv-workload-item {{ display: flex; flex-direction: column; }}
  .mv-workload-val {{ font-weight: 700; font-size: 14px; }}
  .mv-workload-label {{ color: var(--muted); font-size: 10.5px; }}
  .mv-verwendbarkeit {{ display: flex; flex-wrap: wrap; gap: 5px; }}
  .mv-verwendbarkeit-chip {{ font-size: 10.5px; padding: 3px 8px; border-radius: 20px; background: var(--bg); border: 1px solid var(--border); color: var(--muted); }}
  .mv-verwendbarkeit-none {{ font-size: 12px; color: var(--muted); font-style: italic; }}

  /* ── KONTAKT / FOOTER ── */
  .contact-section {{
    max-width: 1100px; margin: 0 auto 24px; padding: 18px 24px; background: var(--surface);
    border: 1px solid var(--border); border-radius: var(--radius); font-size: 13px; line-height: 1.6;
  }}
  .contact-section a {{ color: var(--accent); font-weight: 600; text-decoration: none; }}
  .contact-section a:hover {{ text-decoration: underline; }}

  footer {{
    max-width: 1100px; margin: 0 auto; padding: 20px 24px 40px; font-size: 11.5px;
    color: var(--muted); line-height: 1.7; border-top: 1px solid var(--border);
    scroll-margin-top: var(--header-h);
  }}
  footer a {{ color: var(--muted); }}
  footer:target {{ animation: footer-highlight 2.5s ease-out; }}
  @keyframes footer-highlight {{
    from {{ background: rgba(223, 187, 234, .35); }}
    to   {{ background: transparent; }}
  }}

  @media (max-width: 700px) {{
    header {{ padding: 14px 16px; }}
    .disclaimer-mini {{ padding: 9px 16px; }}
    .intro {{ padding: 14px 16px 4px; }}
    .mv-plan {{ padding: 0 16px; }}
    .sb-legend {{ padding: 0 16px 8px; }}
    .mv-row {{ flex-direction: column; gap: 8px; }}
    .mv-row-label {{ flex-direction: row; align-items: center; gap: 8px; }}
    .mv-details {{ padding: 0 16px; }}
    .mv-detail-body {{ grid-template-columns: 1fr; }}
    .mv-card {{ min-width: 0; max-width: none; flex: 1 1 45%; }}
    .contact-section {{ margin-left: 16px; margin-right: 16px; padding: 16px; }}
    footer {{ margin-left: 16px; margin-right: 16px; padding-left: 0; padding-right: 0; }}
  }}
</style>
</head>
<body>

<div class="disclaimer-mini">
  Inoffizielle Seite ·
  <a href="#disclaimer">mehr dazu</a>
</div>

<header>
  <div>
    <h1>Modulverzeichnis</h1>
    <p>Bachelor Soziale Arbeit · EH Ludwigsburg · alle 28 Module im Überblick ·
       <a href="https://kalender.xn--peppermita-lnb.de/" target="_blank" style="color:var(--accent);font-weight:600;text-decoration:none;">Vorlesungskalender ↗</a></p>
  </div>
  <div class="sem-select-wrap">
    <label for="semSelect">Mein aktuelles Semester:</label>
    <select id="semSelect">
      <option value="0">– auswählen –</option>
      <option value="1">1. Semester</option>
      <option value="2">2. Semester</option>
      <option value="3">3. Semester</option>
      <option value="4">4. Semester</option>
      <option value="5">5. Semester</option>
      <option value="6">6. Semester</option>
      <option value="7">7. Semester</option>
    </select>
  </div>
</header>

<div class="intro">
  Übersicht aller Module des Studiengangs mit Bausteinen, Modulprüfungen, Modulverantwortlichen,
  Workload-Aufteilung und Voraussetzungen. Wähle oben dein aktuelles Semester, um zu sehen, wie die
  Module aufeinander aufbauen.
</div>

<p style="max-width:1100px;margin:0 auto;padding:0 24px 6px;font-size:11.5px;color:var(--muted);">Farblegende der Studienbereiche:</p>
<div class="sb-legend" id="sbLegend"></div>

<div class="mv-plan" id="plan"></div>

<div class="mv-details" id="details"></div>

<div class="contact-section" id="kontakt">
  <strong>Fehler gefunden oder Feedback?</strong> Über Hinweise zu Fehlern oder Ergänzungen freuen wir uns:
  <a href="mailto:info@peppermięta.de">info@peppermięta.de</a>
</div>

<footer id="disclaimer">
  Diese inoffizielle, selbst erstellte Übersicht ist rechtlich nicht bindend. Alle Angaben wurden
  nach bestem Wissen übertragen, Fehler sind aber nicht ausgeschlossen – maßgeblich ist
  ausschließlich das offizielle
  <a href="https://www.eh-ludwigsburg.de/fileadmin/user_upload/Studium/Studienangebot/Bachelorstudiengaenge/Soziale_Arbeit/BA_Soziale_Arbeit_MHB_2025_Stand_03.2026.pdf" target="_blank">Modulhandbuch der EH Ludwigsburg</a>
  (Version 2025, Stand: 27.03.2026). Kontaktdaten der Modulverantwortlichen entnommen aus dem
  <a href="https://www.eh-ludwigsburg.de/hochschule/personenverzeichnis" target="_blank">Personenverzeichnis der EH Ludwigsburg</a>,
  alle übrigen Angaben aus dem verlinkten Modulhandbuch.<br>
  Der Quellcode dieser Seite ist unter der <strong>MIT-Lizenz</strong> frei nutzbar und veränderbar –
  Repository auf <a href="https://github.com/peppermieta/Modulverzeichnis" target="_blank">GitHub</a>.
  Die Inhalte (Modulhandbuch-Daten) gehören der EH Ludwigsburg und sind davon ausgenommen.
</footer>

<script>
const MODULES = {MODULES_JSON};
const STUDIENBEREICHE = {SB_JSON};
const CURRENT_KEY = 'mv_current_semester';

function esc(s) {{
  return String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}}

function renderLegend() {{
  const el = document.getElementById('sbLegend');
  el.innerHTML = Object.entries(STUDIENBEREICHE).filter(([k]) => k !== '0').map(([k, sb]) => `
    <span class="sb-legend-item" style="background:${{sb.bg}};color:${{sb.tx}};border-color:${{sb.bd}}">
      <span class="sb-legend-dot" style="background:${{sb.dot}}"></span>${{esc(sb.name)}}
    </span>`).join('');
}}

function moduleCardHtml(m, currentSem) {{
  const sb = STUDIENBEREICHE[m.sb];
  let cls = 'mv-card';
  let style = `style="background:${{sb.bg}};color:${{sb.tx}};border-color:${{sb.bd}}"`;
  if (currentSem && m.sem[0] < currentSem && !m.sem.includes(currentSem)) cls += ' mv-card-done';
  const span = m.sem.length > 1 ? `<div class="mv-card-span">${{m.sem[0]}}.–${{m.sem[m.sem.length-1]}}. Sem.</div>` : '';
  return `<a href="#modul-${{m.nr}}" class="${{cls}}" ${{style}}>
    <div class="mv-card-nr">M${{String(m.nr).padStart(2,'0')}}</div>
    <div class="mv-card-name">${{esc(m.name)}}</div>
    ${{span}}
  </a>`;
}}

function renderPlan(currentSem) {{
  const el = document.getElementById('plan');
  let html = '';
  for (let sem = 1; sem <= 7; sem++) {{
    const modsInSem = MODULES.filter(m => m.sem.includes(sem));
    let status, statusCls;
    if (!currentSem) {{ status = ''; statusCls = ''; }}
    else if (sem < currentSem) {{ status = 'abgeschlossen'; statusCls = 'status-done'; }}
    else if (sem === currentSem) {{ status = 'aktuelles Semester'; statusCls = 'status-current'; }}
    else {{ status = 'kommend'; statusCls = 'status-upcoming'; }}
    const statusHtml = status ? `<span class="mv-row-status ${{statusCls}}">${{status}}</span>` : '';
    html += `<div class="mv-row">
      <div class="mv-row-label"><span class="mv-row-sem">${{sem}}. Sem.</span>${{statusHtml}}</div>
      <div class="mv-row-cards">${{modsInSem.map(m => moduleCardHtml(m, currentSem)).join('')}}</div>
    </div>`;
  }}
  el.innerHTML = html;
}}

function baustein(b) {{
  const [name, art, pl] = b;
  const plHtml = pl ? `<span class="mv-pl-badge">${{pl}}</span>` : '';
  return `<div class="mv-baustein"><span class="mv-baustein-name">${{esc(name)}}</span><span class="mv-baustein-art">${{esc(art)}}</span>${{plHtml}}</div>`;
}}

function voraus(v) {{
  if (!v.length) return '<span class="mv-voraus-none">keine</span>';
  return v.map(x => {{
    if (typeof x === 'string') return `<span class="mv-voraus-chip">${{esc(x)}}</span>`;
    const target = MODULES.find(m => m.nr === x);
    return `<a href="#modul-${{x}}" class="mv-voraus-chip mv-voraus-link">M${{String(x).padStart(2,'0')}} – ${{esc(target.name)}}</a>`;
  }}).join(' ');
}}

function verwendbarkeit(v) {{
  if (!v.length) return '<span class="mv-verwendbarkeit-none">keine bekannte Verwendung in anderen Studiengängen</span>';
  return v.map(x => `<span class="mv-verwendbarkeit-chip">${{esc(x)}}</span>`).join('');
}}

function renderVerantwortung(names, emails) {{
  const nameList = names.split(' / ');
  const emailList = (emails || '').split(' / ');
  return '<div class="mv-verantwortung">' + nameList.map((name, i) => {{
    const email = emailList[i];
    const mail = email ? ` <a href="mailto:${{email}}" class="mv-mail-link" title="E-Mail an ${{esc(name)}}">✉</a>` : '';
    return `<div>${{esc(name)}}${{mail}}</div>`;
  }}).join('') + '</div>';
}}

function renderDetails() {{
  const el = document.getElementById('details');
  let html = '';
  let lastSem = null;
  for (const m of MODULES) {{
    const firstSem = m.sem[0];
    if (firstSem !== lastSem) {{ html += `<h2>${{firstSem}}. Semester</h2>`; lastSem = firstSem; }}
    const sb = STUDIENBEREICHE[m.sb];
    const semLabel = m.sem.length > 1 ? `${{m.sem[0]}}.–${{m.sem[m.sem.length-1]}}. Semester` : `${{m.sem[0]}}. Semester`;
    const [pnr, part, pben] = m.pruefung;
    const modart = m.modulart ? `<span class="mv-tag">${{esc(m.modulart)}}</span>` : '';
    const verantwortungHtml = m.verantwortung
      ? renderVerantwortung(m.verantwortung, m.email)
      : `<div class="mv-verantwortung placeholder">wird nachgetragen</div>`;
    const w = m.workload;
    html += `
    <div class="mv-detail" id="modul-${{m.nr}}">
      <div class="mv-detail-head">
        <div>
          <div class="mv-detail-nr">MODUL ${{String(m.nr).padStart(2,'0')}}</div>
          <h3>${{esc(m.name)}}</h3>
          <span class="mv-sb-tag" style="background:${{sb.bg}};color:${{sb.tx}}">${{esc(sb.name)}}</span>
        </div>
        <div class="mv-detail-meta">${{semLabel}} · ${{m.cp}} CP · ${{m.sws}} SWS ${{modart}}</div>
      </div>
      <div class="mv-detail-body">
        <div class="mv-col">
          <div class="mv-label">Bausteine</div>
          ${{m.bausteine.map(baustein).join('')}}
          <div class="mv-label" style="margin-top:16px;">Verwendbarkeit in anderen Studiengängen</div>
          <div class="mv-verwendbarkeit">${{verwendbarkeit(m.verwendbarkeit)}}</div>
        </div>
        <div class="mv-col mv-col-side">
          <div class="mv-label">Modulverantwortung</div>
          ${{verantwortungHtml}}
          <div class="mv-label" style="margin-top:14px;">Modulprüfung</div>
          <div class="mv-pruefung">${{esc(pnr)}} · ${{esc(part)}} <span class="mv-pruefung-note">(${{esc(pben)}})</span></div>
          <div class="mv-label" style="margin-top:14px;">Workload</div>
          <div class="mv-workload">
            <div class="mv-workload-item"><span class="mv-workload-val">${{w.gesamt}} h</span><span class="mv-workload-label">Gesamt</span></div>
            <div class="mv-workload-item"><span class="mv-workload-val">${{w.kontakt}} h</span><span class="mv-workload-label">Kontaktzeit</span></div>
            <div class="mv-workload-item"><span class="mv-workload-val">${{w.selbst}} h</span><span class="mv-workload-label">Selbststudium</span></div>
            ${{w.praxis ? `<div class="mv-workload-item"><span class="mv-workload-val">${{w.praxis}} h</span><span class="mv-workload-label">Praxis</span></div>` : ''}}
          </div>
          <div class="mv-label" style="margin-top:14px;">Voraussetzungen</div>
          <div class="mv-voraus">${{voraus(m.voraus)}}</div>
        </div>
      </div>
    </div>`;
  }}
  el.innerHTML = html;
}}

function applySemester(sem) {{
  renderPlan(sem || null);
  if (sem) localStorage.setItem(CURRENT_KEY, sem);
  else localStorage.removeItem(CURRENT_KEY);
}}

document.getElementById('semSelect').addEventListener('change', e => {{
  applySemester(Number(e.target.value) || null);
}});

// Init
renderLegend();
renderDetails();
const saved = Number(localStorage.getItem(CURRENT_KEY)) || null;
if (saved) document.getElementById('semSelect').value = String(saved);
applySemester(saved);

// ── Header-Höhe dynamisch messen (variiert je nach Viewport-Breite, da das
//    Semester-Dropdown auf schmalen Bildschirmen umbricht) und als
//    scroll-margin-top für die Modulkarten nutzen, statt eines festen Werts.
const headerEl = document.querySelector('header');
function updateHeaderHeight() {{
  const h = Math.ceil(headerEl.getBoundingClientRect().height) + 14;
  document.documentElement.style.setProperty('--header-h', h + 'px');
}}
updateHeaderHeight();
if ('ResizeObserver' in window) {{
  new ResizeObserver(updateHeaderHeight).observe(headerEl);
}} else {{
  window.addEventListener('resize', updateHeaderHeight);
}}
// Falls die Seite direkt mit einem #modul-Anker geöffnet wurde, könnte der
// Browser schon vor der Höhenmessung gescrollt haben – einmal korrigieren.
if (location.hash) {{
  const target = document.querySelector(location.hash);
  if (target) requestAnimationFrame(() => target.scrollIntoView({{block: 'start'}}));
}}
</script>
</body>
</html>
'''

with open('/home/claude/modverz_v2/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fertig:", len(html), "Zeichen")
