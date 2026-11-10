"""
Generate bespoke animated SVGs for Faris Ruknuddin's GitHub profile:
  - assets/identity.svg
  - assets/linkedin.svg
  - assets/email.svg
  - assets/casevault-forensics.svg
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
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" role="img">
<title>Faris Ruknuddin - Systems Architect, Applied AI &amp; Cybersecurity Engineer</title>
<defs>
  <linearGradient id="cyber-grad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#00f2fe"/>
    <stop offset="50%" stop-color="#4facfe"/>
    <stop offset="100%" stop-color="#8b5cf6"/>
  </linearGradient>
  <linearGradient id="shield-grad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.1"/>
  </linearGradient>
  <pattern id="mesh" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#2d3748" opacity="0.6"/>
  </pattern>
</defs>
<style>
  .trace { stroke-dasharray: 60 400; animation: trace 6s linear infinite; }
  .pulse { animation: pulse 3s ease-in-out infinite alternate; }
  .scan { animation: scan 4s ease-in-out infinite; }
  .blink { animation: blink 2s step-end infinite; }
  @keyframes trace { to { stroke-dashoffset: -460; } }
  @keyframes pulse { 0% { opacity: 0.35; } 100% { opacity: 0.85; } }
  @keyframes scan { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(110px); } }
  @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>

<!-- Background Base -->
<rect width="1000" height="360" rx="16" fill="#0b0f19"/>
<rect width="1000" height="360" rx="16" fill="url(#mesh)"/>

<!-- Glowing Cyber Border -->
<rect x="2" y="2" width="996" height="356" rx="14" fill="none" stroke="#1f293d" stroke-width="2"/>
<path class="trace" d="M 20 2 H 980 A 14 14 0 0 1 998 20 V 340 A 14 14 0 0 1 980 358 H 20 A 14 14 0 0 1 2 340 V 20 A 14 14 0 0 1 20 2" fill="none" stroke="url(#cyber-grad)" stroke-width="2.5"/>

<!-- Terminal Bar Header -->
<g transform="translate(36, 32)">
  <circle cx="0" cy="0" r="5" fill="#ef4444"/>
  <circle cx="16" cy="0" r="5" fill="#f59e0b"/>
  <circle cx="32" cy="0" r="5" fill="#10b981"/>
  <text x="56" y="4" fill="#64748b" font-family="ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace" font-size="12" letter-spacing="1">faris@systems-lab:~ // SEC_TELEMETRY.v4</text>
  <rect x="360" y="-7" width="10" height="15" fill="#00f2fe" class="blink"/>
</g>

<!-- Left: Name & Title Hero -->
<g transform="translate(36, 85)">
  <!-- Name -->
  <text x="0" y="42" fill="#ffffff" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif" font-weight="900" font-size="46" letter-spacing="-1">FARIS RUKNUDDIN</text>
  
  <!-- Headline -->
  <text x="0" y="78" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif" font-weight="600" font-size="20" letter-spacing="-0.3">Systems Architect &#183; Applied AI &amp; Cybersecurity Engineer</text>
  
  <!-- Subtitle Narrative -->
  <text x="0" y="112" fill="#64748b" font-family="ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace" font-size="13">
    Architecting tamper-evident forensics, AST static security analysis &amp; local-first resilient engines.
  </text>

  <!-- Capability Badges -->
  <g transform="translate(0, 142)">
    <!-- Badge 1: AppSec & Forensics -->
    <rect x="0" y="0" width="168" height="30" rx="6" fill="#0f172a" stroke="#00f2fe" stroke-width="1.2"/>
    <circle cx="14" cy="15" r="4" fill="#00f2fe"/>
    <text x="26" y="19" fill="#e2e8f0" font-family="ui-monospace,Consolas,monospace" font-size="11" font-weight="700">SAST &amp; FORENSICS</text>

    <!-- Badge 2: Defense-in-Depth -->
    <rect x="178" y="0" width="180" height="30" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <circle cx="192" cy="15" r="4" fill="#10b981"/>
    <text x="204" y="19" fill="#e2e8f0" font-family="ui-monospace,Consolas,monospace" font-size="11" font-weight="700">DEFENSE-IN-DEPTH</text>

    <!-- Badge 3: Computer Vision & Control -->
    <rect x="368" y="0" width="176" height="30" rx="6" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
    <circle cx="382" cy="15" r="4" fill="#8b5cf6"/>
    <text x="394" y="19" fill="#e2e8f0" font-family="ui-monospace,Consolas,monospace" font-size="11" font-weight="700">OPENCV &amp; RESILIENCE</text>
  </g>

  <!-- Credential Telemetry -->
  <g transform="translate(0, 204)" font-family="ui-monospace,Consolas,monospace" font-size="12" fill="#64748b">
    <text x="0" y="0">&#9658; Founder @ Omnimate &#183; Smart India Hackathon '26 Finalist &#183; B.E. AI &amp; ML (2027)</text>
    <text x="0" y="20" fill="#475569">&#9658; 5&#215; Engineering Internships &#183; 16 Production &amp; Systems Repositories</text>
  </g>
</g>

<!-- Right: Visual Cybernetic Shield & Telemetry HUD -->
<g transform="translate(680, 50)">
  <!-- Outer HUD Ring -->
  <circle cx="140" cy="130" r="120" fill="none" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 6"/>
  <circle cx="140" cy="130" r="95" fill="none" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Rotating Pulse Ring -->
  <circle cx="140" cy="130" r="95" fill="none" stroke="#00f2fe" stroke-width="2" stroke-dasharray="40 220" class="trace"/>

  <!-- Cyber Shield Silhouette -->
  <path d="M 140 60 L 205 85 V 135 C 205 180 140 205 140 205 C 140 205 75 180 75 135 V 85 Z" 
        fill="url(#shield-grad)" stroke="#00f2fe" stroke-width="2" class="pulse"/>

  <!-- Scanning Laser Bar -->
  <line class="scan" x1="85" y1="85" x2="195" y2="85" stroke="#38ef7d" stroke-width="2" opacity="0.8"/>

  <!-- Shield Core Lock / Node Icon -->
  <circle cx="140" cy="125" r="16" fill="#0b0f19" stroke="#8b5cf6" stroke-width="2"/>
  <path d="M 134 125 L 140 131 L 148 119" fill="none" stroke="#00f2fe" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- HUD Status Readouts -->
  <g font-family="ui-monospace,Consolas,monospace" font-size="10" fill="#94a3b8">
    <rect x="35" y="222" width="210" height="24" rx="4" fill="#0f172a" stroke="#334155"/>
    <circle cx="48" cy="234" r="3" fill="#10b981"/>
    <text x="58" y="238" fill="#10b981" font-weight="700">INTEGRITY: MERKLE_VERIFIED</text>
    
    <text x="140" y="260" text-anchor="middle" fill="#475569" font-size="9">SHA-256: 7F9E...D412 // ZERO TRUST</text>
  </g>
</g>
</svg>"""


