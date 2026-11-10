"""
Build clean, polished, editorial-grade SVGs matching 7awwad's glacier design language:
  - assets/identity.svg
  - assets/portfolio.svg
  - assets/linkedin.svg
  - assets/email.svg
  - assets/intersection.svg
  - assets/project-reel.svg
  - assets/session.svg
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def write_svg(filename, content):
    dest = ASSETS / filename
    dest.write_text(content.strip(), encoding="utf-8")
    print(f"Generated {dest.relative_to(ROOT)} ({len(content)} bytes)")


def generate_identity():
    # Read the ASCII portrait from faris-ascii.svg if available
    ascii_svg_path = ROOT / "faris-ascii.svg"
    ascii_body = ""
    if ascii_svg_path.exists():
        raw = ascii_svg_path.read_text(encoding="utf-8")
        # Extract inner contents
        start = raw.find("<rect width=")
        end = raw.rfind("</svg>")
        if start != -1 and end != -1:
            ascii_body = raw[start:end]

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 364" role="img">
<title>Faris Ruknuddin - ZephyrusZorro</title>
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
  <clipPath id="terminal-clip">
    <rect x="0" y="0" width="840" height="880" rx="12"/>
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
  <text x="32" y="335">SYSTEMS ENGINEERING  /  APPLIED AI  /  CYBERSECURITY</text>
</g>

<!-- Main Name & Title -->
<g font-family="Georgia,serif" font-style="italic" font-weight="bold" fill="#f3f1ff">
  <text x="30" y="118" font-size="52" letter-spacing="-1">Faris Ruknuddin</text>
</g>

<!-- Editorial Subtitle & Persona -->
<g font-family="Arial,sans-serif" font-size="18" fill="#c4c7dc">
  <text x="32" y="160">Backend &amp; full-stack software engineer · Applied AI</text>
  <text x="32" y="194" fill="#9ba1c2" font-size="15" font-family="monospace">From the interface to the system behind it.</text>
</g>

<!-- Metadata Bar -->
<g font-family="monospace" font-size="14" fill="#a6e7ff">
  <text x="32" y="248">Bhatkal, India  ·  AITM (2027)  ·  Founder @ Omnimate</text>
  <text x="32" y="272" fill="#8d94be">Portfolio: zephyruszoro09.vercel.app</text>
</g>

<!-- Right Side: Mini Terminal Portrait -->
<g transform="translate(640, 24) scale(0.36)" clip-path="url(#terminal-clip)">
  {ascii_body}
</g>
</svg>"""


def generate_portfolio():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 116"><title>Portfolio - Faris Ruknuddin</title><style>.route{animation:go 3s linear infinite}@keyframes go{to{stroke-dashoffset:-52}}.arrow{animation:arrow 3.5s ease-in-out infinite}@keyframes arrow{50%{transform:translate(4px,-4px)}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style><path fill="#a6e7ff" d="M0 0h466l24 24v92H22L0 94Z"/><path d="M103 0v116M425 0v116" stroke="#191a35" opacity=".3" stroke-dasharray="3 4"/><g fill="#191a35"><circle cx="50" cy="58" r="23" fill="none" stroke="#191a35" stroke-width="3.5"/><ellipse cx="50" cy="58" rx="9" ry="23" fill="none" stroke="#191a35" stroke-width="2.8"/><line x1="27" y1="58" x2="73" y2="58" stroke="#191a35" stroke-width="2.8"/><line x1="33" y1="44" x2="67" y2="44" stroke="#191a35" stroke-width="2.2"/><line x1="33" y1="72" x2="67" y2="72" stroke="#191a35" stroke-width="2.2"/></g><g font-family="Arial,sans-serif" fill="#191a35"><text x="121" y="39" font-family="monospace" font-size="14" letter-spacing="1.4">LIVE PORTFOLIO</text><text x="119" y="81" font-family="Georgia,serif" font-style="italic" font-weight="bold" font-size="34" letter-spacing="-1">Digital Workshop</text></g><path d="M120 96h275" stroke="#191a35" opacity=".15"/><path class="route" d="M120 96h275" stroke="#191a35" stroke-width="2" stroke-dasharray="6 46"/><path class="arrow" d="M443 69l22-22m-18 0h18v18" fill="none" stroke="#191a35" stroke-width="3"/></svg>"""


def generate_linkedin():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 116"><title>LinkedIn - Faris Ruknuddin</title><style>.route{animation:go 3s linear infinite}@keyframes go{to{stroke-dashoffset:-52}}.arrow{animation:arrow 3.5s ease-in-out infinite}@keyframes arrow{50%{transform:translate(4px,-4px)}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style><path fill="#b8eaff" d="M0 0h466l24 24v92H22L0 94Z"/><path d="M103 0v116M425 0v116" stroke="#191a35" opacity=".3" stroke-dasharray="3 4"/><g fill="#191a35"><rect x="25" y="33" width="50" height="50" rx="4"/><path fill="#b8eaff" d="M34 48h6v23h-6zm-.5-7a3.5 3.5 0 1 0 7 0 3.5 3.5 0 1 0-7 0zM46 48h6v3q3-5 8-3 6 1 6 10v13h-6V58q0-5-4-5t-4 5v13h-6z"/></g><g font-family="Arial,sans-serif" fill="#191a35"><text x="121" y="39" font-family="monospace" font-size="14" letter-spacing="1.4">PROFESSIONAL PROFILE</text><text x="119" y="81" font-family="Georgia,serif" font-style="italic" font-weight="bold" font-size="36" letter-spacing="-1">LinkedIn</text></g><path d="M120 96h275" stroke="#191a35" opacity=".15"/><path class="route" d="M120 96h275" stroke="#191a35" stroke-width="2" stroke-dasharray="6 46"/><path class="arrow" d="M443 69l22-22m-18 0h18v18" fill="none" stroke="#191a35" stroke-width="3"/></svg>"""


