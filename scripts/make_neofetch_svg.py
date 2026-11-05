#!/usr/bin/env python3
"""
Generates an animated Neofetch-style system info card (neofetch-card.svg)
for Faris Ruknuddin (ZephyrusZorro).

Dimensions: 840 x 880 (matches ASCII portrait and stats.svg canvas).
Each row fades and slides in on a staggered delay, followed by a color palette bar.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "neofetch-card.svg")

W, H = 840, 880
PAD = 32
TITLEBAR_H = 34

BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
INK = "#e6edf3"
CYAN = "#22d3ee"
GREEN = "#39d353"
GOLD = "#f2cc60"
PURPLE = "#bc8cff"
RED = "#ff7b72"
BLUE = "#58a6ff"

# Systems lab spec entries
SPECS = [
    ("OS", "Ubuntu 24.04 LTS x86_64", INK),
    ("Host", "Omnimate Systems Node [Production]", CYAN),
    ("Kernel", "6.8.0-applied-ai-pipeline", MUTED),
    ("Uptime", "AIML Student @ AITM · Continuous Builder", INK),
    ("Shell", "zsh 5.9 (systems-lab-theme)", MUTED),
    ("Role", "Backend Developer & Applied AI Engineer", GREEN),
    ("Focus", "Turning messy inputs into useful systems", GOLD),
    ("Core Stack", "Python · TypeScript · FastAPI · Node.js", CYAN),
    ("Vision & AI", "OpenCV · MediaPipe · scikit-learn · Agentic Workflows", PURPLE),
    ("Database", "PostgreSQL · Redis · Vector Store · SQLite", INK),
    ("Infrastructure", "Docker · GitHub Actions · AWS S3 · Linux", BLUE),
    ("Active Lab", "CaseVault · Omnimate Shots · Vox AI", GREEN),
    ("Locale", "Bhatkal, India [IST / UTC+5:30]", MUTED),
]

COLORS = [
    "#ff7b72", "#f2cc60", "#39d353", "#22d3ee",
    "#58a6ff", "#bc8cff", "#e6edf3", "#7d8590"
]

def render():
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '<style>',
        '.row { opacity: 0; animation: fadeSlide 0.5s cubic-bezier(0.16, 1, 0.3, 1) both; }',
        '@keyframes fadeSlide { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: translateX(0); } }',
        '.dot-bar { opacity: 0; animation: fadeIn 0.6s ease-out both; }',
        '@keyframes fadeIn { to { opacity: 1; } }',
        '@media (prefers-reduced-motion: reduce) { .row, .dot-bar { opacity: 1 !important; transform: none !important; animation: none !important; } }',
        '</style>',
        f'<defs><linearGradient id="neo_bg" x1="0" y1="0" x2="0" y2="1">',
        f'<stop offset="0%" stop-color="{BG2}"/><stop offset="100%" stop-color="{BG}"/>',
        '</linearGradient></defs>',
        f'<rect width="{W}" height="{H}" rx="12" fill="url(#neo_bg)"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
    ]

    # Traffic dots
    for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dot}"/>')
    parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
                 f'text-anchor="middle">faris@systems-lab: ~$ neofetch --details</text>')

    # ASCII Header Banner
    header_y = TITLEBAR_H + 42
    banner_lines = [
        r"  ____            _                            _____                    ",
        r" |_  /___ _ __  | |_  _   _ _ _ _  _ ___   |_  /___ _ _ _ _ ___    ",
        r"  / // -_) '_ \ | ' \| || | '_| || (_-<    / // _ \ '_| '_/ _ \   ",
        r" /___\___| .__/ |_||_\_,_|_|   \_,_/__/   /___\___/_| |_| \___/   ",
        r"         |_|                                                        ",
    ]
    for idx, bl in enumerate(banner_lines):
        y_pos = header_y + idx * 16
        safe_line = bl.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        parts.append(f'<text xml:space="preserve" x="{PAD}" y="{y_pos}" fill="{CYAN}" font-size="12" font-weight="700">{safe_line}</text>')

    sub_y = header_y + len(banner_lines) * 16 + 10
    parts.append(f'<text x="{PAD}" y="{sub_y}" font-size="15" font-weight="700" fill="{GREEN}">faris<tspan fill="{MUTED}">@</tspan>systems-lab</text>')
    parts.append(f'<line x1="{PAD}" y1="{sub_y+8}" x2="{W-PAD}" y2="{sub_y+8}" stroke="{FRAME}" stroke-dasharray="4 4"/>')

    # Specs Rows
    spec_start_y = sub_y + 36
    row_height = 36
    for i, (key, val, val_color) in enumerate(SPECS):
        ry = spec_start_y + i * row_height
        delay = 0.2 + i * 0.06
        parts.append(f'<g class="row" style="animation-delay:{delay:.2f}s">')
        parts.append(f'<text x="{PAD}" y="{ry}" font-size="16" font-weight="700" fill="{CYAN}">{key}</text>')
        parts.append(f'<text x="{PAD + 150}" y="{ry}" font-size="16" fill="{MUTED}">:</text>')
        parts.append(f'<text x="{PAD + 172}" y="{ry}" font-size="16" fill="{val_color}">{val}</text>')
        parts.append('</g>')

    # Terminal Palette Blocks
    palette_y = spec_start_y + len(SPECS) * row_height + 16
    parts.append(f'<g class="dot-bar" style="animation-delay:{0.2 + len(SPECS)*0.06 + 0.2:.2f}s">')
    for i, color in enumerate(COLORS):
        parts.append(f'<circle cx="{PAD + 16 + i*36}" cy="{palette_y}" r="11" fill="{color}"/>')
    parts.append('</g>')

    parts.append('</svg>')
    svg = "".join(parts)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Rendered {OUT}: {W} x {H} ({len(svg)//1024} KB)")

if __name__ == "__main__":
    render()
