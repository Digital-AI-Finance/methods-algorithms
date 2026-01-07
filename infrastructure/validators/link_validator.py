"""Link validation for course content."""
import re
import urllib.request
import urllib.error
from pathlib import Path
from html.parser import HTMLParser

PROJECT_ROOT = Path(__file__).parent.parent.parent


class HTMLLinkExtractor(HTMLParser):
    """Extract href and src attributes from HTML."""

    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'a' and 'href' in attrs_dict:
            self.links.append(('href', attrs_dict['href']))
        elif tag in ('img', 'script') and 'src' in attrs_dict:
            self.links.append(('src', attrs_dict['src']))
        elif tag == 'link' and 'href' in attrs_dict:
            # Skip preconnect/prefetch hints (not actual resources)
            rel = attrs_dict.get('rel', '')
            if rel not in ('preconnect', 'dns-prefetch', 'prefetch'):
                self.links.append(('href', attrs_dict['href']))


def validate_links(manifest: dict, external: bool = False) -> bool:
    """
    Validate all links in course content.

    Args:
        manifest: Course manifest
        external: If True, check external URLs

    Returns:
        True if all validations pass
    """
    all_passed = True

    # Check file references in manifest
    print("  Checking file references...")
    for topic in manifest["topics"]:
        assets = topic.get("assets", {})

        # Check each asset file
        for asset_type, asset in assets.items():
            if isinstance(asset, dict) and "file" in asset:
                file_path = PROJECT_ROOT / asset["file"]
                if not file_path.exists() and asset.get("status") == "complete":
                    print(f"    [FAIL] Missing: {asset['file']}")
                    all_passed = False
            elif isinstance(asset, list):
                for item in asset:
                    if "file" in item:
                        file_path = PROJECT_ROOT / item["file"]
                        if not file_path.exists() and item.get("status") == "complete":
                            print(f"    [FAIL] Missing: {item['file']}")
                            all_passed = False

    # Check external URLs if requested
    if external:
        print("  Checking external URLs...")
        urls = _extract_urls_from_files()
        for url in urls:
            if _check_url(url):
                print(f"    [PASS] {url}")
            else:
                print(f"    [FAIL] {url}")
                all_passed = False

    if all_passed:
        print("  [PASS] All links valid")

    return all_passed


def validate_html_links(html_file: str = None, check_external: bool = True) -> dict:
    """
    Validate all links in HTML files (GitHub Pages).

    Args:
        html_file: Specific HTML file to check, or None for all in docs/
        check_external: Whether to check external URLs

    Returns:
        Dictionary with results: {passed: [], failed: [], summary: {}}
    """
    results = {"passed": [], "failed": [], "summary": {}}
    docs_dir = PROJECT_ROOT / "docs"

    if html_file:
        html_files = [Path(html_file)]
    else:
        html_files = list(docs_dir.rglob("*.html"))

    print(f"\n{'='*60}")
    print("  HTML LINK VALIDATION")
    print(f"{'='*60}")

    local_links = []
    external_links = []

    for html_path in html_files:
        print(f"\n  Scanning: {html_path.relative_to(PROJECT_ROOT)}")

        try:
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            results["failed"].append({"file": str(html_path), "error": str(e)})
            continue

        # Extract links
        parser = HTMLLinkExtractor()
        parser.feed(content)

        for link_type, link in parser.links:
            if link.startswith("http://") or link.startswith("https://"):
                external_links.append((html_path, link))
            elif link.startswith("#"):
                # Skip anchor links
                continue
            elif link.startswith("data:"):
                # Skip data URIs
                continue
            else:
                local_links.append((html_path, link))

    # Check local file links
    print(f"\n  Checking {len(local_links)} local links...")
    for html_path, link in local_links:
        # Resolve relative path from HTML file location
        if link.startswith("/"):
            resolved = docs_dir / link[1:]
        else:
            resolved = html_path.parent / link
        resolved = resolved.resolve()

        if resolved.exists():
            results["passed"].append({"type": "local", "link": link, "resolved": str(resolved)})
            print(f"    [PASS] {link}")
        else:
            results["failed"].append({"type": "local", "link": link, "expected": str(resolved)})
            print(f"    [FAIL] {link} -> {resolved}")

    # Check external links
    if check_external:
        print(f"\n  Checking {len(external_links)} external links...")
        for html_path, url in external_links:
            # Skip Colab links with repo paths (they redirect)
            if "colab.research.google.com" in url:
                results["passed"].append({"type": "external", "link": url, "note": "Colab link (skipped)"})
                print(f"    [SKIP] {url[:60]}... (Colab)")
                continue

            if _check_url(url):
                results["passed"].append({"type": "external", "link": url})
                print(f"    [PASS] {url[:60]}...")
            else:
                results["failed"].append({"type": "external", "link": url})
                print(f"    [FAIL] {url[:60]}...")

    # Summary
    results["summary"] = {
        "total_local": len(local_links),
        "total_external": len(external_links),
        "passed": len(results["passed"]),
        "failed": len(results["failed"])
    }

    print(f"\n{'='*60}")
    print(f"  SUMMARY: {results['summary']['passed']} passed, {results['summary']['failed']} failed")
    print(f"{'='*60}\n")

    return results


def _extract_urls_from_files() -> set:
    """Extract URLs from all tex, md, and html files."""
    urls = set()
    url_pattern = re.compile(r'https?://[^\s\)\]\}>"\']+')

    for ext in ["*.tex", "*.md", "*.html"]:
        for file_path in PROJECT_ROOT.rglob(ext):
            if ".git" in str(file_path):
                continue
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    found = url_pattern.findall(content)
                    urls.update(found)
            except Exception:
                pass

    return urls


def _check_url(url: str, timeout: int = 10) -> bool:
    """Check if URL is accessible."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        urllib.request.urlopen(req, timeout=timeout)
        return True
    except (urllib.error.URLError, urllib.error.HTTPError, Exception):
        return False


if __name__ == "__main__":
    # Run HTML link validation when called directly
    import sys
    check_external = "--external" in sys.argv or "-e" in sys.argv
    results = validate_html_links(check_external=check_external)
    sys.exit(0 if results["summary"]["failed"] == 0 else 1)
