"""Custom Beamer LaTeX to Reveal.js HTML parser.

Parses Beamer .tex files directly without Pandoc for better control over output.
"""

import re
from pathlib import Path
from typing import Tuple, List, Dict


# Color mapping from LaTeX to CSS
COLORS = {
    'MLPurple': '#3333B2', 'mlpurple': '#3333B2',
    'MLBlue': '#0066CC', 'mlblue': '#0066CC',
    'MLOrange': '#FF7F0E', 'mlorange': '#FF7F0E',
    'MLGreen': '#2CA02C', 'mlgreen': '#2CA02C',
    'MLRed': '#D62728', 'mlred': '#D62728',
    'gray': '#666666', 'grey': '#666666',
    'red': '#D62728', 'blue': '#0066CC', 'green': '#2CA02C',
    'orange': '#FF7F0E', 'purple': '#3333B2',
}


class BeamerParser:
    """Parse Beamer LaTeX and convert to Reveal.js HTML sections."""

    def __init__(self, tex_file: Path, chart_map: dict = None):
        self.tex_file = Path(tex_file)
        self.chart_map = chart_map or {}
        self.lecture_name = self.tex_file.parent.name
        self.content = ""
        self.metadata = {
            'title': 'Untitled',
            'subtitle': '',
            'author': 'Methods and Algorithms',
            'date': ''
        }

    def parse(self) -> Tuple[List[str], Dict]:
        """Parse the .tex file and return sections and metadata."""
        self.content = self.tex_file.read_text(encoding='utf-8')

        # Remove comments
        self.content = self._remove_comments(self.content)

        # Extract metadata from preamble
        self._extract_metadata()

        # Extract frames
        frames = self._extract_frames()

        # Convert frames to HTML sections
        sections = []
        for i, frame in enumerate(frames):
            section_html = self._frame_to_section(frame, i == 0)
            if section_html:
                sections.append(section_html)

        return sections, self.metadata

    def _remove_comments(self, text: str) -> str:
        """Remove LaTeX comments (lines starting with % or inline %)."""
        lines = []
        for line in text.split('\n'):
            # Remove inline comments but keep escaped %
            idx = 0
            result = []
            while idx < len(line):
                if line[idx] == '%':
                    if idx > 0 and line[idx-1] == '\\':
                        result.append('%')
                        idx += 1
                    else:
                        break  # Rest is comment
                else:
                    result.append(line[idx])
                    idx += 1
            lines.append(''.join(result))
        return '\n'.join(lines)

    def _extract_metadata(self) -> None:
        """Extract title, subtitle, author from preamble."""
        # Title: \title[short]{long} or \title{title}
        match = re.search(r'\\title(?:\[.*?\])?\{(.+?)\}', self.content, re.DOTALL)
        if match:
            self.metadata['title'] = self._clean_text(match.group(1))

        # Subtitle
        match = re.search(r'\\subtitle\{(.+?)\}', self.content, re.DOTALL)
        if match:
            self.metadata['subtitle'] = self._clean_text(match.group(1))

        # Author
        match = re.search(r'\\author\{(.+?)\}', self.content, re.DOTALL)
        if match:
            self.metadata['author'] = self._clean_text(match.group(1))

        # Date
        match = re.search(r'\\date\{(.+?)\}', self.content, re.DOTALL)
        if match:
            self.metadata['date'] = self._clean_text(match.group(1))

    def _extract_frames(self) -> List[dict]:
        """Extract all frame environments."""
        frames = []

        # Pattern for \begin{frame}[options]{title} or \begin{frame}{title} or \begin{frame}
        pattern = r'\\begin\{frame\}(?:\s*\[([^\]]*)\])?\s*(?:\{([^}]*)\})?\s*(.*?)\\end\{frame\}'
        matches = re.finditer(pattern, self.content, re.DOTALL)

        for match in matches:
            options = match.group(1) or ''
            title = match.group(2) or ''
            body = match.group(3) or ''

            # Check for \frametitle in body
            title_match = re.search(r'\\frametitle\{([^}]+)\}', body)
            if title_match:
                title = title_match.group(1)
                body = re.sub(r'\\frametitle\{[^}]+\}', '', body)

            frames.append({
                'options': options,
                'title': self._clean_text(title),
                'body': body.strip(),
                'is_title': '\\titlepage' in body
            })

        return frames

    def _frame_to_section(self, frame: dict, is_first: bool) -> str:
        """Convert a frame dict to an HTML section."""
        if frame['is_title']:
            # Title slide - will be replaced by enhanced version in template
            return self._create_title_section()

        title = frame['title']
        body = frame['body']

        # Skip empty frames
        if not title and not body.strip():
            return ""

        # Convert body content
        html_body = self._convert_body(body)

        # Build section
        section = ['<section>']
        if title:
            section.append(f'<h2>{title}</h2>')
        section.append(html_body)
        section.append('</section>')

        return '\n'.join(section)

    def _create_title_section(self) -> str:
        """Create placeholder for title slide (replaced by template)."""
        return '<section id="title-slide"></section>'

    def _convert_body(self, body: str) -> str:
        """Convert frame body LaTeX to HTML."""
        html = body

        # Clean LaTeX escapes first
        html = re.sub(r"``", '"', html)  # Opening quotes
        html = re.sub(r"''", '"', html)  # Closing quotes
        html = re.sub(r'\\%', '%', html)  # Escaped percent

        # Remove common LaTeX commands that don't translate
        html = re.sub(r'\\vspace\{[^}]*\}', '', html)
        html = re.sub(r'\\hspace\{[^}]*\}', '', html)
        html = re.sub(r'\\vfill\b', '', html)
        html = re.sub(r'\\centering\b', '', html)
        html = re.sub(r'\\pause\b', '', html)
        html = re.sub(r'\\tableofcontents\b', '', html)

        # Convert environments first (before inline formatting)
        html = self._convert_center(html)
        html = self._convert_lists(html)
        html = self._convert_equations(html)
        html = self._convert_columns(html)

        # Convert inline formatting
        html = self._convert_textbf(html)
        html = self._convert_textit(html)
        html = self._convert_emph(html)
        html = self._convert_textcolor(html)
        html = self._convert_highlight(html)
        html = self._convert_inline_math(html)

        # Convert images
        html = self._convert_includegraphics(html)

        # Convert bottomnote
        html = self._convert_bottomnote(html)

        # Convert line breaks
        html = re.sub(r'\\\\(?:\[.*?\])?', '<br>', html)

        # Clean up excess whitespace
        html = re.sub(r'\n{3,}', '\n\n', html)

        # Wrap remaining text in paragraphs
        html = self._wrap_paragraphs(html)

        return html.strip()

    def _convert_center(self, text: str) -> str:
        """Convert center environment."""
        pattern = r'\\begin\{center\}(.*?)\\end\{center\}'
        return re.sub(pattern, r'<div class="center">\1</div>', text, flags=re.DOTALL)

    def _convert_lists(self, text: str) -> str:
        """Convert itemize and enumerate environments."""
        result = text

        # Process itemize
        def replace_itemize(match):
            content = match.group(1)
            items = re.split(r'\\item\s*', content)
            items = [i.strip() for i in items if i.strip()]
            li_items = '\n'.join(f'<li>{self._clean_text(item)}</li>' for item in items)
            return f'<ul>\n{li_items}\n</ul>'

        result = re.sub(
            r'\\begin\{itemize\}(.*?)\\end\{itemize\}',
            replace_itemize,
            result,
            flags=re.DOTALL
        )

        # Process enumerate
        def replace_enumerate(match):
            content = match.group(1)
            items = re.split(r'\\item\s*', content)
            items = [i.strip() for i in items if i.strip()]
            li_items = '\n'.join(f'<li>{self._clean_text(item)}</li>' for item in items)
            return f'<ol>\n{li_items}\n</ol>'

        result = re.sub(
            r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}',
            replace_enumerate,
            result,
            flags=re.DOTALL
        )

        return result

    def _convert_equations(self, text: str) -> str:
        """Convert equation environments to MathJax display math."""
        result = text

        # equation environment
        result = re.sub(
            r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}',
            r'\\[\1\\]',
            result,
            flags=re.DOTALL
        )

        # align environment
        result = re.sub(
            r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}',
            r'\\[\1\\]',
            result,
            flags=re.DOTALL
        )

        # bmatrix - keep as is for MathJax
        # No conversion needed

        return result

    def _convert_columns(self, text: str) -> str:
        """Convert columns environment."""
        result = text

        # columns environment
        def replace_columns(match):
            content = match.group(1)
            # Extract individual column environments
            cols = re.findall(r'\\begin\{column\}\{[^}]*\}(.*?)\\end\{column\}', content, re.DOTALL)
            if cols:
                col_divs = '\n'.join(f'<div class="column">{c.strip()}</div>' for c in cols)
                return f'<div class="columns">\n{col_divs}\n</div>'
            return content

        result = re.sub(
            r'\\begin\{columns\}(.*?)\\end\{columns\}',
            replace_columns,
            result,
            flags=re.DOTALL
        )

        return result

    def _convert_textbf(self, text: str) -> str:
        """Convert \\textbf{} to <strong>."""
        return re.sub(r'\\textbf\{([^}]+)\}', r'<strong>\1</strong>', text)

    def _convert_textit(self, text: str) -> str:
        """Convert \\textit{} to <em>."""
        return re.sub(r'\\textit\{([^}]+)\}', r'<em>\1</em>', text)

    def _convert_emph(self, text: str) -> str:
        """Convert \\emph{} to <em>."""
        return re.sub(r'\\emph\{([^}]+)\}', r'<em>\1</em>', text)

    def _convert_textcolor(self, text: str) -> str:
        """Convert \\textcolor{color}{text} to <span style="color:...">."""
        def replace_color(match):
            color_name = match.group(1)
            content = match.group(2)
            hex_color = COLORS.get(color_name, color_name)
            if not hex_color.startswith('#'):
                hex_color = COLORS.get(color_name.lower(), '#666666')
            return f'<span style="color: {hex_color}">{content}</span>'

        return re.sub(r'\\textcolor\{([^}]+)\}\{([^}]+)\}', replace_color, text)

    def _convert_highlight(self, text: str) -> str:
        """Convert \\highlight{} command."""
        def replace_highlight(match):
            content = match.group(1)
            return f'<span style="color: {COLORS["MLOrange"]}"><strong>{content}</strong></span>'

        return re.sub(r'\\highlight\{([^}]+)\}', replace_highlight, text)

    def _convert_inline_math(self, text: str) -> str:
        """Convert $...$ to \\(...\\) for MathJax."""
        # Be careful not to match $$ (display math)
        result = re.sub(r'(?<!\$)\$([^$]+)\$(?!\$)', r'\\(\1\\)', text)
        return result

    def _convert_includegraphics(self, text: str) -> str:
        """Convert \\includegraphics to <img>."""
        def replace_img(match):
            path = match.group(1)
            # Map to PNG in images folder
            for pdf_path, png_path in self.chart_map.items():
                if pdf_path in path or path in pdf_path:
                    return f'<img src="{png_path}" style="max-width:100%; max-height:500px;">'

            # Try to construct path
            # Input: 01_scree_plot/chart.pdf
            # Output: images/L05_PCA_tSNE/01_scree_plot.png
            chart_match = re.search(r'(\d+_[^/]+)/chart\.pdf', path)
            if chart_match:
                chart_name = chart_match.group(1)
                png_path = f'images/{self.lecture_name}/{chart_name}.png'
                return f'<img src="{png_path}" style="max-width:100%; max-height:500px;">'

            # Fallback
            return f'<img src="{path}" style="max-width:100%; max-height:500px;">'

        return re.sub(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', replace_img, text)

    def _convert_bottomnote(self, text: str) -> str:
        """Convert \\bottomnote{} to styled paragraph."""
        def replace_note(match):
            content = match.group(1)
            return f'<p class="bottomnote" style="color: #666666; font-size: 0.85em; margin-top: 1em;"><em>{content}</em></p>'

        return re.sub(r'\\bottomnote\{([^}]+)\}', replace_note, text)

    def _wrap_paragraphs(self, text: str) -> str:
        """Wrap loose text in paragraph tags."""
        lines = text.split('\n\n')
        result = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Don't wrap if already HTML element
            if re.match(r'^<(div|ul|ol|p|h[1-6]|section|img|table)', line):
                result.append(line)
            elif re.match(r'^\\\[', line):  # Display math
                result.append(line)
            elif line:
                # Wrap plain text in <p>
                if not line.startswith('<') and not line.startswith('\\'):
                    result.append(f'<p>{line}</p>')
                else:
                    result.append(line)
        return '\n\n'.join(result)

    def _clean_text(self, text: str) -> str:
        """Clean LaTeX text for HTML output."""
        result = text.strip()

        # Remove common LaTeX commands
        result = re.sub(r'\\\\', ' ', result)  # Line breaks
        result = re.sub(r'\\&', '&amp;', result)  # Escaped ampersand
        result = re.sub(r"``", '"', result)  # Opening quotes
        result = re.sub(r"''", '"', result)  # Closing quotes
        result = re.sub(r'--', '-', result)  # En dash
        result = re.sub(r'---', '-', result)  # Em dash
        result = re.sub(r'~', ' ', result)  # Non-breaking space
        result = re.sub(r'\\,', ' ', result)  # Thin space
        result = re.sub(r'\\;', ' ', result)  # Medium space
        result = re.sub(r'\\!', '', result)  # Negative space
        result = re.sub(r'\\ ', ' ', result)  # Escaped space
        result = re.sub(r'\\%', '%', result)  # Escaped percent

        # Convert text formatting
        result = self._convert_textbf(result)
        result = self._convert_textit(result)
        result = self._convert_emph(result)
        result = self._convert_textcolor(result)
        result = self._convert_inline_math(result)

        return result.strip()


if __name__ == "__main__":
    # Test with a sample file
    import sys
    if len(sys.argv) > 1:
        tex_file = Path(sys.argv[1])
        parser = BeamerParser(tex_file)
        sections, metadata = parser.parse()
        print(f"Title: {metadata['title']}")
        print(f"Subtitle: {metadata['subtitle']}")
        print(f"Sections: {len(sections)}")
        for i, s in enumerate(sections[:3]):
            print(f"\n--- Section {i} ---")
            print(s[:500])