def generate_email():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 116"><title>Email Faris Ruknuddin</title><style>.route{animation:go 3s linear infinite}@keyframes go{to{stroke-dashoffset:-52}}.arrow{animation:arrow 3.5s ease-in-out infinite}@keyframes arrow{50%{transform:translate(4px,-4px)}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style><path fill="#beaaff" d="M0 0h466l24 24v92H22L0 94Z"/><path d="M103 0v116M425 0v116" stroke="#191a35" opacity=".3" stroke-dasharray="3 4"/><g fill="#191a35"><path d="M22 37h56v42H22zm5 5 23 18 23-18H27zm47 5L50 66 26 47v27h48z" fill-rule="evenodd"/></g><g font-family="Arial,sans-serif" fill="#191a35"><text x="121" y="39" font-family="monospace" font-size="14" letter-spacing="1.4">DIRECT MESSAGE</text><text x="119" y="81" font-family="Georgia,serif" font-style="italic" font-weight="bold" font-size="36" letter-spacing="-1">Email Faris</text></g><path d="M120 96h275" stroke="#191a35" opacity=".15"/><path class="route" d="M120 96h275" stroke="#191a35" stroke-width="2" stroke-dasharray="6 46"/><path class="arrow" d="M443 69l22-22m-18 0h18v18" fill="none" stroke="#191a35" stroke-width="3"/></svg>"""


def generate_intersection():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 316" role="img"><title>Adaptive Traffic Signals – illustrated queue release</title><defs><pattern id="grid" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".8" fill="#5a6080"/></pattern><clipPath id="frame"><rect x="510" y="0" width="490" height="316"/></clipPath></defs><style>.flow{animation:release 8s linear infinite}.lamp{animation:go 8s step-end infinite}.scan{animation:read 8s ease-in-out infinite}@keyframes release{0%{transform:translateX(-42px);opacity:0}12%{opacity:1}28%,55%{transform:translateX(0);opacity:1}91%,100%{transform:translateX(350px);opacity:0}}@keyframes go{0%,98%{fill:#ed9aca}55%{fill:#a1f0db}}@keyframes read{0%,54%,100%{opacity:.9}65%,90%{opacity:.18}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style><rect width="1000" height="316" rx="12" fill="#191a31"/><rect x="510" width="490" height="316" fill="url(#grid)"/><g clip-path="url(#frame)"><g transform="rotate(-14 765 155)"><path d="M444 157H1060M765 -95V385" fill="none" stroke="#525779" stroke-width="86"/><path d="M444 157H1060M765 -95V385" fill="none" stroke="#292c46" stroke-width="82"/><path d="M444 157h279m86 0h251M765 -95v210m0 85v185" fill="none" stroke="#7982a0" stroke-width="2" stroke-dasharray="13 11"/><path d="M711 161v34m108-74v33" stroke="#d0cbe7" stroke-width="4"/><g class="flow"><g transform="translate(669 171)"><rect width="28" height="14" rx="4" fill="#bbaeff"/><rect x="17" y="2" width="6" height="10" rx="1" fill="#343854"/><path d="M2 3v8m24-8v8" stroke="#eef5ff" stroke-width="1"/></g><g transform="translate(626 171)"><rect width="28" height="14" rx="4" fill="#c8eaff"/><rect x="17" y="2" width="6" height="10" rx="1" fill="#343854"/><path d="M2 3v8m24-8v8" stroke="#eef5ff" stroke-width="1"/></g><g transform="translate(583 171)"><rect width="28" height="14" rx="4" fill="#a2b0dc"/><rect x="17" y="2" width="6" height="10" rx="1" fill="#343854"/><path d="M2 3v8m24-8v8" stroke="#eef5ff" stroke-width="1"/></g></g><g transform="translate(838 132)"><rect width="28" height="14" rx="4" fill="#c8c2e2"/><rect x="5" y="2" width="6" height="10" rx="1" fill="#343854"/><path d="M2 3v8m24-8v8" stroke="#eef5ff" stroke-width="1"/></g><g transform="translate(883 132)"><rect width="28" height="14" rx="4" fill="#a5b9d7"/><rect x="5" y="2" width="6" height="10" rx="1" fill="#343854"/><path d="M2 3v8m24-8v8" stroke="#eef5ff" stroke-width="1"/></g><rect class="scan" x="574" y="163" width="131" height="30" rx="4" stroke="#a8a4ee" stroke-dasharray="5 3" fill="none"/><circle cx="714" cy="209" r="7" class="lamp" fill="#ed9aca"/></g></g><path d="M507 24v268" stroke="#515371"/><g font-family="monospace" font-size="16" fill="#b4e5ff"><text x="33" y="42">OPENCV   /   TRAFFIC CONTROL</text></g><g font-family="Georgia,serif" font-style="italic" fill="#f3f1ff" font-size="58"><text x="30" y="133">Adaptive</text><text x="30" y="197">traffic signals</text></g><text x="34" y="266" fill="#c4c7dc" font-size="19" font-family="Arial,sans-serif">Vehicle queues set the green time.</text></svg>"""


