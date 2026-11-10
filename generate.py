"""
Generate Faris Ruknuddin's GitHub profile README.
Editorial-grade systems portfolio matching the glacier aesthetic, structure, and tone of 7awwad.
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
        '<img src="./assets/identity.svg?v=glacier" width="100%" alt="Faris Ruknuddin - animated terminal ASCII portrait, backend systems and applied AI">',
        "",
        f'<p><a href="{config["portfolio_url"]}"><img src="./assets/portfolio.svg?v=glacier" width="32.5%" alt="Open Faris Ruknuddin\'s Digital Workshop portfolio"></a> <a href="{config["linkedin"]}"><img src="./assets/linkedin.svg?v=glacier" width="32.5%" alt="Open Faris Ruknuddin\'s LinkedIn profile"></a> <a href="mailto:{config["email"]}"><img src="./assets/email.svg?v=glacier" width="32.5%" alt="Email Faris"></a></p>',
        "",
        "### `whoami`",
        "",
        "- 🎓 I'm a final-year **Computer Science (AI & ML)** engineering student at AITM, Bhatkal.",
        "",
        "- 🛡️ I'm exploring **cybersecurity**, with a focus on application security, defensive engineering, and understanding how attackers find weaknesses in software. I want to excel in this field by combining offensive curiosity with defensible systems architecture.",
        "",
        "- ⚙️ I founded **Omnimate** and led a seven-person team delivering client software. Across five internships in retail software, applied AI, machine learning, and cloud infrastructure, I've focused on what connects the interface to the data moving behind it.",
        "",
        "- 🔨 I put real effort into verifiable engineering: writing tests, building local-first tools with offline resilience, and making edge cases explicit instead of sweeping them under the rug.",
        "",
        "<br>",
        "",
        "### GitHub activity",
        "",
        f'<a href="https://github.com/{config["username"]}?tab=overview#js-contribution-activity"><img src="./contrib-heatmap.svg" width="100%" alt="My rolling GitHub contribution calendar with activity heatmap"></a>',
        "",
        "<br>",
        "",
        "### Featured build",
        "",
        "#### 🚦 [Adaptive Traffic Signals](https://github.com/ZephyrusZorro/ai-traffic-signal-optimization)",
        "",
        '<a href="https://github.com/ZephyrusZorro/ai-traffic-signal-optimization"><img src="./assets/intersection.svg" width="100%" alt="Adaptive Traffic Signals: an illustrated intersection with a queue moving when the light turns green. Open the project."></a>',
        "",
        "**What if a traffic light could see the queue?** Mohammed Jawwad and I built an OpenCV simulation that estimates traffic density in each approach and adjusts the green phase between **8 and 35 seconds**. The illustration shows the idea; the repository includes intersection footage and the Python controller.",
        "",
        "[Explore the project ↗](https://github.com/ZephyrusZorro/ai-traffic-signal-optimization) · [Read the signal logic](https://github.com/ZephyrusZorro/ai-traffic-signal-optimization/blob/main/traffic_logic.py)",
        "",
        "### Selected projects",
        "",
        '<img src="./assets/project-reel.svg?v=glacier" width="100%" alt="Illustrated project reel. Shelfday allocates ingredient batches with rollback; Cueproof compares subtitle revisions with timecoded diffs.">',
        "",
        "#### 🍲 [Shelfday ↗](https://github.com/ZephyrusZorro/shelfday)",
        "",
        "Kitchen operations need to know which ingredient batch expires first before the rush starts. I built an intake, prep, and reconciliation workbench for small commercial kitchens.",
        "",
        "**Inside Shelfday** · Ingredients don't just get allocated—they run short, expire, or get cancelled mid-shift. Shelfday implements earliest-expiry-first (FEFO) allocation across batches and keeps closing records locked. Making rollback an explicit database state transition rather than an error handler kept inventory honest when cancellations occurred.",
        "",
        "#### 🎬 [Cueproof ↗](https://zephyruszorro.github.io/cueproof/)",
        "",
        "Caption revisions are frustrating to review when wording changes, timing drifts, and reviewer notes live in separate documents. I built a browser-based caption revision desk to compare reference and revision subtitle tracks.",
        "",
        "**Inside Cueproof** · The parser, text comparisons, and audio-video playback run entirely in the browser using IndexedDB. Reviewers see cue-level text additions and removals alongside synchronized video, with follow-up rounds and portable JSON backups. [Try the live demo ↗](https://zephyruszorro.github.io/cueproof/)",
        "",
        "#### 📊 [Kuber Data Core](https://github.com/ZephyrusZorro/kuber-datacore)",
        "",
        "- **The problem** · Financial research becomes hard to trust when changing numbers lose their connection to original filings.",
        "",
        "- **Structure** · Uses an asynchronous crawler and FIBO/EDGAR ontology schemas to extract and snapshot corporate relationship graphs.",
        "",
        "- **Repeatability** · Pinned pipelines ensure that every calculated metric can be traced back to its raw source document.",
        "",
        "<br>",
        "",
        "#### 🛡️ [CaseVault](https://github.com/ZephyrusZorro/case-vault)",
        "",
        "- **Access boundaries** · Role-aware permissions determine which investigator can access specific case files.",
        "",
        "- **Evidence tracking** · Tracks revisions, access history, and evidence attachments to legal case files.",
        "",
        "- **System architecture** · Backed by a FastAPI application with database-level isolation between case dossiers.",
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
        "**LeakageGuard** · My final-year B.E. project. I'm building a static code and dataset auditor that inspects Python ML workflows using Abstract Syntax Trees (AST). It catches preprocessing leakage, train/test duplicate records, and temporal lookahead before models are evaluated on contaminated data.",
        "",
        "**Cybersecurity & Threat Monitoring** · I'm exploring offensive and defensive security through hands-on labs (Wireshark packet inspection, Nmap network scanning, and OWASP Top 10 vulnerabilities). Alongside that, I'm prototyping a local dashboard that tracks public ransomware disclosures and distinguishes verified security incidents from unconfirmed extortion claims.",
        "",
        "### Tools in practice",
        "",
        "| Area | Where I use it |",
        "| --- | --- |",
        "| **Python & OpenCV** | Compute real-time vehicle density and schedule signal phases in Adaptive Traffic Signals; build AST analysis rules in LeakageGuard. |",
        "| **TypeScript & React** | Build client-side workbenches like Cueproof and Shelfday; handle IndexedDB storage, cue diffing, and media synchronization. |",
        "| **FastAPI & SQLite / Postgres** | Handle authenticated routes, schema constraints, and relation graphs in Kuber Data Core and CaseVault. |",
        "| **Cybersecurity tooling** | Inspect network traffic, analyze service exposure, and test web application input boundaries in lab environments. |",
        "| **Git & GitHub Actions** | Keep commits traceable, run automated test suites, and generate this profile's live telemetry artwork. |",
        "",
        "### A few things I've learned",
        "",
        "**Model the failure mode before the happy path.** In Shelfday, ingredients don't just get used; batches expire, orders get cancelled, and count mistakes happen. Designing the rollback and closing reconciliation first made the day-to-day workflow much simpler to reason about.",
        "",
        "**Static checks are cheaper than runtime surprises.** In LeakageGuard, checking code structure with the Python AST catches methodological mistakes in milliseconds, before anyone trains a model on contaminated data.",
        "",
        "**Keep state inspectable.** Whether it's an evidence audit log in CaseVault or a dataset manifest in Market Cortex, software is easier to trust when you can point to the exact record and timestamp that produced a number.",
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
        "I'm a final-year AI & ML student in Bhatkal, interested in internships and graduate roles in software engineering, backend systems, and cybersecurity. If you work on local-first tools, verifiable data workflows, or application security, I'd enjoy hearing how you tackle hard edge cases.",
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
