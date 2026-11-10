"""
Build clean, polished, editorial-grade glacier SVGs for Faris Ruknuddin (@ZephyrusZorro).
Highlights: Full-Stack, Backend, and AI/ML.
Featured Build: Shelfday.
Selected Projects: Cueproof, TarkAI, Vaani Clinical, NephroGuard.
Embeds Faris's uploaded studio photo into identity.svg.
"""
import base64
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def write_svg(filename, content):
    dest = ASSETS / filename
    dest.write_text(content.strip(), encoding="utf-8")
    print(f"Generated {dest.relative_to(ROOT)} ({len(content)} bytes)")


def get_photo_b64():
    photo_path = ROOT / "faris-profile.jpg"
    if photo_path.exists():
        with open(photo_path, "rb") as f:
            return base64.b64encode(f.read()).decode("ascii")
    return ""


def generate_identity():
    b64 = get_photo_b64()

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 364" role="img">
<title>Faris Ruknuddin - Full-Stack &amp; Backend Software Engineer · Applied AI</title>
<defs>
  <linearGradient id="metal" x2="1" y2="1" gradientUnits="objectBoundingBox">
    <stop stop-color="#e7fbff"/>
    <stop offset=".34" stop-color="#a6e7ff"/>
    <stop offset=".52" stop-color="#a3a2ff"/>
    <stop offset=".81" stop-color="#524caa"/>
    <stop offset="1" stop-color="#c9afff"/>
  </linearGradient>
  <pattern id="mesh" width="16" height="16" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r=".9" fill="#495076"/>
  </pattern>
  <clipPath id="avatar-clip">
    <circle cx="805" cy="182" r="128"/>
  </clipPath>
