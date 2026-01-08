"""Convert Beamer LaTeX slides to enhanced Reveal.js HTML presentations.

Pipeline:
1. Pandoc converts .tex to basic Reveal.js HTML
2. Post-processor fixes structure (splits frames, fixes colors, adds fragments)
3. Chart PDFs converted to PNGs for web display
4. Template injection adds plugins and custom theme
"""

import subprocess
import re
import shutil
from pathlib import Path
from bs4 import BeautifulSoup

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


def run_pandoc(tex_file: Path, output_html: Path) -> bool:
    """Run Pandoc to convert .tex to basic Reveal.js HTML."""
    cmd = [
        "pandoc",
        str(tex_file),
        "-t", "revealjs",
        "-s",
        "--mathjax",
        "-V", f"revealjs-url={REVEALJS_CDN}",
        "-V", "theme=white",
        "-V", "slideNumber=true",
        "-V", "width=1600",
        "-V", "height=900",
        "--slide-level=2",
        "-o", str(output_html)
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=tex_file.parent)
        return result.returncode == 0
    except Exception:
        return False


def extract_metadata(soup: BeautifulSoup) -> dict:
    """Extract title and author from Pandoc output."""
    metadata = {'title': 'Untitled', 'author': 'Methods and Algorithms', 'subtitle': ''}

    title_slide = soup.find('section', id='title-slide')
    if title_slide:
        h1 = title_slide.find('h1')
        if h1:
            metadata['title'] = h1.get_text(strip=True)
        subtitle = title_slide.find('p', class_='subtitle')
        if subtitle:
            metadata['subtitle'] = subtitle.get_text(strip=True)
        author = title_slide.find('p', class_='author')
        if author:
            metadata['author'] = author.get_text(strip=True)

    return metadata


def fix_colors(soup: BeautifulSoup) -> None:
    """Replace LaTeX color names with actual hex values."""
    for span in soup.find_all('span', style=True):
        style = span.get('style', '')
        for latex_color, hex_color in COLOR_MAP.items():
            if f'color: {latex_color}' in style:
                span['style'] = style.replace(f'color: {latex_color}', f'color: {hex_color}')


def remove_artifacts(soup: BeautifulSoup) -> None:
    """Remove conversion artifacts."""
    # Remove column width text (0.48, 0.5, etc.)
    for span in soup.find_all('span'):
        text = span.get_text(strip=True)
        if re.match(r'^0\.\d+$', text):
            span.decompose()

    # Remove empty frame divs
    for div in soup.find_all('div', class_='frame'):
        if not div.get_text(strip=True):
            div.decompose()

    # Fix stray whitespace after titles
    for p in soup.find_all('p'):
        if p.string and p.string.strip() == '':
            p.decompose()


def fix_image_paths(html: str, chart_map: dict) -> str:
    """Replace PDF embed paths with PNG image paths."""
    for pdf_path, png_path in chart_map.items():
        # Handle various embed formats from Pandoc
        html = re.sub(
            rf'<embed[^>]*data-src="{re.escape(pdf_path)}"[^>]*/?>',
            f'<img src="{png_path}" style="max-width:100%; max-height:500px;">',
            html
        )
        html = re.sub(
            rf'<embed[^>]*src="{re.escape(pdf_path)}"[^>]*/?>',
            f'<img src="{png_path}" style="max-width:100%; max-height:500px;">',
            html
        )
        # Handle object tags
        html = re.sub(
            rf'<object[^>]*data="{re.escape(pdf_path)}"[^>]*>.*?</object>',
            f'<img src="{png_path}" style="max-width:100%; max-height:500px;">',
            html,
            flags=re.DOTALL
        )

    return html


def split_frames_to_sections(soup: BeautifulSoup) -> list:
    """Split merged frames into separate section elements."""
    slides_container = soup.find('div', class_='slides')
    if not slides_container:
        return []

    new_sections = []

    # Get title slide
    title_slide = slides_container.find('section', id='title-slide')
    if title_slide:
        new_sections.append(str(title_slide))

    # Find merged section with frames
    for section in slides_container.find_all('section', class_='slide'):
        frames = section.find_all('div', class_='frame')

        for frame in frames:
            if not frame.get_text(strip=True):
                continue

            # Create new section
            section_html = ['<section>']

            # Extract title from first span
            first_p = frame.find('p')
            if first_p:
                first_span = first_p.find('span')
                if first_span and not first_span.get('class') and not first_span.get('style'):
                    title_text = first_span.get_text(strip=True)
                    if title_text and len(title_text) < 100:
                        section_html.append(f'<h2>{title_text}</h2>')
                        first_span.decompose()
                        if not first_p.get_text(strip=True):
                            first_p.decompose()

            # Add remaining content with fragment animations on list items
            frame_html = str(frame)

            # Add fragment class to li elements (but not in References section)
            if 'References' not in frame_html and 'ISLR' not in frame_html:
                frame_html = re.sub(r'<li(?![^>]*class="fragment")', '<li class="fragment"', frame_html)

            # Remove the outer frame div
            frame_html = re.sub(r'^<div class="frame"[^>]*>', '', frame_html)
            frame_html = re.sub(r'</div>\s*$', '', frame_html)

            section_html.append(frame_html)
            section_html.append('</section>')

            new_sections.append('\n'.join(section_html))

    return new_sections


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


def apply_template(sections: list, metadata: dict) -> str:
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

    return html


def convert_tex_to_revealjs(tex_file: Path, output_dir: Path) -> Path:
    """Convert a single .tex file to enhanced Reveal.js HTML."""
    output_html = output_dir / f"{tex_file.stem}.html"
    temp_html = output_dir / f"{tex_file.stem}_temp.html"

    # Step 0: Process charts
    chart_map = process_charts(tex_file)

    # Step 1: Run Pandoc
    if not run_pandoc(tex_file, temp_html):
        print(f"  ERROR (Pandoc): {tex_file.name}")
        return None

    try:
        # Step 2: Parse and process
        html_content = temp_html.read_text(encoding='utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract metadata
        metadata = extract_metadata(soup)

        # Fix issues
        fix_colors(soup)
        remove_artifacts(soup)

        # Split into sections
        sections = split_frames_to_sections(soup)

        if not sections:
            print(f"  WARNING: No sections extracted from {tex_file.name}")
            temp_html.rename(output_html)
            return output_html

        # Step 3: Apply template
        final_html = apply_template(sections, metadata)

        # Step 4: Fix image paths
        final_html = fix_image_paths(final_html, chart_map)

        # Write final output
        output_html.write_text(final_html, encoding='utf-8')

        # Clean up temp file
        if temp_html.exists():
            temp_html.unlink()

        charts_info = f", {len(chart_map)} charts" if chart_map else ""
        print(f"  OK: {tex_file.name} -> {output_html.name} ({len(sections)} slides{charts_info})")
        return output_html

    except Exception as e:
        print(f"  ERROR (Processing): {tex_file.name} - {e}")
        if temp_html.exists():
            temp_html.rename(output_html)
            return output_html
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
