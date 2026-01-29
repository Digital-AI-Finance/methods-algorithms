"""Download XKCD comics for L01 slides.

XKCD comics are licensed under CC BY-NC 2.5.
Attribution is required when using these images.

Usage: python download_xkcd.py
"""
import urllib.request
from pathlib import Path

# XKCD comic URLs and metadata
XKCD_COMICS = {
    "1725_linear_regression": {
        "url": "https://imgs.xkcd.com/comics/linear_regression.png",
        "title": "Linear Regression",
        "attribution": "XKCD #1725 by Randall Munroe (CC BY-NC 2.5)"
    },
    "2048_curve_fitting": {
        "url": "https://imgs.xkcd.com/comics/curve_fitting.png",
        "title": "Curve-Fitting",
        "attribution": "XKCD #2048 by Randall Munroe (CC BY-NC 2.5)"
    },
    "605_extrapolating": {
        "url": "https://imgs.xkcd.com/comics/extrapolating.png",
        "title": "Extrapolating",
        "attribution": "XKCD #605 by Randall Munroe (CC BY-NC 2.5)"
    }
}

def download_comics():
    """Download all XKCD comics to current directory."""
    output_dir = Path(__file__).parent

    for name, info in XKCD_COMICS.items():
        output_path = output_dir / f"{name}.png"

        if output_path.exists():
            print(f"Skipping {name} (already exists)")
            continue

        print(f"Downloading {name}...")
        try:
            urllib.request.urlretrieve(info["url"], output_path)
            print(f"  Saved to {output_path}")
        except Exception as e:
            print(f"  Error downloading {name}: {e}")

    print("\nDone! Remember to include attribution in slides:")
    for name, info in XKCD_COMICS.items():
        print(f"  {name}: {info['attribution']}")

if __name__ == "__main__":
    download_comics()
