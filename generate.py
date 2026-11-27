"""
Generate Faris Ruknuddin's GitHub profile README.
Editorial-grade systems portfolio highlighting Full-Stack, Backend Systems, and Applied AI.
Featured: Shelfday.
Selected: Cueproof, TarkAI, Vaani Clinical, NephroGuard, Kuber Data Core.
"""
import argparse
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parent


def api(path):
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    if token:
        request = urllib.request.Request(
            "https://api.github.com/" + path,
            headers={
                "Authorization": "Bearer " + token,
                "Accept": "application/vnd.github+json",
                "User-Agent": "systems-lab-profile",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    try:
        result = subprocess.run(["gh", "api", path], capture_output=True, encoding="utf-8", check=True)
        return json.loads(result.stdout)
    except (FileNotFoundError, subprocess.SubprocessError):
        request = urllib.request.Request(
            "https://api.github.com/" + path,
            headers={"User-Agent": "systems-lab-profile"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)


def fetch_repos(username):
    repos = []
    page = 1
    while True:
        batch = api(f"users/{username}/repos?type=owner&per_page=100&page={page}")
        if not isinstance(batch, list):
            raise ValueError("GitHub did not return a repository list")
        repos.extend(batch)
        if len(batch) < 100:
            return repos
        page += 1


def public_repos(repos, username):
    return sorted(
        (r for r in repos if r.get("private") is False
         and r.get("owner", {}).get("login", "").lower() == username.lower()),
        key=lambda r: r["name"].lower(),
    )


def esc(value):
    return html.escape(str(value)).replace("|", "&#124;").replace("\n", " ")


def render(config, repos):
    visible = public_repos(repos, config["username"])

    lines = [
        '<img src="./assets/identity.svg?v=v3" width="100%" alt="Faris Ruknuddin - Full-Stack &amp; Backend Software Engineer · Applied AI">',
        "",
        f'<p><a href="{config["portfolio_url"]}"><img src="./assets/portfolio.svg?v=glacier" width="32.5%" alt="Open Faris Ruknuddin\'s Digital Workshop portfolio"></a> <a href="{config["linkedin"]}"><img src="./assets/linkedin.svg?v=glacier" width="32.5%" alt="Open Faris Ruknuddin\'s LinkedIn profile"></a> <a href="mailto:{config["email"]}"><img src="./assets/email.svg?v=glacier" width="32.5%" alt="Email Faris"></a></p>',
        "",
        "### `whoami`",
        "",
        "- 🎓 I'm a final-year **Computer Science (AI & ML)** engineering student at AITM, Bhatkal (Class of 2027).",
        "",
        "- 💻 I build **backend systems and full-stack software** in Python and TypeScript, with a focus on reliable APIs, structured data workflows, and local-first architecture.",
        "",
        "- ⚙️ I founded **Omnimate** and led a team delivering client software, alongside internships covering retail platforms, applied AI, machine learning, and cloud infrastructure.",
        "",
        "- 🛡️ On the side, I'm exploring **cybersecurity**—learning how systems fail under attack and how to design software with defensible boundaries.",
        "",
        "- 🔨 I put real effort into verifiable engineering: writing clean tests, handling failure modes upfront, and making edge cases explicit.",
        "",
        "<br>",
        "",
        "### GitHub activity",
        "",
        f'<a href="https://github.com/{config["username"]}?tab=overview#js-contribution-activity"><img src="./contrib-heatmap.svg" width="100%" alt="My rolling GitHub contribution calendar with activity heatmap"></a>',
        "",
        "<br>",
        "",
        "### Flagship builds",
        "",
        "#### 🛡️ [TraceGuard ↗](https://github.com/ZephyrusZorro/traceguard)",
        "",
        "Causal multi-agent failure attribution (**C³-Attributor**), CaMeL-inspired prompt-injection capability firewall, and time-travel counterfactual replay for OpenTelemetry GenAI traces (`Python`, `FastAPI`, `React 19`, `TypeScript`, `MCP`).",
        "",
        "#### 🔬 [PARALLAX v2.0 ↗](https://github.com/ZephyrusZorro/parallax)",
        "",
        "Neuro-symbolic multimodal causal digital twin & counterfactual resilience engine combining invertible SCMs, FLIR/optical inspection, an 8-agent council, Pearl `do()` simulations, and SHA-256 audit governance (`Python`, `FastAPI`, `React`, `MCP`, `Docker`).",
        "",
        "#### 🎙️ [RelayDesk 2.0 ↗](https://github.com/ZephyrusZorro/relaydesk)",
        "",
        "Voice-enabled IT support operations workbench orchestrated in n8n with three local Ollama specialist agents, a durable SQLite lease worker, and versioned BM25+RRF hybrid RAG (`Python`, `FastAPI`, `n8n`, `LangChain`, `Ollama`, `Docker`).",
        "",
        "#### 📈 [Market Cortex ↗](https://github.com/ZephyrusZorro/market-cortex)",
        "",
        "Local-first, point-in-time market data, analytics, and evidence-grounded quantitative research workstation with content-addressed Parquet manifests, DuckDB, PostgreSQL, and Next.js.",
        "",
        "#### 🪵 [Offcut Atlas ↗](https://github.com/ZephyrusZorro/offcut-atlas)",
        "",
        "Local-first material planning workbench for picture-framing studios turning commissions into verified cut drawings, traceable offcut racks, and two-order lookahead simulations (`Python 3.12`, `SQLite`).",
        "",
        "#### 💹 [CRYPTOZ ↗](https://cryptoz-seven.vercel.app) · [Source](https://github.com/ZephyrusZorro/cryptoz)",
        "",
        "Crypto market research workstation with live Binance feeds, chart studies, market breadth, and paper trading — deployed live on Vercel.",
        "",
        "#### 🍲 [Shelfday](https://github.com/ZephyrusZorro/shelfday)",
        "",
        '<a href="https://github.com/ZephyrusZorro/shelfday"><img src="./assets/shelfday-hero.svg" width="100%" alt="Shelfday: illustrated kitchen stock prep and closing reconciliation workbench. Open the project."></a>',
        "",
        "**What if a kitchen could track batch expiry before the morning rush?** Small commercial kitchens need to know which ingredient batch to use first and reconcile what happened before closing the day. I built a daily prep and perishable-stock workbench using TypeScript, React, and Cloudflare D1 with SQLite — featuring earliest-expiry-first (FEFO) batch allocation, atomic shortage rollback, and locked closing summaries.",
        "",
        "[Explore Shelfday ↗](https://github.com/ZephyrusZorro/shelfday) · [View architecture docs](https://github.com/ZephyrusZorro/shelfday#readme)",
        "",
        "### More selected engineering work",
        "",
        '<img src="./assets/project-reel.svg?v=glacier" width="100%" alt="Illustrated project reel: Cueproof caption revision review and TarkAI AST code practice studio.">',
        "",
        "#### 🎬 [Cueproof ↗](https://zephyruszorro.github.io/cueproof/) · [Source](https://github.com/ZephyrusZorro/cueproof)",
        "",
        "Private-by-design browser caption revision desk for comparing SRT and WebVTT tracks against synchronized video with IndexedDB storage, follow-up rounds, and portable JSON backups.",
        "",
        "#### 🛡️ [Vigil ↗](https://github.com/ZephyrusZorro/vigil)",
        "",
        "Local-first unified deadline, compliance, license, and contract intelligence platform with a deterministic 0–100 risk engine, alert thresholds, and native Node.js SQLite WAL storage (`TypeScript`, `React`, `Express`, `SQLite`).",
        "",
        "#### 🧠 [TarkAI (तर्क) ↗](https://github.com/ZephyrusZorro/tark-ai)",
        "",
        "Local Python practice studio combining Python 3.12 AST semantic introspection, Halstead complexity metrics, timed subprocess test runs, Socratic mentoring tiers, and Leitner spaced review.",
        "",
        "<br>",
        "",
        "### `cat field-notes/shelfday`",
        "",
        '<img src="./assets/session.svg?v=glacier" width="100%" alt="Shelfday batch allocation and rollback sequence: tag intake, deduct FEFO, and restore cancelled portions.">',
        "",
        "The hardest bug in inventory software isn't adding numbers—it's dealing with partial cancellations. When an order is cancelled halfway through kitchen prep, you cannot simply delete the line item. You have to return that exact portion to the specific lot it was drawn from, or your expiry sequence breaks. Making rollback an atomic state transition instead of an afterthought is what makes the ledger dependable. [Shelfday source code](https://github.com/ZephyrusZorro/shelfday)",
        "",
        "### On my workbench",
        "",
        "**LeakageGuard** · My final-year B.E. project. Developer tooling that checks Python ML workflows and datasets for preprocessing leakage, train/test duplicate records, group overlap, and temporal target leakage before models are evaluated on contaminated data.",
        "",
        "**AI Reliability & Local-First Systems** · Building verifiable agentic systems (causal attribution, prompt-injection capability firewalls, counterfactual replay) alongside local-first tools backed by SQLite, DuckDB, and IndexedDB.",
        "",
        "### Tools in practice",
        "",
        "| Area | Where I use it |",
        "| --- | --- |",
        "| **Python & FastAPI** | Backend APIs, causal/ML engines, and data pipelines across TraceGuard, PARALLAX, RelayDesk, Market Cortex, Offcut Atlas, and TarkAI. |",
        "| **TypeScript & React** | Interactive workbenches and dashboards in TraceGuard, PARALLAX, Shelfday, Cueproof, Vigil, and CRYPTOZ. |",
        "| **Databases & Storage** | SQLite (WAL/FTS5), PostgreSQL, DuckDB, Parquet, Cloudflare D1, and IndexedDB for local-first and analytical workloads. |",
        "| **Applied AI & Security** | Multi-agent orchestration (n8n, Ollama, MCP), OpenTelemetry GenAI tracing, prompt-injection firewalls, AST analysis, and causal SCMs. |",
        "| **DevOps & Verification** | Automated pytest/Playwright/Vitest suites, Docker Compose, GitHub Actions CI/CD, and Vercel deployments. |",
        "",
        "### A few things I've learned",
        "",
        "**Model the failure mode before the happy path.** In Shelfday, ingredients don't just get used; batches expire, orders get cancelled, and count mistakes happen. Designing the rollback and closing reconciliation first made the day-to-day workflow much simpler to reason about.",
        "",
        "**Static checks are cheaper than runtime surprises.** In LeakageGuard, checking code structure with the Python AST catches methodological mistakes in milliseconds, before anyone trains a model on contaminated data.",
        "",
        "**Keep state inspectable.** Whether it's a FHIR bundle in Vaani Clinical or a relationship graph in Kuber Data Core, software is easier to trust when you can point to the exact record and timestamp that produced a number.",
        "",
        "<details>",
        "<summary>Systems Lab artwork &amp; portrait</summary>",
        "",
        '<p align="center">',
        '  <img src="faris-profile.jpg" width="380" style="border-radius:12px;" alt="Faris Ruknuddin Portrait" />',
        "</p>",
        "",
        '<p align="center">',
        '  <img src="faris-ascii.svg" width="416" alt="Faris\'s animated ASCII portrait" />',
        '  <img src="stats.svg" width="416" alt="Repository activity" />',
        "</p>",
        "",
        "</details>",
        "",
        "<details>",
        f"<summary>{len(visible)} public repositories</summary>",
        "",
        "| Repository | Description | Language |",
        "| :--- | :--- | :--- |",
    ]

    for repo in visible:
        name = repo["name"]
        note = config["repository_notes"].get(name, repo.get("description") or "Public repository.")
        if repo.get("archived"):
            note = "Archived · " + note
        language = repo.get("language") or "-"
        lines.append(f"| [{esc(name)}]({repo['html_url']}) | {esc(note)} | {esc(language)} |")

    lines.extend([
        "",
        "</details>",
        "",
        "### Get in touch",
        "",
        "I'm a final-year AI & ML student in Bhatkal, interested in internships and graduate roles in software engineering, backend systems, and full-stack development. If you work on reliable data workflows, local-first tools, or useful developer software, I'd enjoy hearing from you.",
        "",
        f"[Digital Workshop]({config['portfolio_url']}) · [LinkedIn]({config['linkedin']}) · [Email](mailto:{config['email']})",
        "",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repos", type=Path, help="Offline GitHub API JSON fixture")
    parser.add_argument("--output", type=Path, default=ROOT / "README.md")
    args = parser.parse_args()

    config = json.loads((ROOT / "profile.json").read_text(encoding="utf-8-sig"))
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", config["username"]):
        raise ValueError("Invalid GitHub username")

    repos = json.loads(args.repos.read_text(encoding="utf-8-sig")) if args.repos else fetch_repos(config["username"])
    content = render(config, repos)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_suffix(".tmp")
    temp.write_text(content, encoding="utf-8", newline="\n")
    temp.replace(args.output)
    print(f"Generated {args.output.name}: {len(public_repos(repos, config['username']))} public repos.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Generation failed; existing README preserved: {error}", file=sys.stderr)
        sys.exit(1)
