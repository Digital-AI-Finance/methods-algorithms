"""Convert Beamer LaTeX slides to enhanced Reveal.js HTML presentations.

Pipeline:
1. TexSoup-based parser converts .tex directly to Reveal.js sections
2. Chart PDFs converted to PNGs for web display
3. Template injection adds plugins and custom theme

Uses TexSoup for proper AST-based LaTeX parsing (no Pandoc needed).
"""

import subprocess
import re
import shutil
from pathlib import Path
from beamer_parser_v2 import BeamerParserV2 as BeamerParser

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
SLIDES_SRC = PROJECT_ROOT / "slides"
SLIDES_OUT = PROJECT_ROOT / "docs" / "slides"
IMAGES_OUT = SLIDES_OUT / "images"
TEMPLATE_FILE = Path(__file__).parent / "revealjs_template.html"

# Reveal.js CDN
REVEALJS_CDN = "https://unpkg.com/reveal.js@4.5.0"

# ML Color palette
COLOR_MAP = {
    'MLPurple': '#3333B2',
    'MLBlue': '#0066CC',
    'MLOrange': '#FF7F0E',
    'MLGreen': '#2CA02C',
    'MLRed': '#D62728',
    'MLLavender': '#ADADE0',
    'gray': '#666666',
}

# Wiki URL for QR codes
WIKI_URL = "https://digital-ai-finance.github.io/methods-algorithms/"


def convert_pdf_to_png(pdf_path: Path, output_dir: Path) -> Path:
    """Convert a PDF chart to PNG using pdf2image or ImageMagick."""
    png_name = f"{pdf_path.parent.name}.png"
    png_path = output_dir / png_name

    if png_path.exists():
        return png_path

    # Try pdf2image (Python)
    try:
        from pdf2image import convert_from_path
        images = convert_from_path(str(pdf_path), dpi=150, first_page=1, last_page=1)
        if images:
            images[0].save(str(png_path), 'PNG')
            return png_path
    except ImportError:
        pass
    except Exception:
        pass

    # Try ImageMagick
    try:
        cmd = ["magick", "convert", "-density", "150", str(pdf_path) + "[0]", str(png_path)]
        result = subprocess.run(cmd, capture_output=True, timeout=30)
        if result.returncode == 0 and png_path.exists():
            return png_path
    except Exception:
        pass

    # Try pdftoppm (poppler)
    try:
        cmd = ["pdftoppm", "-png", "-singlefile", "-r", "150", str(pdf_path), str(png_path.with_suffix(''))]
        result = subprocess.run(cmd, capture_output=True, timeout=30)
        if png_path.exists():
            return png_path
    except Exception:
        pass

    return None


def process_charts(tex_file: Path) -> dict:
    """Find and convert all chart PDFs for a lecture to PNGs."""
    lecture_dir = tex_file.parent
    chart_dirs = [d for d in lecture_dir.iterdir() if d.is_dir() and (d / "chart.pdf").exists()]

    # Create images subdirectory for this lecture
    lecture_name = lecture_dir.name
    images_subdir = IMAGES_OUT / lecture_name
    images_subdir.mkdir(parents=True, exist_ok=True)

    chart_map = {}
    for chart_dir in chart_dirs:
        pdf_path = chart_dir / "chart.pdf"
        png_path = convert_pdf_to_png(pdf_path, images_subdir)
        if png_path:
            # Map relative PDF path to web image path
            rel_pdf = f"{chart_dir.name}/chart.pdf"
            rel_png = f"images/{lecture_name}/{chart_dir.name}.png"
            chart_map[rel_pdf] = rel_png

    return chart_map




