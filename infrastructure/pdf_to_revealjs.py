"""PDF to Reveal.js converter.

Converts Beamer PDF slides to PNG images and generates Reveal.js HTML slideshow.
This avoids LaTeX parsing issues - the PDF is already perfectly rendered.

Supports vertical slide navigation when section config files are provided.
"""

from pathlib import Path
from pdf2image import convert_from_path
import shutil
import json


def convert_pdf_to_slides(pdf_path: Path, output_dir: Path, dpi: int = 150) -> list:
    """Convert PDF to PNG images, one per page.

    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save PNG images
        dpi: Resolution (150 is good balance of quality/size)

    Returns:
        List of paths to generated slide images
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"  Converting {pdf_path.name} to images...")
    images = convert_from_path(str(pdf_path), dpi=dpi)

    slide_paths = []
    for i, image in enumerate(images, 1):
        slide_path = output_dir / f"slide_{i:02d}.png"
        image.save(slide_path, "PNG", optimize=True)
        slide_paths.append(slide_path)

    print(f"    Created {len(slide_paths)} slide images")
    return slide_paths


def load_section_config(sections_dir: Path, slide_name: str) -> dict:
    """Load section configuration for a lecture if it exists.

    Args:
        sections_dir: Directory containing section JSON files
        slide_name: Name of the slide deck (e.g., L01_overview)

    Returns:
        Section config dict or None if no config exists
    """
    config_path = sections_dir / f"{slide_name}.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def generate_revealjs_html(
    slide_paths: list,
    slide_name: str,
    title: str,
    output_path: Path,
    images_subdir: str,
    section_config: dict = None
) -> None:
    """Generate Reveal.js HTML with image slides.

    Args:
        slide_paths: List of paths to slide images
        slide_name: Name for the slide deck (e.g., L01_overview)
        title: Title for the HTML page
        output_path: Path to save the HTML file
        images_subdir: Subdirectory name for images (relative to HTML)
        section_config: Optional section grouping config for vertical slides
    """
    # Generate slide sections (nested if config provided)
    if section_config and 'sections' in section_config:
        # Vertical slides: group by sections
        sections = []
        for section in section_config['sections']:
            section_name = section.get('name', '')
            slide_nums = section.get('slides', [])

            # Build nested section
            inner_slides = []
            for slide_num in slide_nums:
                if 1 <= slide_num <= len(slide_paths):
                    slide = slide_paths[slide_num - 1]
                    inner_slides.append(f'''    <section data-slide="{slide_num}">
        <img src="{images_subdir}/{slide.name}"
             style="max-width:100%; max-height:95vh; object-fit:contain;"
             alt="Slide {slide_num}">
    </section>''')

            if inner_slides:
                section_html = f'''<section data-section="{section_name}">
{chr(10).join(inner_slides)}
</section>'''
                sections.append(section_html)
    else:
        # Flat structure (no vertical navigation)
        sections = []
        for i, slide in enumerate(slide_paths, 1):
            sections.append(f'''<section data-slide="{i}">
    <img src="{images_subdir}/{slide.name}"
         style="max-width:100%; max-height:95vh; object-fit:contain;"
         alt="Slide {i}">
</section>''')

    slides_content = '\n\n'.join(sections)

    # Generate full HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="generator" content="pdf-to-revealjs">
    <meta name="author" content="Methods and Algorithms - MSc Data Science">
    <title>{title}</title>

    <!-- Reveal.js core -->
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/theme/white.css" id="theme">

    <!-- Custom ML theme -->
    <link rel="stylesheet" href="css/ml-theme.css">

    <!-- Menu plugin CSS -->
    <link rel="stylesheet" href="https://unpkg.com/reveal.js-menu@2.1.0/menu.css">

    <!-- Chalkboard plugin CSS -->
    <link rel="stylesheet" href="https://unpkg.com/reveal.js-plugins@latest/chalkboard/style.css">

    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        /* Image slide styling */
        .reveal section img {{
            border: none;
            box-shadow: none;
            background: transparent;
        }}

        /* Center slides vertically */
        .reveal .slides section {{
            display: flex !important;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}

        /* Spotlight cursor */
        .spotlight-cursor {{
            position: fixed;
            pointer-events: none;
            z-index: 9999;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255,0,0,0.3) 0%, transparent 70%);
            transform: translate(-50%, -50%);
        }}

        /* PDF download button */
        .pdf-export-btn {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 100;
            background: var(--ml-purple, #3333B2);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            opacity: 0.8;
            transition: opacity 0.2s;
            text-decoration: none;
        }}
        .pdf-export-btn:hover {{
            opacity: 1;
            color: white;
        }}

        @media print {{
            .pdf-export-btn {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
{slides_content}
        </div>

        <!-- Custom footer -->
        <div class="slide-footer">
            <div class="footer-left">Methods and Algorithms</div>
            <div class="footer-center">MSc Data Science</div>
            <div class="footer-right"></div>
        </div>
    </div>

    <!-- PDF Download Button -->
    <a href="pdf/{slide_name}.pdf" class="pdf-export-btn" download title="Download PDF">
        <i class="fas fa-file-pdf"></i> PDF
    </a>

    <!-- Reveal.js core -->
    <script src="https://unpkg.com/reveal.js@4.5.0/dist/reveal.js"></script>

    <!-- Reveal.js plugins -->
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/notes/notes.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/search/search.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/zoom/zoom.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>

    <!-- Menu plugin -->
    <script src="https://unpkg.com/reveal.js-menu@2.1.0/menu.js"></script>

    <!-- Chalkboard plugin -->
    <script src="https://unpkg.com/reveal.js-plugins@latest/chalkboard/plugin.js"></script>

    <script>
        // Spotlight functionality
        let spotlightEnabled = false;
        let spotlightElement = null;

        function toggleSpotlight() {{
            spotlightEnabled = !spotlightEnabled;
            if (spotlightEnabled) {{
                spotlightElement = document.createElement('div');
                spotlightElement.className = 'spotlight-cursor';
                spotlightElement.style.width = '100px';
                spotlightElement.style.height = '100px';
                document.body.appendChild(spotlightElement);
                document.addEventListener('mousemove', updateSpotlight);
            }} else if (spotlightElement) {{
                document.removeEventListener('mousemove', updateSpotlight);
                spotlightElement.remove();
                spotlightElement = null;
            }}
        }}

        function updateSpotlight(e) {{
            if (spotlightElement) {{
                spotlightElement.style.left = e.clientX + 'px';
                spotlightElement.style.top = e.clientY + 'px';
            }}
        }}

        Reveal.initialize({{
            // Display settings
            controls: true,
            controlsTutorial: true,
            controlsLayout: 'bottom-right',
            progress: true,
            slideNumber: 'c/t',
            showSlideNumber: 'all',
            hash: true,
            history: true,

            // Navigation
            keyboard: true,
            overview: true,
            touch: true,
            loop: false,
            navigationMode: 'default',

            // Transitions
            transition: 'slide',
            transitionSpeed: 'default',
            backgroundTransition: 'fade',

            // Sizing (16:9 aspect ratio - matches Beamer)
            width: 1600,
            height: 900,
            margin: 0,
            minScale: 0.2,
            maxScale: 2.0,
            center: true,

            // Auto-slide (disabled)
            autoSlide: 0,

            // Menu plugin configuration
            menu: {{
                side: 'left',
                width: 'normal',
                numbers: true,
                titleSelector: 'h1, h2, [data-slide]',
                useTextContentForMissingTitles: false,
                hideMissingTitles: false,
                markers: true,
                custom: [
                    {{
                        title: 'Tools',
                        icon: '<i class="fas fa-tools"></i>',
                        content: `
                            <ul class="slide-menu-items">
                                <li class="slide-menu-item" onclick="toggleSpotlight(); RevealMenu.toggle();">
                                    <i class="fas fa-bullseye"></i> Toggle Spotlight (L)
                                </li>
                                <li class="slide-menu-item" onclick="window.open('pdf/{slide_name}.pdf', '_blank');">
                                    <i class="fas fa-file-pdf"></i> Download PDF
                                </li>
                            </ul>
                        `
                    }}
                ],
                themes: [
                    {{ name: 'ML Theme (Light)', theme: 'css/ml-theme.css' }},
                    {{ name: 'Black', theme: 'https://unpkg.com/reveal.js@4.5.0/dist/theme/black.css' }},
                    {{ name: 'White', theme: 'https://unpkg.com/reveal.js@4.5.0/dist/theme/white.css' }}
                ],
                transitions: true,
                openButton: true,
                openSlideNumber: false,
                keyboard: true,
                sticky: false,
                autoOpen: true
            }},

            // Chalkboard plugin configuration
            chalkboard: {{
                boardmarkerWidth: 3,
                chalkWidth: 4,
                chalkEffect: 0.5,
                storage: null,
                src: null,
                readOnly: false,
                toggleChalkboardButton: {{ left: "30px", bottom: "30px", top: "auto", right: "auto" }},
                toggleNotesButton: {{ left: "70px", bottom: "30px", top: "auto", right: "auto" }},
                colorButtons: true,
                boardHandle: true,
                transition: 800,
                theme: "chalkboard"
            }},

            // Plugins to load (no MathJax needed - math is in images)
            plugins: [
                RevealNotes,
                RevealSearch,
                RevealZoom,
                RevealHighlight,
                RevealMenu,
                RevealChalkboard
            ]
        }});

        // Custom keyboard shortcuts
        Reveal.addKeyBinding({{ keyCode: 76, key: 'L' }}, toggleSpotlight);  // L for spotlight

        // Update footer with slide number
        Reveal.on('slidechanged', event => {{
            const footer = document.querySelector('.slide-footer .footer-right');
            if (footer) {{
                const current = event.indexh + 1;
                const total = Reveal.getTotalSlides();
                footer.textContent = `${{current}} / ${{total}}`;
            }}
        }});

        // Initial footer update
        Reveal.on('ready', event => {{
            const footer = document.querySelector('.slide-footer .footer-right');
            if (footer) {{
                const total = Reveal.getTotalSlides();
                footer.textContent = `1 / ${{total}}`;
            }}
        }});

        // Keyboard shortcuts info
        console.log('Keyboard shortcuts:');
        console.log('  B - Chalkboard');
        console.log('  C - Canvas (draw on slide)');
        console.log('  L - Spotlight/Laser pointer');
        console.log('  M - Menu');
        console.log('  O - Overview');
        console.log('  F - Fullscreen');
        console.log('  ? - Help');
    </script>
</body>
</html>
'''

    output_path.write_text(html, encoding='utf-8')
    print(f"    Generated {output_path.name}")


def convert_all_pdfs(
    pdf_dir: Path,
    output_dir: Path,
    dpi: int = 150,
    sections_dir: Path = None
) -> dict:
    """Convert all PDFs in a directory to Reveal.js slideshows.

    Args:
        pdf_dir: Directory containing PDF files
        output_dir: Directory for output (HTML and images)
        dpi: Image resolution
        sections_dir: Directory containing section JSON configs (optional)

    Returns:
        Dictionary with conversion results
    """
    pdf_files = sorted(pdf_dir.glob("*.pdf"))

    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        return {"converted": 0, "failed": 0}

    print(f"Found {len(pdf_files)} PDF files to convert")
    print(f"Output: {output_dir}")
    if sections_dir and sections_dir.exists():
        print(f"Sections: {sections_dir}")
    print()

    converted = 0
    failed = 0

    for pdf_path in pdf_files:
        slide_name = pdf_path.stem  # e.g., L01_overview

        # Create images directory
        images_dir = output_dir / "images" / slide_name

        try:
            # Convert PDF to images
            slide_paths = convert_pdf_to_slides(pdf_path, images_dir, dpi)

            # Load section config if available
            section_config = None
            if sections_dir:
                section_config = load_section_config(sections_dir, slide_name)
                if section_config:
                    print(f"    Using section config: {len(section_config.get('sections', []))} sections")

            # Generate HTML
            title = slide_name.replace("_", ": ").replace("L0", "L")
            html_path = output_dir / f"{slide_name}.html"

            generate_revealjs_html(
                slide_paths=slide_paths,
                slide_name=slide_name,
                title=title,
                output_path=html_path,
                images_subdir=f"images/{slide_name}",
                section_config=section_config
            )

            nav_type = "vertical" if section_config else "flat"
            print(f"  OK: {pdf_path.name} -> {html_path.name} ({len(slide_paths)} slides, {nav_type})")
            converted += 1

        except Exception as e:
            print(f"  FAILED: {pdf_path.name}: {e}")
            failed += 1

    print()
    print("=" * 50)
    print(f"Converted: {converted}")
    print(f"Failed: {failed}")

    return {"converted": converted, "failed": failed}


if __name__ == "__main__":
    import sys
    import os

    # Change to project root
    script_dir = Path(__file__).parent
    os.chdir(script_dir.parent)

    # Default paths
    pdf_dir = Path("docs/slides/pdf")
    output_dir = Path("docs/slides")
    sections_dir = Path("docs/slides/sections")

    # Parse command line args
    dpi = 150
    if len(sys.argv) > 1:
        dpi = int(sys.argv[1])

    print(f"PDF to Reveal.js Converter")
    print(f"DPI: {dpi}")
    print()

    results = convert_all_pdfs(pdf_dir, output_dir, dpi, sections_dir)
