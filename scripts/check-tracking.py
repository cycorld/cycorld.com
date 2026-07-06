#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "Google Tag Manager": "GTM-MTWNTBB",
    "Rybbit script": "https://rybbit.cycorld.com/api/script.js",
    "Rybbit site id": 'data-site-id="ca76392dfdfa"',
}

missing = []
for path in sorted(ROOT.rglob("*.html")):
    if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
        continue
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    for label, needle in REQUIRED.items():
        if needle not in text:
            missing.append(f"{rel}: missing {label} ({needle})")

if missing:
    print("Tracking check failed:")
    print("\n".join(missing))
    sys.exit(1)

print("Tracking check passed for all HTML files.")