def create_enhanced_title_slide(metadata: dict) -> str:
    """Create an enhanced title slide with gradient background."""
    return f'''<section id="title-slide" data-background="linear-gradient(135deg, #3333B2 0%, #0066CC 100%)">
    <div style="color: white; text-align: center;">
        <h1 style="color: white; font-size: 2.5em; margin-bottom: 0.3em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{metadata['title']}</h1>
        <p style="font-size: 1.4em; color: #ADADE0; margin-bottom: 1.5em;">{metadata['subtitle']}</p>
        <p style="font-size: 1em; color: rgba(255,255,255,0.9);">{metadata['author']}</p>
        <div style="margin-top: 2em;">
            <img src="images/qr_wiki.png" alt="QR Code" style="width: 120px; height: 120px; background: white; padding: 8px; border-radius: 8px;" onerror="this.style.display='none'">
            <p style="font-size: 0.7em; color: rgba(255,255,255,0.7); margin-top: 0.5em;">Scan for course materials</p>
        </div>
    </div>
</section>'''


def apply_template(sections: list, metadata: dict, slide_name: str = "") -> str:
    """Apply the custom template to processed slides."""
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Template not found: {TEMPLATE_FILE}")

    template = TEMPLATE_FILE.read_text(encoding='utf-8')

    # Replace first section (title) with enhanced version
    if sections:
        sections[0] = create_enhanced_title_slide(metadata)

    slides_content = '\n\n'.join(sections)

    html = template.replace('{{TITLE}}', metadata['title'])
    html = html.replace('{{AUTHOR}}', metadata['author'])
    html = html.replace('{{SLIDES_CONTENT}}', slides_content)
    html = html.replace('{{SLIDE_NAME}}', slide_name)

    return html


def convert_tex_to_revealjs(tex_file: Path, output_dir: Path) -> Path:
    """Convert a single .tex file to enhanced Reveal.js HTML."""
    output_html = output_dir / f"{tex_file.stem}.html"
    slide_name = tex_file.stem  # e.g., "L01_overview"

    # Step 1: Process charts (PDF -> PNG)
    chart_map = process_charts(tex_file)

    try:
        # Step 2: Parse .tex with custom parser (no Pandoc needed)
        parser = BeamerParser(tex_file, chart_map)
        sections, metadata = parser.parse()

        if not sections:
            print(f"  WARNING: No sections extracted from {tex_file.name}")
            return None

        # Step 3: Apply template with slide name for PDF link
        final_html = apply_template(sections, metadata, slide_name)

        # Write final output
        output_html.write_text(final_html, encoding='utf-8')

        charts_info = f", {len(chart_map)} charts" if chart_map else ""
        print(f"  OK: {tex_file.name} -> {output_html.name} ({len(sections)} slides{charts_info})")
        return output_html

    except Exception as e:
        print(f"  ERROR (Processing): {tex_file.name} - {e}")
        import traceback
        traceback.print_exc()
        return None


def generate_qr_code():
    """Generate QR code for wiki URL."""
    qr_path = IMAGES_OUT / "qr_wiki.png"
    if qr_path.exists():
        return

    try:
        import qrcode
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(WIKI_URL)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(str(qr_path))
        print(f"  Generated QR code: {qr_path.name}")
    except ImportError:
        print("  WARNING: qrcode module not installed, skipping QR generation")
    except Exception as e:
        print(f"  WARNING: Could not generate QR code: {e}")


def convert_all():
    """Convert all Beamer .tex files to enhanced Reveal.js."""
    # Ensure output directories exist
    SLIDES_OUT.mkdir(parents=True, exist_ok=True)
    IMAGES_OUT.mkdir(parents=True, exist_ok=True)

    # Ensure CSS directory exists
    css_dir = SLIDES_OUT / "css"
    css_dir.mkdir(exist_ok=True)

    # Generate QR code
    generate_qr_code()

    # Find all lecture .tex files
    tex_files = sorted(SLIDES_SRC.rglob("L0*_*.tex"))

    print(f"Found {len(tex_files)} .tex files to convert")
    print(f"Template: {TEMPLATE_FILE}")
    print(f"Output: {SLIDES_OUT}\n")

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
