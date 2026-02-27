#!/usr/bin/env python3
"""Download XKCD comics for L00 Prerequisites mini-lectures."""

import json
import os
import urllib.request
import urllib.error

COMICS = [
    (1838, "1838_machine_learning.png"),
    (1425, "1425_tasks.png"),
    (2173, "2173_trained_a_neural_net.png"),
]

def download_xkcd(num, filename):
    """Download a single XKCD comic via the JSON API."""
    api_url = f"https://xkcd.com/{num}/info.0.json"
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    if os.path.exists(out_path):
        print(f"  [SKIP] {filename} already exists")
        return True

    try:
        print(f"  Fetching metadata for XKCD #{num}...")
        req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        img_url = data["img"]

        print(f"  Downloading {img_url} -> {filename}")
        img_req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(img_req, timeout=30) as img_resp:
            with open(out_path, "wb") as f:
                f.write(img_resp.read())

        print(f"  [OK] {filename} ({os.path.getsize(out_path)} bytes)")
        return True

    except (urllib.error.URLError, urllib.error.HTTPError, OSError, json.JSONDecodeError) as e:
        print(f"  [FAIL] XKCD #{num}: {e}")
        return False


if __name__ == "__main__":
    print("Downloading XKCD comics for L00 Prerequisites...")
    results = []
    for num, fname in COMICS:
        ok = download_xkcd(num, fname)
        results.append((num, fname, ok))

    print("\n--- Summary ---")
    for num, fname, ok in results:
        status = "OK" if ok else "FAILED"
        print(f"  XKCD #{num} ({fname}): {status}")

    failed = sum(1 for _, _, ok in results if not ok)
    if failed:
        print(f"\n{failed} download(s) failed. Place images manually if needed.")
