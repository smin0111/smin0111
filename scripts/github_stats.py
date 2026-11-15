#!/usr/bin/env python3
"""GitHub 공개 API로 프로필 통계를 모아 언어 비율 SVG 카드를 만듭니다.

- assets/github-langs.svg : 내 저장소(포크 제외)의 언어별 코드 크기 비율

외부 통계 서비스에 기대지 않도록 GitHub Actions에서 매일 실행해 저장소에 커밋합니다.
토큰은 GITHUB_TOKEN 환경 변수로만 받고 출력하지 않습니다.
"""
import json
import os
import sys
import urllib.request
from datetime import datetime
from html import escape
from pathlib import Path

USER = os.environ.get("STATS_USER", "smin0111")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = Path(__file__).resolve().parent.parent / "assets"

LANG_COLORS = {
    "Java": "#b07219", "JavaScript": "#f1e05a", "TypeScript": "#3178c6", "Python": "#3572A5",
    "HTML": "#e34c26", "CSS": "#663399", "Shell": "#89e051", "Kotlin": "#A97BFF",
    "Dockerfile": "#384d54", "Swift": "#F05138", "Objective-C": "#438eff", "Ruby": "#701516",
}
FALLBACK = ["#5eead4", "#818cf8", "#fcd34d", "#f0abfc", "#86efac", "#fda4af"]


def get(path):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-stats")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def collect():
    user = get(f"/users/{USER}")
    repos, page = [], 1
    while True:
        batch = get(f"/users/{USER}/repos?type=owner&per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    own = [r for r in repos if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in own)
    langs = {}
    for r in own:
        for name, size in get(f"/repos/{USER}/{r['name']}/languages").items():
            langs[name] = langs.get(name, 0) + size
    since = datetime.strptime(user["created_at"][:10], "%Y-%m-%d").strftime("%B %Y")
    return {
        "name": user.get("login", USER), "since": since,
        "repos": user.get("public_repos", 0), "stars": stars,
        "followers": user.get("followers", 0), "langs": langs,
    }


STYLE = """
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#16213e"/><stop offset="1" stop-color="#0f172a"/>
  </linearGradient>
</defs>
<style>
  .t{font:700 20px 'Segoe UI',Helvetica,Arial,sans-serif;fill:#e2e8f0}
  .s{font:13px ui-monospace,SFMono-Regular,Menlo,monospace;fill:#94a3b8}
  .n{font:700 30px 'Segoe UI',Helvetica,Arial,sans-serif;fill:#5eead4}
  .l{font:13px 'Segoe UI',Helvetica,Arial,sans-serif;fill:#cbd5e1}
  .p{font:13px ui-monospace,SFMono-Regular,Menlo,monospace;fill:#cbd5e1}
</style>
"""


def stats_svg(d):
    w, h = 420, 210
    boxes = [("public repos", d["repos"]), ("stars earned", d["stars"]), ("followers", d["followers"])]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">', STYLE,
             f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="14" fill="url(#bg)" stroke="#1e293b"/>',
             f'<text x="24" y="42" class="t">{escape(d["name"])}</text>',
             f'<text x="24" y="64" class="s">on GitHub since {escape(d["since"])}</text>']
    bw, gap, x0, y0 = 116, 10, 24, 84
    for i, (label, value) in enumerate(boxes):
        x = x0 + i * (bw + gap)
        parts += [f'<rect x="{x}" y="{y0}" width="{bw}" height="84" rx="10" fill="#0b1220" stroke="#1e293b"/>',
                  f'<text x="{x + bw/2}" y="{y0 + 44}" text-anchor="middle" class="n">{value}</text>',
                  f'<text x="{x + bw/2}" y="{y0 + 68}" text-anchor="middle" class="l">{label}</text>']
    parts += [f'<text x="24" y="{h - 18}" class="s">counted from the public API</text>', "</svg>"]
    return "\n".join(parts)


def langs_svg(d):
    w, h = 420, 210
    total = sum(d["langs"].values()) or 1
    top = sorted(d["langs"].items(), key=lambda kv: -kv[1])[:6]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">', STYLE,
             f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="14" fill="url(#bg)" stroke="#1e293b"/>',
             '<text x="24" y="42" class="t">Languages by code size</text>',
             '<clipPath id="bar"><rect x="24" y="62" width="372" height="10" rx="5"/></clipPath>',
             '<g clip-path="url(#bar)"><rect x="24" y="62" width="372" height="10" fill="#1e293b"/>']
    x = 24.0
    colors = {}
    for i, (name, size) in enumerate(top):
        colors[name] = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
        seg = 372 * size / total
        parts.append(f'<rect x="{x:.2f}" y="62" width="{seg:.2f}" height="10" fill="{colors[name]}"/>')
        x += seg
    parts.append("</g>")
    for i, (name, size) in enumerate(top):
        col, row = i % 2, i // 2
        lx, ly = 24 + col * 196, 104 + row * 30
        parts += [f'<rect x="{lx}" y="{ly - 10}" width="11" height="11" rx="3" fill="{colors[name]}"/>',
                  f'<text x="{lx + 18}" y="{ly}" class="l">{escape(name)}</text>',
                  f'<text x="{lx + 176}" y="{ly}" text-anchor="end" class="p">{100 * size / total:.1f}%</text>']
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    data = collect()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "github-langs.svg").write_text(langs_svg(data), encoding="utf-8")
    print(f"repos={data['repos']} stars={data['stars']} followers={data['followers']} langs={len(data['langs'])}")


if __name__ == "__main__":
    sys.exit(main())
