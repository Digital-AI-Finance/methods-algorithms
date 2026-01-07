"""Link validation for course content."""
import re
import urllib.request
import urllib.error
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


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


def _extract_urls_from_files() -> set:
    """Extract URLs from all tex and md files."""
    urls = set()
    url_pattern = re.compile(r'https?://[^\s\)\]\}>"\']+')

    for ext in ["*.tex", "*.md"]:
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