</defs>
<style>
  .trace {{ stroke-dasharray: 60 620; animation: trace 6s linear infinite; }}
  @keyframes trace {{ to {{ stroke-dashoffset: -680; }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>

<!-- Outer Angled Glacier Chassis -->
<path fill="#12132a" d="M0 0H976l24 24v286l-54 54H0Z"/>
<path fill="url(#mesh)" d="M603 0h373l24 24v286l-54 54H603Z"/>

<!-- Circuit Accent Trace -->
<path d="M31 48h505l18-18h74M31 297h477l19 19h86" stroke="#50527d" fill="none"/>
<path class="trace" d="M31 48h505l18-18h74" stroke="#9edcff" fill="none" stroke-width="2"/>

<!-- Top & Bottom Monospace Tags -->
<g font-family="monospace" font-size="16" fill="#afcdff">
  <text x="32" y="33">@ZephyrusZorro</text>
  <text x="32" y="335">FULL-STACK  /  BACKEND SYSTEMS  /  APPLIED AI</text>
</g>

<!-- Main Name & Title -->
<g font-family="Georgia,serif" font-style="italic" font-weight="bold" fill="#f3f1ff">
  <text x="30" y="118" font-size="52" letter-spacing="-1">Faris Ruknuddin</text>
</g>

<!-- Editorial Subtitle & Persona -->
<g font-family="Arial,sans-serif" font-size="18" fill="#c4c7dc">
  <text x="32" y="160">Full-Stack &amp; Backend Software Engineer · Applied AI</text>
  <text x="32" y="194" fill="#9ba1c2" font-size="15" font-family="monospace">From the interface to the system behind it.</text>
</g>

<!-- Metadata Bar -->
<g font-family="monospace" font-size="14" fill="#a6e7ff">
  <text x="32" y="248">Bhatkal, India  ·  AITM (2027)  ·  Omnimate</text>
  <text x="32" y="272" fill="#8d94be">Portfolio: zephyruszoro09.vercel.app</text>
</g>

<!-- Right Side: Circular Studio Portrait -->
<g>
  <!-- Glacier Outer Ring -->
  <circle cx="805" cy="182" r="134" fill="none" stroke="#50527d" stroke-width="2"/>
  <circle cx="805" cy="182" r="134" fill="none" stroke="#9edcff" stroke-width="2.5" stroke-dasharray="80 200" class="trace"/>
  <!-- User Studio Portrait -->
  <image href="data:image/jpeg;base64,{b64}" x="677" y="54" width="256" height="256" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>
</g>
</svg>"""


def generate_portfolio():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 116"><title>Portfolio - Faris Ruknuddin</title><style>.route{animation:go 3s linear infinite}@keyframes go{to{stroke-dashoffset:-52}}.arrow{animation:arrow 3.5s ease-in-out infinite}@keyframes arrow{50%{transform:translate(4px,-4px)}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style><path fill="#a6e7ff" d="M0 0h466l24 24v92H22L0 94Z"/><path d="M103 0v116M425 0v116" stroke="#191a35" opacity=".3" stroke-dasharray="3 4"/><g fill="#191a35"><circle cx="50" cy="58" r="23" fill="none" stroke="#191a35" stroke-width="3.5"/><ellipse cx="50" cy="58" rx="9" ry="23" fill="none" stroke="#191a35" stroke-width="2.8"/><line x1="27" y1="58" x2="73" y2="58" stroke="#191a35" stroke-width="2.8"/><line x1="33" y1="44" x2="67" y2="44" stroke="#191a35" stroke-width="2.2"/><line x1="33" y1="72" x2="67" y2="72" stroke="#191a35" stroke-width="2.2"/></g><g font-family="Arial,sans-serif" fill="#191a35"><text x="121" y="39" font-family="monospace" font-size="14" letter-spacing="1.4">LIVE PORTFOLIO</text><text x="119" y="81" font-family="Georgia,serif" font-style="italic" font-weight="bold" font-size="34" letter-spacing="-1">Digital Workshop</text></g><path d="M120 96h275" stroke="#191a35" opacity=".15"/><path class="route" d="M120 96h275" stroke="#191a35" stroke-width="2" stroke-dasharray="6 46"/><path class="arrow" d="M443 69l22-22m-18 0h18v18" fill="none" stroke="#191a35" stroke-width="3"/></svg>"""


def generate_linkedin():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 116"><title>LinkedIn - Faris Ruknuddin</title><style>.route{animation:go 3s linear infinite}@keyframes go{to{stroke-dashoffset:-52}}.arrow{animation:arrow 3.5s ease-in-out infinite}@keyframes arrow{50%{transform:translate(4px,-4px)}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style><path fill="#b8eaff" d="M0 0h466l24 24v92H22L0 94Z"/><path d="M103 0v116M425 0v116" stroke="#191a35" opacity=".3" stroke-dasharray="3 4"/><g fill="#191a35"><rect x="25" y="33" width="50" height="50" rx="4"/><path fill="#b8eaff" d="M34 48h6v23h-6zm-.5-7a3.5 3.5 0 1 0 7 0 3.5 3.5 0 1 0-7 0zM46 48h6v3q3-5 8-3 6 1 6 10v13h-6V58q0-5-4-5t-4 5v13h-6z"/></g><g font-family="Arial,sans-serif" fill="#191a35"><text x="121" y="39" font-family="monospace" font-size="14" letter-spacing="1.4">PROFESSIONAL PROFILE</text><text x="119" y="81" font-family="Georgia,serif" font-style="italic" font-weight="bold" font-size="36" letter-spacing="-1">LinkedIn</text></g><path d="M120 96h275" stroke="#191a35" opacity=".15"/><path class="route" d="M120 96h275" stroke="#191a35" stroke-width="2" stroke-dasharray="6 46"/><path class="arrow" d="M443 69l22-22m-18 0h18v18" fill="none" stroke="#191a35" stroke-width="3"/></svg>"""


def generate_email():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 116"><title>Email Faris Ruknuddin</title><style>.route{animation:go 3s linear infinite}@keyframes go{to{stroke-dashoffset:-52}}.arrow{animation:arrow 3.5s ease-in-out infinite}@keyframes arrow{50%{transform:translate(4px,-4px)}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style><path fill="#beaaff" d="M0 0h466l24 24v92H22L0 94Z"/><path d="M103 0v116M425 0v116" stroke="#191a35" opacity=".3" stroke-dasharray="3 4"/><g fill="#191a35"><path d="M22 37h56v42H22zm5 5 23 18 23-18H27zm47 5L50 66 26 47v27h48z" fill-rule="evenodd"/></g><g font-family="Arial,sans-serif" fill="#191a35"><text x="121" y="39" font-family="monospace" font-size="14" letter-spacing="1.4">DIRECT MESSAGE</text><text x="119" y="81" font-family="Georgia,serif" font-style="italic" font-weight="bold" font-size="36" letter-spacing="-1">Email Faris</text></g><path d="M120 96h275" stroke="#191a35" opacity=".15"/><path class="route" d="M120 96h275" stroke="#191a35" stroke-width="2" stroke-dasharray="6 46"/><path class="arrow" d="M443 69l22-22m-18 0h18v18" fill="none" stroke="#191a35" stroke-width="3"/></svg>"""


def generate_shelfday_hero():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 316" role="img">
<title>Shelfday - Kitchen Prep, Perishable Stock &amp; Closing Workbench</title>
<defs>
  <pattern id="grid" width="16" height="16" patternUnits="userSpaceOnUse">
    <circle cx="1" cy="1" r=".8" fill="#5a6080"/>
  </pattern>
  <clipPath id="frame">
    <rect x="510" y="0" width="490" height="316"/>
  </clipPath>
</defs>
<style>
  .batch-pulse { animation: pulse 6s ease-in-out infinite alternate; }
  .bar-alloc { animation: alloc 8s ease-in-out infinite; }
  .tag-flash { animation: flash 4s step-end infinite; }
  @keyframes pulse { 0% { opacity: 0.7; } 100% { opacity: 1; } }
  @keyframes alloc { 0%, 20% { width: 30px; } 50%, 80% { width: 220px; } 100% { width: 30px; } }
  @keyframes flash { 0%, 100% { fill: #a1f0db; } 50% { fill: #c8eaff; } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>

<rect width="1000" height="316" rx="12" fill="#191a31"/>
<rect x="510" width="490" height="316" fill="url(#grid)"/>

<!-- Left Side: Editorial Typography -->
<g font-family="monospace" font-size="16" fill="#b4e5ff">
  <text x="33" y="42">FULL-STACK  /  KITCHEN WORKBENCH</text>
</g>
<g font-family="Georgia,serif" font-style="italic" fill="#f3f1ff" font-size="58">
  <text x="30" y="133">Shelfday</text>
</g>
<text x="34" y="185" fill="#c4c7dc" font-size="19" font-family="Arial,sans-serif">
  Perishable stock, batch expiry &amp; closing reconciliation.
</text>
<text x="34" y="225" fill="#8e94be" font-size="14" font-family="monospace">
  Earliest-expiry-first (FEFO) allocation · Atomic shortage rollback
</text>
<text x="34" y="270" fill="#a6e7ff" font-size="14" font-family="monospace">
  TypeScript · React · Cloudflare D1 · SQLite
</text>

<path d="M507 24v268" stroke="#515371"/>

<!-- Right Side: Illustrated Batch Workbench Lifecycle -->
<g clip-path="url(#frame)" transform="translate(535, 30)">
  <!-- Batch 1 Card -->
  <g transform="translate(0, 15)">
    <rect width="440" height="65" rx="8" fill="#222543" stroke="#484d72" stroke-width="1.2"/>
    <rect x="16" y="16" width="120" height="32" rx="4" fill="#14152a"/>
    <text x="28" y="37" fill="#a1f0db" font-family="monospace" font-size="13" font-weight="bold" class="tag-flash">LOT #2601 · 24H</text>
    
    <text x="150" y="28" fill="#e2e8f0" font-family="Arial,sans-serif" font-size="13" font-weight="bold">Organic Dairy Prep</text>
    <rect x="150" y="36" width="260" height="12" rx="3" fill="#14152a"/>
    <rect class="bar-alloc" x="150" y="36" width="190" height="12" rx="3" fill="#60a5fa"/>
  </g>

  <!-- Batch 2 Card -->
  <g transform="translate(0, 95)">
    <rect width="440" height="65" rx="8" fill="#222543" stroke="#484d72" stroke-width="1.2"/>
    <rect x="16" y="16" width="120" height="32" rx="4" fill="#14152a"/>
    <text x="28" y="37" fill="#c8eaff" font-family="monospace" font-size="13">LOT #2602 · 48H</text>
    
    <text x="150" y="28" fill="#e2e8f0" font-family="Arial,sans-serif" font-size="13" font-weight="bold">Cold Press Infusion</text>
    <rect x="150" y="36" width="260" height="12" rx="3" fill="#14152a"/>
    <rect x="150" y="36" width="110" height="12" rx="3" fill="#a78bfa"/>
  </g>

  <!-- Rollback / Reconciliation Tag -->
  <g transform="translate(0, 175)">
    <rect width="440" height="50" rx="8" fill="#181a33" stroke="#50527d"/>
    <circle cx="28" cy="25" r="5" fill="#a1f0db"/>
    <text x="44" y="30" fill="#a1f0db" font-family="monospace" font-size="12">
      CLOSING RECONCILED: 0 SHORTAGES · ROLLBACK SAFE
    </text>
  </g>
</g>
</svg>"""


def generate_project_reel():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 262" role="img">
<title>Cueproof caption desk and TarkAI code practice studio, illustrated</title>
<style>
  .cue-wave { animation: w 1.2s ease-in-out infinite alternate; transform-box: fill-box; transform-origin: center; }
  .ast-pulse { animation: a 3s ease-in-out infinite alternate; }
  @keyframes w { to { transform: scaleY(0.2); } }
  @keyframes a { 0% { opacity: 0.6; } 100% { opacity: 1; } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>

<!-- Left Panel: Cueproof Caption Desk -->
<rect width="496" height="262" fill="#caeaff"/>
<text x="24" y="33" font-size="15" fill="#343559" font-family="monospace">CAPTION DESK  /  TIME-CODED REVIEW</text>
<text x="22" y="84" font-size="48" fill="#14152a" font-family="Georgia,serif" font-weight="bold" font-style="italic" letter-spacing="-1.2">Cueproof</text>

<g transform="translate(24, 120)">
  <!-- Audio Waveform -->
  <g stroke="#14152a" stroke-width="2.5">
    <path class="cue-wave" style="animation-delay:0.0s" d="M0 -10v20"/>
    <path class="cue-wave" style="animation-delay:-0.1s" d="M8 -16v32"/>
    <path class="cue-wave" style="animation-delay:-0.2s" d="M16 -22v44"/>
    <path class="cue-wave" style="animation-delay:-0.3s" d="M24 -12v24"/>
    <path class="cue-wave" style="animation-delay:-0.4s" d="M32 -18v36"/>
    <path class="cue-wave" style="animation-delay:-0.5s" d="M40 -8v16"/>
  </g>

  <!-- Cue Box -->
  <rect x="65" y="-20" width="220" height="42" rx="6" fill="#14152a"/>
  <text x="78" y="6" fill="#caeaff" font-family="monospace" font-size="13">00:01:24.300 ➔ 28.150</text>

  <!-- Diff -->
  <g transform="translate(0, 48)">
    <rect width="320" height="26" rx="4" fill="#273356"/>
    <text x="12" y="17" fill="#f0edff" font-family="monospace" font-size="12">[+] restored sound cue: [engine revs]</text>
  </g>

  <text x="0" y="105" font-size="13" fill="#303b60" font-family="monospace">IN-BROWSER DIFFS  ·  LIVE DEMO AVAILABLE</text>
</g>

<!-- Right Panel: TarkAI Practice Studio -->
<rect x="504" width="496" height="262" fill="#b7a8ff"/>
<text x="529" y="33" font-size="15" fill="#2b2949" font-family="monospace">PRACTICE STUDIO  /  AST ANALYSIS</text>
<text x="527" y="84" font-size="48" fill="#14152a" font-family="Georgia,serif" font-weight="bold" font-style="italic" letter-spacing="-1.2">TarkAI (तर्क)</text>

<g transform="translate(528, 115)">
  <!-- AST Node Tree -->
  <rect x="0" y="0" width="90" height="26" rx="4" fill="#14152a"/>
  <text x="16" y="17" fill="#b7a8ff" font-family="monospace" font-size="12">Module</text>

  <path d="M 90 13 H 125 V 0 H 145" stroke="#14152a" stroke-width="2" fill="none"/>
  <path d="M 125 13 V 30 H 145" stroke="#14152a" stroke-width="2" fill="none"/>

  <rect x="145" y="-12" width="120" height="24" rx="4" fill="#393566"/>
  <text x="155" y="4" fill="#f0edff" font-family="monospace" font-size="11">FunctionDef</text>

  <rect x="145" y="20" width="120" height="24" rx="4" fill="#393566"/>
  <text x="155" y="36" fill="#f0edff" font-family="monospace" font-size="11">Subprocess</text>

  <g transform="translate(0, 62)">
    <rect width="360" height="28" rx="4" fill="#14152a"/>
    <text x="14" y="18" fill="#e0d9ff" font-family="monospace" font-size="12">
      HEURISTIC FEEDBACK  ·  LEITNER REVIEW
    </text>
  </g>

  <text x="0" y="112" font-size="13" fill="#36304d" font-family="monospace">LOCAL PYTHON STUDIO  ·  33/33 TESTS</text>
</g>
</svg>"""


def generate_session():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 203" role="img">
<title>Shelfday batch allocation and rollback sequence, illustrated</title>
<style>
  text { font-family: ui-monospace, Consolas, monospace; }
  .row1 { animation: a 9s infinite; }
  .row2 { animation: b 9s infinite; }
  .row3 { animation: c 9s infinite; }
  @keyframes a { 0% { opacity: .15; } 12%, 95% { opacity: 1; } }
  @keyframes b { 0%, 23% { opacity: .15; } 40%, 95% { opacity: 1; } }
  @keyframes c { 0%, 49% { opacity: .15; } 66%, 95% { opacity: 1; } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>
<rect width="960" height="203" fill="#15162d"/>
<rect x="0" width="5" height="203" fill="#9cdcff"/>
<path d="M25 52H933" stroke="#454767"/>
<g font-size="17" fill="#b8b2ff">
  <text x="28" y="34">faris@systems-lab ~/shelfday</text>
  <text x="932" y="34" text-anchor="end">BATCH ALLOCATION / REPLAY</text>
</g>
<g font-size="20" fill="#eff5ff">
  <text class="row1" x="28" y="92">[ intake ]    Tag perishable delivery with batch number and strict expiry timestamp.</text>
  <text class="row2" x="28" y="131">[ deduct ]    Earliest-expiry-first (FEFO) allocation across prep queues.</text>
  <text class="row3" x="28" y="170">[ rollback ]  Portion cancelled: atomic stock restoration to the originating batch.</text>
</g>
</svg>"""


def main():
    write_svg("identity.svg", generate_identity())
    write_svg("portfolio.svg", generate_portfolio())
    write_svg("linkedin.svg", generate_linkedin())
    write_svg("email.svg", generate_email())
    write_svg("shelfday-hero.svg", generate_shelfday_hero())
    write_svg("project-reel.svg", generate_project_reel())
    write_svg("session.svg", generate_session())
    print("All glacier SVG assets built successfully.")


if __name__ == "__main__":
    main()
