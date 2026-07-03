#!/usr/bin/env python3
"""Register this repo's conductor/*_def.json workflow definition(s) onto Conductor.
    CONDUCTOR_URL=http://localhost:8000 python conductor/register.py
"""
import glob, json, os, urllib.request, urllib.error

CONDUCTOR = os.environ.get("CONDUCTOR_URL", "http://localhost:8000")
here = os.path.dirname(os.path.abspath(__file__))

for f in sorted(glob.glob(os.path.join(here, "*_def.json"))):
    name = json.load(open(f)).get("name", "?")
    req = urllib.request.Request(
        f"{CONDUCTOR}/api/metadata/workflow",
        data=open(f, "rb").read(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=15)
        print(f"registered  {name}  ({os.path.basename(f)})")
    except urllib.error.HTTPError as e:
        print(f"FAILED {name}: HTTP {e.code} {e.read().decode(errors='replace')[:200]}")
    except Exception as e:
        print(f"FAILED {name}: {e}")
