"""Convert Beamer LaTeX slides to Reveal.js HTML presentations."""

import subprocess
from pathlib import Path
import shutil

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
SLIDES_SRC = PROJECT_ROOT / "slides"
SLIDES_OUT = PROJECT_ROOT / "docs" / "slides"

# Reveal.js CDN
REVEALJS_CDN = "https://unpkg.com/reveal.js@4.5.0"

def convert_tex_to_revealjs(tex_file: Path, output_dir: Path) -> Path:
    """Convert a single .tex file to Reveal.js HTML."""

    # Output filename
    output_html = output_dir / f"{tex_file.stem}.html"

    # Pandoc command
    cmd = [
        "pandoc",
        str(tex_file),
        "-t", "revealjs",
        "-s",  # standalone
        "--mathjax",
        "-V", f"revealjs-url={REVEALJS_CDN}",
        "-V", "theme=white",
        "-V", "transition=slide",
        "-V", "slideNumber=true",
        "-V", "hash=true",
        "-V", "width=1600",
        "-V", "height=900",
        "--slide-level=2",
        "-o", str(output_html)
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=tex_file.parent)
        if result.returncode == 0:
            print(f"  OK: {tex_file.name} -> {output_html.name}")
            return output_html
        else:
            print(f"  ERROR: {tex_file.name}")
            print(f"    {result.stderr[:200]}")
            return None
    except Exception as e:
        print(f"  EXCEPTION: {tex_file.name} - {e}")
        return None


def convert_all():
    """Convert all Beamer .tex files to Reveal.js."""

    # Ensure output directory exists
    SLIDES_OUT.mkdir(parents=True, exist_ok=True)

    # Find all lecture .tex files
    tex_files = sorted(SLIDES_SRC.rglob("L0*_*.tex"))

    print(f"Found {len(tex_files)} .tex files to convert\n")

    converted = []
    failed = []

    for tex_file in tex_files:
        result = convert_tex_to_revealjs(tex_file, SLIDES_OUT)
        if result:
            converted.append(result)
        else:
            failed.append(tex_file)

    print(f"\n{'='*50}")
    print(f"Converted: {len(converted)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed files:")
        for f in failed:
            print(f"  - {f}")

    return converted


if __name__ == "__main__":
    convert_all()