def generate_linkedin():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 116" role="img">
<title>LinkedIn - Faris Ruknuddin</title>
<style>
  .route { animation: go 3s linear infinite; }
  .arrow { animation: arrow 3.5s ease-in-out infinite; }
  @keyframes go { to { stroke-dashoffset: -52; } }
  @keyframes arrow { 50% { transform: translate(4px, -4px); } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>
<path fill="#b8eaff" d="M0 0h466l24 24v92H22L0 94Z"/>
<path d="M103 0v116M425 0v116" stroke="#191a35" opacity=".3" stroke-dasharray="3 4"/>
<g fill="#191a35">
  <rect x="25" y="33" width="50" height="50" rx="6"/>
  <path fill="#b8eaff" d="M34 48h6v23h-6zm-.5-7a3.5 3.5 0 1 0 7 0 3.5 3.5 0 1 0-7 0zM46 48h6v3q3-5 8-3 6 1 6 10v13h-6V58q0-5-4-5t-4 5v13h-6z"/>
</g>
<g font-family="Arial,sans-serif" fill="#191a35">
  <text x="121" y="39" font-family="monospace" font-size="14" letter-spacing="1.4">PROFESSIONAL NETWORK</text>
  <text x="119" y="81" font-family="Georgia,serif" font-style="italic" font-weight="bold" font-size="34" letter-spacing="-1">LinkedIn</text>
</g>
<path d="M120 96h275" stroke="#191a35" opacity=".15"/>
<path class="route" d="M120 96h275" stroke="#191a35" stroke-width="2" stroke-dasharray="6 46"/>
<path class="arrow" d="M443 69l22-22m-18 0h18v18" fill="none" stroke="#191a35" stroke-width="3"/>
</svg>"""


def generate_email():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 116" role="img">
<title>Email Faris Ruknuddin</title>
<style>
  .route { animation: go 3s linear infinite; }
  .arrow { animation: arrow 3.5s ease-in-out infinite; }
  @keyframes go { to { stroke-dashoffset: -52; } }
  @keyframes arrow { 50% { transform: translate(4px, -4px); } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>
<path fill="#beaaff" d="M0 0h466l24 24v92H22L0 94Z"/>
<path d="M103 0v116M425 0v116" stroke="#191a35" opacity=".3" stroke-dasharray="3 4"/>
<g fill="#191a35">
  <path d="M22 37h56v42H22zm5 5 23 18 23-18H27zm47 5L50 66 26 47v27h48z" fill-rule="evenodd"/>
</g>
<g font-family="Arial,sans-serif" fill="#191a35">
  <text x="121" y="39" font-family="monospace" font-size="14" letter-spacing="1.4">DIRECT INQUIRY</text>
  <text x="119" y="81" font-family="Georgia,serif" font-style="italic" font-weight="bold" font-size="34" letter-spacing="-1">Email Faris</text>
</g>
<path d="M120 96h275" stroke="#191a35" opacity=".15"/>
<path class="route" d="M120 96h275" stroke="#191a35" stroke-width="2" stroke-dasharray="6 46"/>
<path class="arrow" d="M443 69l22-22m-18 0h18v18" fill="none" stroke="#191a35" stroke-width="3"/>
</svg>"""


def generate_casevault_forensics():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 320" role="img">
<title>ID-SHIELD (CaseVault) - Explainable Identity &amp; Document Forensics Platform</title>
<defs>
  <pattern id="grid-dots" width="16" height="16" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#475569" opacity="0.4"/>
  </pattern>
  <linearGradient id="scan-grad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#ef4444" stop-opacity="0"/>
    <stop offset="50%" stop-color="#ef4444" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#ef4444" stop-opacity="0"/>
  </linearGradient>
</defs>
<style>
  .scanline { animation: scanmove 4s ease-in-out infinite; }
  .badge-flash { animation: flash 2s step-end infinite; }
  .seal-pulse { animation: sealpulse 3s ease-in-out infinite alternate; }
  @keyframes scanmove { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(140px); } }
  @keyframes flash { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
  @keyframes sealpulse { 0% { transform: scale(0.98); } 100% { transform: scale(1.02); } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>

<!-- Background Frame -->
<rect width="1000" height="320" rx="14" fill="#0f1422"/>
<rect x="490" width="510" height="320" rx="14" fill="url(#grid-dots)"/>
<path d="M 490 20 V 300" stroke="#1e293b" stroke-width="2"/>

<!-- Left Side: Narrative & Identity -->
<g transform="translate(36, 42)">
  <text x="0" y="0" fill="#00f2fe" font-family="ui-monospace,Consolas,monospace" font-size="14" font-weight="700" letter-spacing="1.5">
    SMART INDIA HACKATHON 2026 &#183; SIH26188 &#183; TEAM HACKHIVE
  </text>
  
  <text x="0" y="62" fill="#ffffff" font-family="Georgia,serif" font-style="italic" font-size="44" font-weight="bold" letter-spacing="-1">
    ID-SHIELD Forensics
  </text>
  
  <text x="0" y="112" fill="#cbd5e1" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="18" font-weight="600">
    Multi-Document Evidence Fusion &amp; Cryptographic Audit Logs
  </text>

  <text x="0" y="148" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="14" width="420">
    Manual verification checks one document in isolation. ID-SHIELD correlates complete
    evidence sets, exposing subtle cross-record date, address &amp; facial contradictions.
  </text>

  <!-- Tags -->
  <g transform="translate(0, 196)">
    <rect x="0" y="0" width="186" height="28" rx="4" fill="#1e293b" stroke="#00f2fe" stroke-width="1"/>
    <text x="12" y="18" fill="#00f2fe" font-family="ui-monospace,Consolas,monospace" font-size="11" font-weight="700">MERKLE AUDIT TRAIL</text>

    <rect x="196" y="0" width="194" height="28" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="208" y="18" fill="#10b981" font-family="ui-monospace,Consolas,monospace" font-size="11" font-weight="700">ZERO-TRUST RBAC VAULT</text>
  </g>
</g>

<!-- Right Side: Interactive Forensics Scanning Schematic -->
<g transform="translate(520, 36)">
  <!-- Document Card 1: Primary ID -->
  <g transform="translate(15, 20)">
    <rect width="180" height="130" rx="8" fill="#161e31" stroke="#334155" stroke-width="1.5"/>
    <rect x="12" y="12" width="40" height="40" rx="4" fill="#1e293b" stroke="#475569"/>
    <!-- Simulated portrait silhouette -->
    <circle cx="32" cy="28" r="9" fill="#64748b"/>
    <path d="M 20 48 C 20 38 44 38 44 48" fill="#64748b"/>
    <!-- ID Fields -->
    <rect x="62" y="14" width="90" height="8" rx="2" fill="#475569"/>
    <rect x="62" y="28" width="60" height="6" rx="2" fill="#334155"/>
    <text x="14" y="78" fill="#94a3b8" font-family="ui-monospace,Consolas,monospace" font-size="10">DOB: 12-04-1998</text>
    <text x="14" y="96" fill="#94a3b8" font-family="ui-monospace,Consolas,monospace" font-size="10">ID_REF: #9821-IND</text>
    <rect x="14" y="108" width="152" height="10" rx="2" fill="#0f172a"/>
  </g>

  <!-- Document Card 2: Secondary Proof -->
  <g transform="translate(245, 20)">
    <rect width="180" height="130" rx="8" fill="#161e31" stroke="#334155" stroke-width="1.5"/>
    <rect x="12" y="12" width="40" height="40" rx="4" fill="#1e293b" stroke="#475569"/>
    <circle cx="32" cy="28" r="9" fill="#64748b"/>
    <path d="M 20 48 C 20 38 44 38 44 48" fill="#64748b"/>
    <!-- ID Fields -->
    <rect x="62" y="14" width="90" height="8" rx="2" fill="#475569"/>
    <rect x="62" y="28" width="75" height="6" rx="2" fill="#334155"/>
    <!-- Altered date highlighted -->
    <rect x="12" y="66" width="125" height="16" rx="3" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
    <text x="16" y="78" fill="#fca5a5" font-family="ui-monospace,Consolas,monospace" font-size="10" font-weight="700">DOB: 12-04-2001 &#9888;</text>
    <text x="14" y="96" fill="#94a3b8" font-family="ui-monospace,Consolas,monospace" font-size="10">ID_REF: #3104-DL</text>
    <rect x="14" y="108" width="152" height="10" rx="2" fill="#0f172a"/>
  </g>

  <!-- Laser Scanning Bar running across documents -->
  <g class="scanline" transform="translate(15, 10)">
    <line x1="0" y1="0" x2="410" y2="0" stroke="#00f2fe" stroke-width="2" opacity="0.8"/>
    <rect x="0" y="-8" width="410" height="16" fill="url(#scan-grad)"/>
  </g>

  <!-- Discrepancy Detection Connector -->
  <path d="M 195 98 H 245" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3"/>
  <circle cx="220" cy="98" r="9" fill="#ef4444" class="badge-flash"/>
  <text x="220" y="102" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">!</text>

  <!-- Evidence Verdict Banner -->
  <g transform="translate(15, 168)">
    <rect width="410" height="42" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.2"/>
    <circle cx="28" cy="21" r="5" fill="#ef4444" class="badge-flash"/>
    <text x="44" y="25" fill="#e0e7ff" font-family="ui-monospace,Consolas,monospace" font-size="12" font-weight="700">
      DISCREPANCY ALERT: Contradictory Date of Birth
    </text>
  </g>

  <!-- Tamper-Evident Cryptographic Seal -->
  <g transform="translate(15, 222)">
    <rect width="410" height="34" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.2"/>
    <circle cx="28" cy="17" r="5" fill="#10b981"/>
    <text x="44" y="21" fill="#a7f3d0" font-family="ui-monospace,Consolas,monospace" font-size="11" font-weight="700">
      MERKLE AUDIT JOURNAL: BLOCK #2910 &#183; SHA-256 HASH CHAIN SEALED
    </text>
  </g>
</g>
</svg>"""


def generate_project_reel():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 262" role="img">
<title>TarkAI AST Code Auditor &amp; Adaptive Traffic Signals Preemption - Systems Showcase</title>
<defs>
  <pattern id="reel-mesh" width="14" height="14" patternUnits="userSpaceOnUse">
    <circle cx="1.5" cy="1.5" r="0.8" fill="#334155" opacity="0.5"/>
  </pattern>
</defs>
<style>
  .tree-node { animation: nodeflow 4s ease-in-out infinite alternate; }
  .radar-sweep { animation: radar 3s linear infinite; transform-origin: 390px 145px; }
  .car-move { animation: carqueue 6s linear infinite; }
  .siren { animation: sirenpulse 1s step-end infinite; }
  @keyframes nodeflow { 0% { opacity: 0.4; } 100% { opacity: 1; } }
  @keyframes radar { to { transform: rotate(360deg); } }
  @keyframes carqueue { 0% { transform: translateX(0); } 70%, 100% { transform: translateX(110px); } }
  @keyframes sirenpulse { 0%, 100% { fill: #ef4444; } 50% { fill: #3b82f6; } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>

<!-- Left Card: TarkAI (तर्क) AST Static Security Auditor -->
<rect width="494" height="262" rx="12" fill="#0d1322"/>
<rect width="494" height="262" rx="12" fill="url(#reel-mesh)"/>
<rect x="0" y="0" width="494" height="262" rx="12" fill="none" stroke="#1e293b" stroke-width="1.5"/>

<g transform="translate(24, 28)">
  <text x="0" y="0" font-size="12" fill="#00f2fe" font-family="ui-monospace,Consolas,monospace" font-weight="700" letter-spacing="1.2">
    SAST &#183; AST STATIC ANALYSIS &#183; SECURITY AUDITING
  </text>
  <text x="0" y="38" font-size="34" fill="#ffffff" font-family="Georgia,serif" font-weight="bold" font-style="italic">
    TarkAI (तर्क)
  </text>
  <text x="0" y="64" font-size="13" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif">
    Local-first AST security auditor, complexity profiler &amp; Socratic mentor.
  </text>
</g>

<!-- TarkAI AST Diagram Visual -->
<g transform="translate(24, 110)">
  <!-- Tree Root: Module -->
  <rect x="0" y="10" width="80" height="26" rx="4" fill="#1e293b" stroke="#00f2fe" stroke-width="1.2"/>
  <text x="14" y="27" fill="#00f2fe" font-family="ui-monospace,Consolas,monospace" font-size="11" font-weight="700">Module</text>

  <!-- Connectors -->
  <path d="M 80 23 H 115 V 0 H 135" stroke="#475569" stroke-width="1.5" fill="none"/>
  <path d="M 115 23 V 46 H 135" stroke="#475569" stroke-width="1.5" fill="none"/>

  <!-- Node 1: FunctionDef -->
  <rect x="135" y="-12" width="105" height="24" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
  <text x="145" y="4" fill="#e2e8f0" font-family="ui-monospace,Consolas,monospace" font-size="10">FunctionDef</text>

  <!-- Node 2: Unsafe Subprocess Call -->
  <rect x="135" y="34" width="145" height="26" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="1.2"/>
  <text x="143" y="51" fill="#fca5a5" font-family="ui-monospace,Consolas,monospace" font-size="10" font-weight="700">&#9888; Call(subprocess)</text>

  <!-- Security Audit Alert Box -->
  <g transform="translate(0, 80)">
    <rect width="446" height="32" rx="4" fill="#16182a" stroke="#8b5cf6" stroke-width="1"/>
    <circle cx="16" cy="16" r="4" fill="#00f2fe"/>
    <text x="28" y="20" fill="#cbd5e1" font-family="ui-monospace,Consolas,monospace" font-size="11">
      AUDIT: Shell injection vector isolated &#183; 33/33 Tests Passed
    </text>
  </g>
</g>


<!-- Right Card: Adaptive Traffic Signals & EV Override -->
<rect x="506" width="494" height="262" rx="12" fill="#0e1726"/>
<rect x="506" width="494" height="262" rx="12" fill="url(#reel-mesh)"/>
<rect x="506" y="0" width="494" height="262" rx="12" fill="none" stroke="#1e293b" stroke-width="1.5"/>

<g transform="translate(530, 28)">
  <text x="0" y="0" font-size="12" fill="#10b981" font-family="ui-monospace,Consolas,monospace" font-weight="700" letter-spacing="1.2">
    OPENCV &#183; COMPUTER VISION &#183; EV PREEMPTION
  </text>
  <text x="0" y="38" font-size="34" fill="#ffffff" font-family="Georgia,serif" font-weight="bold" font-style="italic">
    Adaptive Signals
  </text>
  <text x="0" y="64" font-size="13" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif">
    MOG2 background subtraction &#183; Dynamic queue scaling (8s–35s).
  </text>
</g>

<!-- Traffic Visual Diagram -->
<g transform="translate(530, 110)">
  <!-- Queue Density Bar -->
  <text x="0" y="14" fill="#94a3b8" font-family="ui-monospace,Consolas,monospace" font-size="11">APPROACH QUEUE: 82%</text>
  <rect x="0" y="24" width="260" height="12" rx="3" fill="#1e293b"/>
  <rect x="0" y="24" width="213" height="12" rx="3" fill="#10b981"/>

  <!-- Dynamic Phase Timing Display -->
  <rect x="275" y="12" width="170" height="32" rx="4" fill="#111c33" stroke="#10b981" stroke-width="1"/>
  <text x="287" y="32" fill="#a7f3d0" font-family="ui-monospace,Consolas,monospace" font-size="11" font-weight="700">GREEN TIME: 32s</text>

  <!-- Emergency Vehicle Override Banner -->
  <g transform="translate(0, 68)">
    <rect width="446" height="44" rx="6" fill="#1f1d2e" stroke="#ef4444" stroke-width="1.2"/>
    <circle cx="20" cy="22" r="6" class="siren"/>
    <text x="36" y="26" fill="#fecaca" font-family="ui-monospace,Consolas,monospace" font-size="12" font-weight="700">
      EV PREEMPTION ACTIVE: Emergency Green-Wave Override
    </text>
  </g>
</g>
</svg>"""


def generate_session():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 205" role="img">
<title>ID-SHIELD Forensics Vault - Verified Session Replay</title>
<style>
  text { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
  .row1 { animation: r1 9s infinite; }
  .row2 { animation: r2 9s infinite; }
  .row3 { animation: r3 9s infinite; }
  @keyframes r1 { 0% { opacity: .15; } 12%, 95% { opacity: 1; } }
  @keyframes r2 { 0%, 23% { opacity: .15; } 40%, 95% { opacity: 1; } }
  @keyframes r3 { 0%, 49% { opacity: .15; } 66%, 95% { opacity: 1; } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>
<rect width="960" height="205" rx="8" fill="#0d111d"/>
<rect x="0" width="5" height="205" rx="2" fill="#00f2fe"/>
<path d="M 25 50 H 935" stroke="#1e293b" stroke-width="1.5"/>

<g font-size="16" fill="#38bdf8">
  <text x="28" y="34">faris@systems-lab ~/id-shield-forensics</text>
  <text x="932" y="34" text-anchor="end" fill="#64748b">REPLAY // EVIDENCE_PIPELINE</text>
</g>

<g font-size="18" fill="#f1f5f9">
  <text class="row1" x="28" y="90">[ 01 &#183; INGEST ]    Accept multi-document evidence bundle with role-based access control.</text>
  <text class="row2" x="28" y="130">[ 02 &#183; CORRELATE ] Cross-reference OCR fields, EXIF anomalies, and face embeddings across records.</text>
  <text class="row3" x="28" y="170">[ 03 &#183; SEAL ]      Commit tamper-evident Merkle hash to audit journal with cited human verdict.</text>
</g>
</svg>"""


def main():
    write_svg("identity.svg", generate_identity())
    write_svg("linkedin.svg", generate_linkedin())
    write_svg("email.svg", generate_email())
    write_svg("casevault-forensics.svg", generate_casevault_forensics())
    write_svg("project-reel.svg", generate_project_reel())
    write_svg("session.svg", generate_session())
    print("All profile SVG assets built successfully.")


if __name__ == "__main__":
    main()