def generate_project_reel():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 262" role="img">
<title>Shelfday batch allocation and Cueproof caption review, illustrated</title>
<style>
  .bar-pulse { animation: bar 4s ease-in-out infinite alternate; }
  .cue-wave { animation: w 1.2s ease-in-out infinite alternate; transform-box: fill-box; transform-origin: center; }
  @keyframes bar { 0% { width: 85px; } 100% { width: 145px; } }
  @keyframes w { to { transform: scaleY(0.2); } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>

<!-- Left Panel: Shelfday Kitchen Operations -->
<rect width="496" height="262" fill="#caeaff"/>
<text x="24" y="33" font-size="15" fill="#343559" font-family="monospace">KITCHEN WORKBENCH  /  INVENTORY</text>
<text x="22" y="84" font-size="48" fill="#14152a" font-family="Georgia,serif" font-weight="bold" font-style="italic" letter-spacing="-1.2">Shelfday</text>

<!-- Shelfday Batch Visual -->
<g transform="translate(24, 115)">
  <!-- Batch 1 Pill -->
  <rect x="0" y="0" width="130" height="32" rx="6" fill="#14152a"/>
  <text x="14" y="21" fill="#caeaff" font-family="monospace" font-size="13" font-weight="bold">BATCH #01 · FEFO</text>

  <!-- Allocation Progress Bar -->
  <rect x="145" y="6" width="180" height="20" rx="4" fill="#a8cde5"/>
  <rect class="bar-pulse" x="145" y="6" width="120" height="20" rx="4" fill="#324068"/>

  <!-- Batch 2 Pill -->
  <rect x="0" y="44" width="130" height="32" rx="6" fill="#3a4b70"/>
  <text x="14" y="65" fill="#e8f3fa" font-family="monospace" font-size="13">BATCH #02 · PREP</text>

  <rect x="145" y="50" width="180" height="20" rx="4" fill="#a8cde5"/>
  <rect x="145" y="50" width="65" height="20" rx="4" fill="#324068"/>

  <text x="0" y="112" font-size="14" fill="#2d3656" font-family="monospace">FEFO ALLOCATION  /  ROLLBACK-SAFE</text>
</g>

<!-- Right Panel: Cueproof Caption Desk -->
<rect x="504" width="496" height="262" fill="#b7a8ff"/>
<text x="529" y="33" font-size="15" fill="#2b2949" font-family="monospace">CAPTION DESK  /  TIME-CODED REVIEW</text>
<text x="527" y="84" font-size="48" fill="#14152a" font-family="Georgia,serif" font-weight="bold" font-style="italic" letter-spacing="-1.2">Cueproof</text>

<!-- Cueproof Diff Visual -->
<g transform="translate(528, 120)">
  <!-- Audio Waveform -->
  <g stroke="#14152a" stroke-width="2.5">
    <path class="cue-wave" style="animation-delay:0.0s" d="M0 -10v20"/>
    <path class="cue-wave" style="animation-delay:-0.1s" d="M8 -16v32"/>
    <path class="cue-wave" style="animation-delay:-0.2s" d="M16 -22v44"/>
    <path class="cue-wave" style="animation-delay:-0.3s" d="M24 -12v24"/>
    <path class="cue-wave" style="animation-delay:-0.4s" d="M32 -18v36"/>
    <path class="cue-wave" style="animation-delay:-0.5s" d="M40 -8v16"/>
  </g>

  <!-- Timestamp Cue Box -->
  <rect x="65" y="-20" width="220" height="42" rx="6" fill="#14152a"/>
  <text x="78" y="6" fill="#b7a8ff" font-family="monospace" font-size="13">00:01:24.300 ➔ 28.150</text>

  <!-- Diff Indicator -->
  <g transform="translate(0, 48)">
    <rect width="285" height="26" rx="4" fill="#393566"/>
    <text x="12" y="17" fill="#f0edff" font-family="monospace" font-size="12">[+] restored sound cue: [engine revs]</text>
  </g>

  <text x="0" y="107" font-size="14" fill="#302949" font-family="monospace">SRT &amp; WEBVTT  /  IN-BROWSER DIFFS</text>
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
    write_svg("intersection.svg", generate_intersection())
    write_svg("project-reel.svg", generate_project_reel())
    write_svg("session.svg", generate_session())
    print("All editorial-grade glacier SVGs built successfully.")


if __name__ == "__main__":
    main()
