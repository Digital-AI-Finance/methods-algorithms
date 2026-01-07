"""Post-process Pandoc Reveal.js output to fix structure and styling."""

import re
from pathlib import Path
from bs4 import BeautifulSoup

# ML Color palette (from Beamer definitions)
COLOR_MAP = {
    'MLPurple': '#3333B2',
    'MLBlue': '#0066CC',
    'MLOrange': '#FF7F0E',
    'MLGreen': '#2CA02C',
    'MLRed': '#D62728',
    'MLLavender': '#ADADE0',
}


def fix_colors(soup: BeautifulSoup) -> None:
    """Replace LaTeX color names with actual hex values."""
    for span in soup.find_all('span', style=True):
        style = span.get('style', '')
        for latex_color, hex_color in COLOR_MAP.items():
            if latex_color in style:
                span['style'] = style.replace(f'color: {latex_color}', f'color: {hex_color}')


def remove_column_width_text(soup: BeautifulSoup) -> None:
    """Remove column width artifacts like <span>0.48</span>."""
    for span in soup.find_all('span'):
        text = span.get_text(strip=True)
        # Match patterns like "0.48", "0.5", etc.
        if re.match(r'^0\.\d+$', text):
            span.decompose()


def remove_empty_frames(soup: BeautifulSoup) -> None:
    """Remove empty <div class="frame"> elements."""
    for div in soup.find_all('div', class_='frame'):
        # Check if div has no meaningful content
        if not div.get_text(strip=True):
            div.decompose()


def split_frames_to_sections(soup: BeautifulSoup) -> None:
    """Convert <div class="frame"> elements to proper <section> slides."""
    slides_container = soup.find('div', class_='slides')
    if not slides_container:
        return

    # Find the merged section with all frames
    merged_section = slides_container.find('section', class_='slide')
    if not merged_section:
        return

    frames = merged_section.find_all('div', class_='frame', recursive=False)
    if not frames:
        return

    # Create new sections for each frame
    new_sections = []
    for frame in frames:
        # Skip empty frames
        if not frame.get_text(strip=True):
            continue

        new_section = soup.new_tag('section')

        # Extract title from first span if it looks like a title
        first_p = frame.find('p')
        if first_p:
            first_span = first_p.find('span')
            if first_span and not first_span.get('class') and not first_span.get('style'):
                # This is likely the frame title
                title_text = first_span.get_text(strip=True)
                if title_text and len(title_text) < 100:  # Reasonable title length
                    h2 = soup.new_tag('h2')
                    h2.string = title_text
                    new_section.append(h2)
                    first_span.decompose()
                    # If the paragraph is now empty, remove it
                    if not first_p.get_text(strip=True):
                        first_p.decompose()

        # Move all remaining content to new section
        for child in list(frame.children):
            new_section.append(child.extract() if hasattr(child, 'extract') else child)

        new_sections.append(new_section)

    # Replace merged section with new sections
    for new_section in new_sections:
        merged_section.insert_before(new_section)

    # Remove the original merged section
    merged_section.decompose()


def add_fragment_animations(soup: BeautifulSoup) -> None:
    """Add fragment class to list items for progressive reveal."""
    # Skip the first slide (title) and process rest
    sections = soup.find_all('section')
    for section in sections[1:]:  # Skip title slide
        # Add fragment to list items (but not nested ones to avoid double-animation)
        for ul in section.find_all(['ul', 'ol'], recursive=True):
            for li in ul.find_all('li', recursive=False):
                existing_classes = li.get('class', [])
                if 'fragment' not in existing_classes:
                    li['class'] = existing_classes + ['fragment']


def fix_bottomnote(soup: BeautifulSoup) -> None:
    """Style bottomnote (italic text at end of slides) properly."""
    for em in soup.find_all('em'):
        # Check if this is the last element in a section (bottomnote pattern)
        parent = em.parent
        if parent and parent.name == 'p':
            # Check if this p is near the end of its section
            section = parent.find_parent('section')
            if section:
                # Add bottomnote class for styling
                parent['class'] = parent.get('class', []) + ['bottomnote']


def process_html(html_content: str) -> str:
    """Process HTML content and return fixed version."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Apply fixes in order
    remove_empty_frames(soup)
    fix_colors(soup)
    remove_column_width_text(soup)
    split_frames_to_sections(soup)
    add_fragment_animations(soup)
    fix_bottomnote(soup)

    return str(soup)


def process_file(input_path: Path, output_path: Path = None) -> None:
    """Process a single HTML file."""
    if output_path is None:
        output_path = input_path

    html_content = input_path.read_text(encoding='utf-8')
    fixed_html = process_html(html_content)
    output_path.write_text(fixed_html, encoding='utf-8')
    print(f"  Processed: {input_path.name}")


if __name__ == "__main__":
    # Process all HTML files in docs/slides
    PROJECT_ROOT = Path(__file__).parent.parent
    SLIDES_DIR = PROJECT_ROOT / "docs" / "slides"

    html_files = list(SLIDES_DIR.glob("*.html"))
    print(f"Found {len(html_files)} HTML files to process\n")

    for html_file in sorted(html_files):
        process_file(html_file)

    print(f"\nProcessed {len(html_files)} files")
