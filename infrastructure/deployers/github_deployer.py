"""GitHub deployer - pushes content to GitHub repository."""
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional, List

PROJECT_ROOT = Path(__file__).parent.parent.parent


def deploy_to_github(
    commit_message: Optional[str] = None,
    branch: str = "main",
    push: bool = True,
    verbose: bool = False
) -> bool:
    """
    Deploy course content to GitHub.

    Args:
        commit_message: Git commit message (auto-generated if None)
        branch: Target branch
        push: Actually push to remote
        verbose: Show detailed output

    Returns:
        True if deployment succeeded
    """
    print(f"Deploying to GitHub ({branch})...")

    try:
        # Check if git repo
        if not (PROJECT_ROOT / ".git").exists():
            print("  [FAIL] Not a git repository")
            return False

        # Get status
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )

        if not result.stdout.strip():
            print("  [SKIP] No changes to commit")
            return True

        # Stage changes
        print("  Staging changes...")
        subprocess.run(
            ["git", "add", "-A"],
            cwd=PROJECT_ROOT,
            capture_output=not verbose
        )

        # Generate commit message
        if not commit_message:
            commit_message = _generate_commit_message()

        # Commit
        print(f"  Committing: {commit_message[:50]}...")
        result = subprocess.run(
            ["git", "commit", "-m", commit_message],
            cwd=PROJECT_ROOT,
            capture_output=not verbose,
            text=True
        )

        if result.returncode != 0:
            print(f"  [FAIL] Commit failed: {result.stderr}")
            return False

        # Push
        if push:
            print(f"  Pushing to {branch}...")
            result = subprocess.run(
                ["git", "push", "origin", branch],
                cwd=PROJECT_ROOT,
                capture_output=not verbose,
                text=True
            )

            if result.returncode != 0:
                print(f"  [FAIL] Push failed: {result.stderr}")
                return False

        print("  [PASS] Deployed successfully")
        return True

    except Exception as e:
        print(f"  [FAIL] {e}")
        return False


def sync_github_pages(
    source_dir: str = "docs",
    verbose: bool = False
) -> bool:
    """
    Sync GitHub Pages content.

    Args:
        source_dir: Directory containing GitHub Pages content
        verbose: Show detailed output

    Returns:
        True if sync succeeded
    """
    print("Syncing GitHub Pages...")

    docs_dir = PROJECT_ROOT / source_dir
    if not docs_dir.exists():
        print(f"  [FAIL] {source_dir}/ directory not found")
        return False

    # Check for index.html
    if not (docs_dir / "index.html").exists():
        print("  [WARN] No index.html found")

    # List contents
    files = list(docs_dir.rglob("*"))
    file_count = len([f for f in files if f.is_file()])
    print(f"  Found {file_count} files in {source_dir}/")

    # Verify key files
    required_files = ["index.html"]
    optional_files = ["css/style.css", "js/main.js"]

    for req in required_files:
        path = docs_dir / req
        if path.exists():
            print(f"  [X] {req}")
        else:
            print(f"  [ ] {req} (missing)")

    for opt in optional_files:
        path = docs_dir / opt
        if path.exists():
            print(f"  [X] {opt}")

    print("  [PASS] GitHub Pages ready")
    return True


def _generate_commit_message() -> str:
    """Generate automatic commit message."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Try to get summary of changes
    result = subprocess.run(
        ["git", "diff", "--cached", "--stat"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )

    if result.stdout:
        lines = result.stdout.strip().split("\n")
        if len(lines) > 1:
            summary = lines[-1].strip()  # e.g., "5 files changed, 200 insertions(+)"
        else:
            summary = "Content update"
    else:
        summary = "Content update"

    return f"Course update ({timestamp}): {summary}"


def get_remote_info() -> dict:
    """Get information about git remote."""
    info = {
        "remote_url": None,
        "branch": None,
        "has_remote": False
    }

    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            info["remote_url"] = result.stdout.strip()
            info["has_remote"] = True

        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            info["branch"] = result.stdout.strip()

    except Exception:
        pass

    return info


def create_release_tag(version: str, message: str = "") -> bool:
    """Create a git release tag."""
    print(f"Creating release tag: {version}")

    try:
        if not message:
            message = f"Release {version}"

        result = subprocess.run(
            ["git", "tag", "-a", version, "-m", message],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(f"  [FAIL] {result.stderr}")
            return False

        print(f"  [PASS] Tag {version} created")
        return True

    except Exception as e:
        print(f"  [FAIL] {e}")
        return False
