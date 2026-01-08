"""TexSoup-based Beamer LaTeX to Reveal.js HTML converter.

Uses TexSoup for proper AST-based parsing instead of fragile regex.
Handles nested structures, math environments, and Beamer-specific elements.
"""

from TexSoup import TexSoup
from TexSoup.data import TexNode, TexText
from pathlib import Path
from typing import Tuple, List, Dict, Any
import re


# Color mapping from LaTeX to CSS hex
COLORS = {
    'MLPurple': '#3333B2', 'mlpurple': '#3333B2',
    'MLBlue': '#0066CC', 'mlblue': '#0066CC',
    'MLOrange': '#FF7F0E', 'mlorange': '#FF7F0E',
    'MLGreen': '#2CA02C', 'mlgreen': '#2CA02C',
    'MLRed': '#D62728', 'mlred': '#D62728',
    'gray': '#666666', 'grey': '#666666',
    'red': '#D62728', 'blue': '#0066CC', 'green': '#2CA02C',
    'orange': '#FF7F0E', 'purple': '#3333B2', 'black': '#000000',
}


class BeamerParserV2:
    """Parse Beamer LaTeX using TexSoup AST and convert to Reveal.js HTML."""

    def __init__(self, tex_file: Path, chart_map: dict = None):
        self.tex_file = Path(tex_file)
        self.chart_map = chart_map or {}
        self.lecture_name = self.tex_file.parent.name

        # Read and parse content
        content = self.tex_file.read_text(encoding='utf-8')
        # Pre-process to help TexSoup
        content = self._preprocess(content)
        self.soup = TexSoup(content)

        self.metadata = {
            'title': 'Untitled',
            'subtitle': '',
            'author': 'Methods and Algorithms',
            'date': ''
        }

    def _preprocess(self, content: str) -> str:
        """Pre-process LaTeX to help TexSoup parse correctly."""
        # First, protect escaped dollar signs by replacing with placeholder
        content = content.replace('\\$', 'ESCAPEDDOLLAR')

        # Protect inline math $...$ by converting to HTML-style marker
        # Use @@MATH@@ markers that TexSoup won't try to parse as commands
        # Match $...$ but not $$ (display math)
        def protect_inline_math(match):
            math_content = match.group(1)
            # Use base64-like encoding to avoid any parsing issues
            import base64
            encoded = base64.b64encode(math_content.encode()).decode()
            return f'@@INLINEMATH:{encoded}@@'

        # Use greedy matching but exclude $$
        content = re.sub(r'(?<!\$)\$([^$]+)\$(?!\$)', protect_inline_math, content)

        # Also protect display math $$...$$
        def protect_display_math(match):
            math_content = match.group(1)
            import base64
            encoded = base64.b64encode(math_content.encode()).decode()
            return f'@@DISPLAYMATH:{encoded}@@'

        content = re.sub(r'\$\$(.+?)\$\$', protect_display_math, content, flags=re.DOTALL)

        # Restore escaped dollar signs
        content = content.replace('ESCAPEDDOLLAR', '\\$')

        # Remove comments
        lines = []
        for line in content.split('\n'):
            # Find % not preceded by \
            idx = 0
            result = []
            while idx < len(line):
                if line[idx] == '%':
                    if idx > 0 and line[idx-1] == '\\':
                        result.append('%')
                        idx += 1
                    else:
                        break
                else:
                    result.append(line[idx])
                    idx += 1
            lines.append(''.join(result))
        return '\n'.join(lines)

    def parse(self) -> Tuple[List[str], Dict]:
        """Parse the .tex file and return sections and metadata."""
        # Extract metadata
        self._extract_metadata()

        # Find all frames
        frames = list(self.soup.find_all('frame'))

        # Convert frames to HTML sections
        sections = []
        for i, frame in enumerate(frames):
            section_html = self._convert_frame(frame, i == 0)
            if section_html:
                sections.append(section_html)

        return sections, self.metadata

    def _extract_metadata(self) -> None:
        """Extract title, subtitle, author from preamble."""
        # Title
        title_node = self.soup.find('title')
        if title_node:
            # Get the content (may be in args or as text)
            title_text = self._get_node_text(title_node)
            if title_text:
                self.metadata['title'] = self._clean_text(title_text)

        # Subtitle
        subtitle_node = self.soup.find('subtitle')
        if subtitle_node:
            subtitle_text = self._get_node_text(subtitle_node)
            if subtitle_text:
                self.metadata['subtitle'] = self._clean_text(subtitle_text)

        # Author
        author_node = self.soup.find('author')
        if author_node:
            author_text = self._get_node_text(author_node)
            if author_text:
                self.metadata['author'] = self._clean_text(author_text)

    def _get_node_text(self, node) -> str:
        """Extract text content from a TexSoup node."""
        if node is None:
            return ''

        # Try to get from args first
        if hasattr(node, 'args') and node.args:
            # Find the main content arg (usually in braces)
            for arg in node.args:
                text = str(arg)
                if text.startswith('[') and text.endswith(']'):
                    continue  # Skip optional args
                # Remove surrounding braces
                if text.startswith('{') and text.endswith('}'):
                    text = text[1:-1]
                return text

        # Fall back to string content
        if hasattr(node, 'string'):
            return str(node.string) if node.string else ''

        return str(node)

    def _convert_frame(self, frame, is_first: bool) -> str:
        """Convert a frame node to an HTML section."""
        # Check if it's a title page
        frame_content = str(frame)
        if '\\titlepage' in frame_content:
            return '<section id="title-slide"></section>'

        # Get frame title from args
        title = ''
        seen_args = set()  # Track what we've used from args
        if hasattr(frame, 'args') and frame.args:
            for i, arg in enumerate(frame.args):
                arg_str = str(arg)
                if arg_str.startswith('[') and arg_str.endswith(']'):
                    seen_args.add(arg_str)  # Skip options like [t]
                    continue
                if arg_str.startswith('{') and arg_str.endswith('}'):
                    title = arg_str[1:-1]
                    seen_args.add(arg_str)
                    break

        # Also check for \frametitle
        frametitle = frame.find('frametitle')
        if frametitle:
            title = self._get_node_text(frametitle)

        # Build section HTML
        html_parts = ['<section>']
        if title:
            html_parts.append(f'<h2>{self._clean_text(title)}</h2>')

        # Process frame contents, skipping args we already used
        for child in frame.contents:
            child_str = str(child).strip()
            # Skip if this is a raw arg we already processed
            if child_str in seen_args:
                continue
            # Skip single letter options like 't' from [t]
            if len(child_str) <= 2 and child_str.isalpha():
                continue
            # Skip if it's just the title repeated
            if title and child_str == title:
                continue

            child_html = self._convert_node(child)
            if child_html and child_html.strip():
                # Skip if output is just the title
                if title and child_html.strip() == title:
                    continue
                html_parts.append(child_html)

        html_parts.append('</section>')

        # Post-process to convert any remaining INLINEMATH/DISPLAYMATH markers
        result = '\n'.join(html_parts)
        result = self._postprocess_math(result)
        return result

    def _postprocess_math(self, html: str) -> str:
        """Convert @@INLINEMATH:base64@@ and @@DISPLAYMATH:base64@@ markers to MathJax format."""
        import base64

        def decode_inline(match):
            encoded = match.group(1)
            try:
                content = base64.b64decode(encoded.encode()).decode()
                return f'\\({content}\\)'
            except:
                return match.group(0)  # Return as-is if decode fails

        def decode_display(match):
            encoded = match.group(1)
            try:
                content = base64.b64decode(encoded.encode()).decode()
                return f'\\[{content}\\]'
            except:
                return match.group(0)

        # Decode base64 math markers
        html = re.sub(r'@@INLINEMATH:([A-Za-z0-9+/=]+)@@', decode_inline, html)
        html = re.sub(r'@@DISPLAYMATH:([A-Za-z0-9+/=]+)@@', decode_display, html)

        # Also handle any old-style INLINEMATH{} markers for backwards compatibility
        html = re.sub(r'INLINEMATH\{([^{}]+)\}', lambda m: f'\\({m.group(1)}\\)', html)
        html = re.sub(r'DISPLAYMATH\{([^{}]+)\}', lambda m: f'\\[{m.group(1)}\\]', html)

        # Clean up any remaining INLINEMATH text (edge cases)
        html = re.sub(r'INLINEMATH([a-zA-Z0-9_\\^{}]+?)(?=[^a-zA-Z0-9_\\{}]|$)',
                      lambda m: f'\\({m.group(1)}\\)', html)

        return html

    def _convert_node(self, node) -> str:
        """Convert a TexSoup node to HTML."""
        # Handle plain text
        if isinstance(node, str):
            return self._process_text(node)

        if isinstance(node, TexText):
            return self._process_text(str(node))

        # Skip if not a TeX node
        if not hasattr(node, 'name'):
            return self._process_text(str(node))

        name = node.name

        # Skip certain commands
        if name in ('frametitle', 'titlepage', 'tableofcontents', 'pause',
                    'vspace', 'hspace', 'vfill', 'centering', 'setlength'):
            return ''

        # Environment handlers
        if name == 'itemize':
            return self._convert_list(node, 'ul')
        elif name == 'enumerate':
            return self._convert_list(node, 'ol')
        elif name == 'center':
            return f'<div class="center">{self._convert_contents(node)}</div>'
        elif name == 'columns':
            return self._convert_columns(node)
        elif name == 'column':
            return ''  # Handled by columns
        elif name == 'block':
            return self._convert_block(node)
        elif name in ('equation', 'equation*', 'align', 'align*'):
            return self._convert_display_math(node)
        elif name in ('tabular', 'table'):
            return self._convert_table(node)

        # Command handlers
        elif name == 'textbf':
            return f'<strong>{self._convert_contents(node)}</strong>'
        elif name == 'textit' or name == 'emph':
            return f'<em>{self._convert_contents(node)}</em>'
        elif name == 'textcolor':
            return self._convert_textcolor(node)
        elif name == 'highlight':
            content = self._convert_contents(node)
            return f'<span style="color: {COLORS["MLOrange"]}"><strong>{content}</strong></span>'
        elif name == 'includegraphics':
            return self._convert_image(node)
        elif name == 'bottomnote':
            content = self._convert_contents(node)
            return f'<p class="bottomnote" style="color: #666666; font-size: 0.85em; margin-top: 1em;"><em>{content}</em></p>'
        elif name == 'item':
            return ''  # Handled by list conversion
        elif name == 'section':
            return ''  # Skip section markers

        # For unknown commands, try to extract content
        return self._convert_contents(node)

    def _convert_list(self, node, tag: str) -> str:
        """Convert itemize/enumerate to HTML list."""
        items = []
        current_item = []

        for child in node.contents:
            if hasattr(child, 'name') and child.name == 'item':
                # Save previous item
                if current_item:
                    item_content = ''.join(current_item).strip()
                    if item_content:
                        items.append(f'<li>{item_content}</li>')
                current_item = []
                # Process item contents
                for item_child in child.contents:
                    current_item.append(self._convert_node(item_child))
            elif current_item is not None:
                # Add to current item
                current_item.append(self._convert_node(child))

        # Don't forget last item
        if current_item:
            item_content = ''.join(current_item).strip()
            if item_content:
                items.append(f'<li>{item_content}</li>')

        if not items:
            # Fallback: split by \item in string representation
            content = str(node)
            item_texts = re.split(r'\\item\s*', content)
            for text in item_texts[1:]:  # Skip first (before first \item)
                text = text.strip()
                if text:
                    # Clean up
                    text = re.sub(r'\\end\{(itemize|enumerate)\}.*', '', text, flags=re.DOTALL)
                    text = self._clean_text(text)
                    if text:
                        items.append(f'<li>{text}</li>')

        return f'<{tag}>\n' + '\n'.join(items) + f'\n</{tag}>'

    def _convert_columns(self, node) -> str:
        """Convert columns environment to flexbox."""
        columns = list(node.find_all('column'))
        if not columns:
            return self._convert_contents(node)

        html = '<div class="columns">'
        for col in columns:
            col_content = self._convert_column_contents(col)
            html += f'<div class="column">{col_content}</div>'
        html += '</div>'
        return html

    def _convert_column_contents(self, node) -> str:
        """Convert column contents, filtering out width specifications."""
        if not hasattr(node, 'contents'):
            return self._get_node_text(node)

        parts = []
        for child in node.contents:
            child_str = str(child).strip()
            # Skip column width specifications like {0.48\textwidth}
            if 'textwidth' in child_str:
                continue
            # Skip bare numbers that are width values like "0.48"
            if re.match(r'^[\d.]+$', child_str):
                continue
            child_html = self._convert_node(child)
            if child_html:
                parts.append(child_html)
        return ''.join(parts)

    def _convert_block(self, node) -> str:
        """Convert block environment."""
        title = ''
        if hasattr(node, 'args') and node.args:
            for arg in node.args:
                arg_str = str(arg)
                if arg_str.startswith('{') and arg_str.endswith('}'):
                    title = arg_str[1:-1]
                    break

        content = self._convert_contents(node)
        return f'''<div class="block">
            <div class="block-title"><strong>{title}</strong></div>
            {content}
        </div>'''

    def _convert_display_math(self, node) -> str:
        """Convert equation/align environments to MathJax display math."""
        # Get the raw math content
        content = str(node)
        # Extract just the math (between begin and end)
        match = re.search(r'\\begin\{[^}]+\}(.*?)\\end\{[^}]+\}', content, re.DOTALL)
        if match:
            math = match.group(1).strip()
        else:
            math = self._get_node_text(node)

        return f'\\[{math}\\]'

    def _convert_table(self, node) -> str:
        """Convert tabular/table environment to HTML table."""
        content = str(node)

        # For table environment, find the nested tabular
        if 'tabular' in content:
            tabular_match = re.search(r'\\begin\{tabular\}(\{[^}]*\})?(.*?)\\end\{tabular\}',
                                      content, re.DOTALL)
            if tabular_match:
                content = tabular_match.group(2)
        else:
            # Extract content between begin{tabular} and end{tabular}
            match = re.search(r'\\begin\{[^}]+\}(\{[^}]*\})?(.*?)\\end\{[^}]+\}',
                              content, re.DOTALL)
            if match:
                content = match.group(2)

        # Parse rows - split by \\ (row separator)
        # Also handle \toprule, \midrule, \bottomrule, \hline
        content = re.sub(r'\\(toprule|midrule|bottomrule|hline)', '', content)

        rows = re.split(r'\\\\', content)
        html_rows = []

        for row in rows:
            row = row.strip()
            if not row:
                continue

            cells = row.split('&')
            html_cells = []
            for cell in cells:
                cell_raw = cell.strip()
                # Check if it should be a header (has \textbf)
                is_header = '\\textbf' in cell_raw or 'textbf' in cell_raw
                # Process textbf
                cell_text = re.sub(r'\\textbf\{([^}]+)\}', r'<strong>\1</strong>', cell_raw)
                cell_text = self._clean_text(cell_text)
                if cell_text:
                    if is_header:
                        html_cells.append(f'<th>{cell_text}</th>')
                    else:
                        html_cells.append(f'<td>{cell_text}</td>')

            if html_cells:
                html_rows.append('<tr>' + ''.join(html_cells) + '</tr>')

        if html_rows:
            return '<table class="beamer-table">\n' + '\n'.join(html_rows) + '\n</table>'
        return ''

    def _convert_textcolor(self, node) -> str:
        """Convert \\textcolor{color}{text}."""
        args = list(node.args) if hasattr(node, 'args') else []
        if len(args) >= 2:
            color_name = str(args[0]).strip('{}')
            text = str(args[1]).strip('{}')
            hex_color = COLORS.get(color_name, COLORS.get(color_name.lower(), '#666666'))
            return f'<span style="color: {hex_color}">{self._clean_text(text)}</span>'
        return self._convert_contents(node)

    def _convert_image(self, node) -> str:
        """Convert \\includegraphics to <img>."""
        # Get the path from args
        path = ''
        if hasattr(node, 'args') and node.args:
            for arg in node.args:
                arg_str = str(arg)
                if arg_str.startswith('['):
                    continue  # Skip options
                if arg_str.startswith('{') and arg_str.endswith('}'):
                    path = arg_str[1:-1]
                    break

        if not path:
            return ''

        # Check chart_map first
        for pdf_path, png_path in self.chart_map.items():
            if pdf_path in path or path in pdf_path:
                return f'<img src="{png_path}" style="max-width:100%; max-height:500px;">'

        # Try to construct path for charts
        chart_match = re.search(r'(\d+_[^/]+)/chart\.pdf', path)
        if chart_match:
            chart_name = chart_match.group(1)
            png_path = f'images/{self.lecture_name}/{chart_name}.png'
            return f'<img src="{png_path}" style="max-width:100%; max-height:500px;">'

        # Fallback
        return f'<img src="{path}" style="max-width:100%; max-height:500px;">'

    def _convert_contents(self, node) -> str:
        """Convert all contents of a node."""
        if not hasattr(node, 'contents'):
            return self._get_node_text(node)

        parts = []
        for child in node.contents:
            child_html = self._convert_node(child)
            if child_html:
                parts.append(child_html)
        return ''.join(parts)

    def _process_text(self, text: str) -> str:
        """Process plain text, handling inline math and formatting."""
        if not text or not text.strip():
            return ''

        # Clean LaTeX escapes
        text = self._clean_text(text)

        # Note: Inline math $...$ is now handled in _preprocess() and _convert_node()
        # Any remaining $ should be treated as text (e.g., currency)

        return text

    def _clean_text(self, text: str) -> str:
        """Clean LaTeX text for HTML output."""
        if not text:
            return ''

        result = str(text).strip()

        # Handle escaped dollar signs FIRST (before other processing)
        result = result.replace('\\$', '$')

        # LaTeX escapes
        result = re.sub(r'\\\\(?:\[.*?\])?', '<br>', result)  # Line breaks
        result = re.sub(r'\\&', '&amp;', result)
        result = re.sub(r"``", '"', result)
        result = re.sub(r"''", '"', result)
        result = re.sub(r'---', '-', result)
        result = re.sub(r'--', '-', result)
        result = re.sub(r'~', ' ', result)
        result = re.sub(r'\\,', ' ', result)
        result = re.sub(r'\\;', ' ', result)
        result = re.sub(r'\\!', '', result)
        result = re.sub(r'\\ ', ' ', result)
        result = re.sub(r'\\%', '%', result)

        # Remove remaining backslash commands we don't handle
        # But keep math-related ones
        result = re.sub(r'\\(vspace|hspace|vfill|centering|pause)\{[^}]*\}', '', result)
        result = re.sub(r'\\(vspace|hspace|vfill|centering|pause)\b', '', result)

        return result.strip()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        tex_file = Path(sys.argv[1])
        parser = BeamerParserV2(tex_file)
        sections, metadata = parser.parse()
        print(f"Title: {metadata['title']}")
        print(f"Subtitle: {metadata['subtitle']}")
        print(f"Author: {metadata['author']}")
        print(f"Sections: {len(sections)}")
        for i, s in enumerate(sections[:3]):
            print(f"\n--- Section {i} ---")
            print(s[:800] if len(s) > 800 else s)
