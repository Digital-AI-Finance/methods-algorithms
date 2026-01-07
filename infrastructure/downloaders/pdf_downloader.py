"""PDF downloader - downloads and manages course reference materials."""
import json
import hashlib
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List
import ssl
import time

PROJECT_ROOT = Path(__file__).parent.parent.parent
RESOURCES_DIR = PROJECT_ROOT / "resources"
REGISTRY_PATH = Path(__file__).parent / "resource_registry.json"

# Default resources
DEFAULT_RESOURCES = [
    {
        "id": "islr-book",
        "title": "Introduction to Statistical Learning",
        "type": "textbook",
        "url": "https://www.statlearning.com/s/ISLRv2_corrected_June_2023.pdf",
        "topics": ["L01", "L02", "L03", "L04"],
        "local_path": "textbooks/ISLRv2.pdf"
    },
    {
        "id": "esl-book",
        "title": "Elements of Statistical Learning",
        "type": "textbook",
        "url": "https://hastie.su.domains/Papers/ESLII.pdf",
        "topics": ["L01", "L02", "L04", "L05"],
        "local_path": "textbooks/ESL.pdf"
    }
]


def download_resource(
    resource_id: str,
    max_retries: int = 3,
    verbose: bool = False
) -> bool:
    """
    Download a single resource.

    Args:
        resource_id: Resource ID from registry
        max_retries: Maximum retry attempts
        verbose: Show detailed output

    Returns:
        True if download succeeded
    """
    registry = _load_registry()
    resource = next((r for r in registry.get("resources", []) if r["id"] == resource_id), None)

    if not resource:
        print(f"  [FAIL] Resource not found: {resource_id}")
        return False

    return _download_with_retry(resource, max_retries, verbose)


def download_all_resources(
    topic: Optional[str] = None,
    max_retries: int = 3,
    verbose: bool = False
) -> Dict[str, bool]:
    """
    Download all resources (optionally filtered by topic).

    Args:
        topic: Filter by topic ID (e.g., "L01")
        max_retries: Maximum retry attempts per resource
        verbose: Show detailed output

    Returns:
        Dictionary of resource_id -> success status
    """
    print("Downloading resources...")
    registry = _load_registry()
    results = {}

    resources = registry.get("resources", [])
    if topic:
        resources = [r for r in resources if topic in r.get("topics", [])]

    for resource in resources:
        success = _download_with_retry(resource, max_retries, verbose)
        results[resource["id"]] = success

    # Summary
    success_count = sum(results.values())
    print(f"\nDownload complete: {success_count}/{len(results)} succeeded")

    return results


def verify_downloads(verbose: bool = False) -> Dict[str, Dict]:
    """
    Verify integrity of downloaded resources.

    Args:
        verbose: Show detailed output

    Returns:
        Dictionary of resource_id -> verification status
    """
    print("Verifying downloads...")
    registry = _load_registry()
    results = {}

    for resource in registry.get("resources", []):
        res_id = resource["id"]
        local_path = RESOURCES_DIR / resource.get("local_path", "")

        status = {
            "exists": local_path.exists(),
            "size_kb": 0,
            "hash_match": None
        }

        if status["exists"]:
            status["size_kb"] = local_path.stat().st_size / 1024

            if resource.get("sha256"):
                actual_hash = _compute_file_hash(local_path)
                status["hash_match"] = actual_hash == resource["sha256"]

            icon = "[X]" if status["size_kb"] > 100 else "[?]"
            print(f"  {icon} {res_id}: {status['size_kb']:.0f} KB")
        else:
            print(f"  [ ] {res_id}: not downloaded")

        results[res_id] = status

    return results


def get_download_status() -> Dict:
    """
    Get overall download status.

    Returns:
        Status dictionary
    """
    registry = _load_registry()
    resources = registry.get("resources", [])

    total = len(resources)
    downloaded = 0
    pending = 0
    failed = 0

    for resource in resources:
        status = resource.get("status", "pending")
        if status == "downloaded":
            downloaded += 1
        elif status == "failed":
            failed += 1
        else:
            pending += 1

    return {
        "total": total,
        "downloaded": downloaded,
        "pending": pending,
        "failed": failed,
        "percent_complete": int(100 * downloaded / total) if total > 0 else 0
    }


def _download_with_retry(
    resource: dict,
    max_retries: int,
    verbose: bool
) -> bool:
    """Download with retry logic."""
    res_id = resource["id"]
    url = resource["url"]
    local_path = RESOURCES_DIR / resource.get("local_path", f"{res_id}.pdf")

    print(f"  Downloading {res_id}...")

    # Create directory
    local_path.parent.mkdir(parents=True, exist_ok=True)

    # Skip if already downloaded
    if local_path.exists() and local_path.stat().st_size > 1000:
        print(f"    [SKIP] Already exists ({local_path.stat().st_size / 1024:.0f} KB)")
        return True

    last_error = None
    for attempt in range(max_retries):
        try:
            # Create SSL context that doesn't verify (for some academic sites)
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            # Download
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (Course Downloader)"}
            )

            with urllib.request.urlopen(req, timeout=60, context=ctx) as response:
                content = response.read()

            # Save
            with open(local_path, 'wb') as f:
                f.write(content)

            # Update registry
            _update_resource_status(res_id, "downloaded")

            size_kb = len(content) / 1024
            print(f"    [PASS] Downloaded ({size_kb:.0f} KB)")
            return True

        except Exception as e:
            last_error = str(e)
            if attempt < max_retries - 1:
                delay = 2 ** attempt
                if verbose:
                    print(f"    [RETRY] Attempt {attempt + 1} failed: {e}. Waiting {delay}s...")
                time.sleep(delay)

    # All retries failed
    print(f"    [FAIL] {last_error}")
    _update_resource_status(res_id, "failed", last_error)
    _add_to_manual_review(resource, last_error)
    return False


def _load_registry() -> dict:
    """Load resource registry."""
    if not REGISTRY_PATH.exists():
        # Create default registry
        registry = {"resources": DEFAULT_RESOURCES}
        _save_registry(registry)
        return registry

    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def _save_registry(registry: dict) -> None:
    """Save resource registry."""
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2)


def _update_resource_status(
    resource_id: str,
    status: str,
    error: Optional[str] = None
) -> None:
    """Update resource status in registry."""
    registry = _load_registry()

    for resource in registry.get("resources", []):
        if resource["id"] == resource_id:
            resource["status"] = status
            resource["last_attempt"] = datetime.now().isoformat()
            if error:
                resource["error_message"] = error
            break

    _save_registry(registry)


def _compute_file_hash(file_path: Path) -> str:
    """Compute SHA256 hash of file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def _add_to_manual_review(resource: dict, error: str) -> None:
    """Add failed download to manual review list."""
    manual_review_path = PROJECT_ROOT / "infrastructure" / "trackers" / "manual_review.json"
    manual_review_path.parent.mkdir(parents=True, exist_ok=True)

    items = []
    if manual_review_path.exists():
        with open(manual_review_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get("items", [])

    items.append({
        "type": "download_failed",
        "resource_id": resource["id"],
        "url": resource["url"],
        "error": error,
        "timestamp": datetime.now().isoformat(),
        "suggested_action": "Verify URL or download manually"
    })

    with open(manual_review_path, 'w', encoding='utf-8') as f:
        json.dump({"items": items}, f, indent=2)
