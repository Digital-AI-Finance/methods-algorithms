# Deployers Module - Content Deployment

<!-- Parent: ../AGENTS.md -->
<!-- Updated: 2026-02-07 -->

## Purpose

Deployment subsystem for publishing course content to external platforms. Handles git operations for GitHub deployment and notebook preparation for Google Colab.

**All deployers return `bool`:** `True` = deployment succeeded, `False` = deployment failed.

## Key Files

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `__init__.py` | Module exports | minimal | Package initialization |
| `github_deployer.py` | Deploy to GitHub repository | 229 | `deploy_to_github()`, `sync_github_pages()`, `get_remote_info()`, `create_release_tag()` |
| `colab_deployer.py` | Prepare notebooks for Colab | TBD | `deploy_to_colab()` (stub) |

## For AI Agents

### Module Architecture

All deployers follow a **platform-specific deployment pattern**:

```python
def deploy_to_<platform>(content: dict, **options) -> bool:
    """
    Deploy content to <platform>.

    Args:
        content: Content to deploy (manifest, file paths, etc.)
        **options: Platform-specific deployment options

    Returns:
        True if deployment succeeded
    """
    # Validate prerequisites (git installed, credentials, etc.)
    # Prepare content for platform
    # Execute deployment
    # Verify deployment succeeded
    return success
```

### GitHub Deployer (`github_deployer.py`)

**Purpose:** Automate git operations for deploying course content to GitHub.

**Key Features:**
- Automatic commit message generation
- Staging and committing changes
- Pushing to remote repository
- GitHub Pages synchronization
- Release tag creation

**Deployment Functions:**

**1. Deploy to GitHub:**
```python
def deploy_to_github(
    commit_message: Optional[str] = None,
    branch: str = "main",
    push: bool = True,
    verbose: bool = False
) -> bool:
    """Deploy course content to GitHub."""
    # Check if git repo
    if not (PROJECT_ROOT / ".git").exists():
        return False

    # Get status
    result = subprocess.run(["git", "status", "--porcelain"], ...)
    if not result.stdout.strip():
        print("  [SKIP] No changes to commit")
        return True

    # Stage changes
    subprocess.run(["git", "add", "-A"], ...)

    # Generate commit message if needed
    if not commit_message:
        commit_message = _generate_commit_message()

    # Commit
    subprocess.run(["git", "commit", "-m", commit_message], ...)

    # Push
    if push:
        subprocess.run(["git", "push", "origin", branch], ...)

    return True
```

**2. Automatic Commit Messages:**
```python
def _generate_commit_message() -> str:
    """Generate automatic commit message based on changes."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Get summary of changes
    result = subprocess.run(
        ["git", "diff", "--cached", "--stat"],
        capture_output=True,
        text=True
    )

    if result.stdout:
        lines = result.stdout.strip().split("\n")
        summary = lines[-1].strip()  # e.g., "5 files changed, 200 insertions(+)"
    else:
        summary = "Content update"

    return f"Course update ({timestamp}): {summary}"
```

**Example commit messages:**
- `Course update (2026-01-25 14:30): 5 files changed, 200 insertions(+), 10 deletions(-)`
- `Course update (2026-01-25 15:45): 12 files changed, 450 insertions(+)`

**3. GitHub Pages Sync:**
```python
def sync_github_pages(
    source_dir: str = "docs",
    verbose: bool = False
) -> bool:
    """Sync GitHub Pages content."""
    docs_dir = PROJECT_ROOT / source_dir

    # Check directory exists
    if not docs_dir.exists():
        return False

    # Verify index.html
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
        print(f"  {'[X]' if path.exists() else '[ ]'} {req}")

    return True
```

**4. Get Remote Info:**
```python
def get_remote_info() -> dict:
    """Get information about git remote."""
    info = {
        "remote_url": None,
        "branch": None,
        "has_remote": False
    }

    try:
        # Get remote URL
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            info["remote_url"] = result.stdout.strip()
            info["has_remote"] = True

        # Get current branch
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            info["branch"] = result.stdout.strip()

    except Exception:
        pass

    return info
```

**Example output:**
```python
{
    "remote_url": "https://github.com/username/Methods_and_Algorithms.git",
    "branch": "master",
    "has_remote": True
}
```

**5. Create Release Tag:**
```python
def create_release_tag(version: str, message: str = "") -> bool:
    """Create a git release tag."""
    if not message:
        message = f"Release {version}"

    result = subprocess.run(
        ["git", "tag", "-a", version, "-m", message],
        capture_output=True,
        text=True
    )

    return result.returncode == 0
```

**Usage Examples:**

**Deploy changes to GitHub:**
```bash
# Automatic deployment with generated message
python infrastructure/course_cli.py deploy github

# Custom commit message
python infrastructure/course_cli.py deploy github --message "Add L06 slides"

# Deploy to different branch
python infrastructure/course_cli.py deploy github --branch develop

# Dry run (commit but don't push)
python infrastructure/course_cli.py deploy github --no-push
```

**From Python:**
```python
from deployers import deploy_to_github, sync_github_pages, create_release_tag

# Deploy with automatic commit message
success = deploy_to_github(push=True)

# Deploy with custom message
success = deploy_to_github(
    commit_message="Add quiz 2",
    branch="main",
    push=True,
    verbose=True
)

# Sync GitHub Pages
success = sync_github_pages(source_dir="docs", verbose=True)

# Create release tag
success = create_release_tag("v1.0.0", "First complete version")
```

**Deployment Workflow:**

```
1. Make changes to course content
   ↓
2. Build content (slides, charts, etc.)
   ↓
3. Validate content (validators)
   ↓
4. Stage changes (git add -A)
   ↓
5. Commit with message
   ↓
6. Push to GitHub
   ↓
7. GitHub Pages auto-deploys (if enabled)
```

**GitHub Pages Setup:**

**Prerequisites:**
1. GitHub repository created
2. Repository settings → Pages → Source: `main` branch, `/docs` folder
3. `docs/index.html` exists

**File Structure:**
```
docs/
├── index.html          (landing page)
├── css/
│   └── style.css       (styling)
├── js/
│   └── main.js         (interactions)
└── assets/
    ├── slides/         (PDF slides)
    └── notebooks/      (Colab links)
```

**Verification:**
After deployment, GitHub Pages site available at:
```
https://<username>.github.io/<repository>/
```

**Testing:**
```python
from deployers import deploy_to_github, get_remote_info

# Check git setup
info = get_remote_info()
assert info["has_remote"], "No git remote configured"
assert info["branch"] in ["main", "master"], "Unexpected branch"

# Test deployment (dry run)
success = deploy_to_github(push=False, verbose=True)
assert success, "Deployment failed"
```

### Colab Deployer (`colab_deployer.py`)

**Purpose:** Prepare and deploy Jupyter notebooks for Google Colab (STUB).

**Planned Features:**
- Add Colab badges to notebooks
- Update dataset paths to GitHub raw URLs
- Add installation cells for dependencies
- Validate notebooks execute in Colab
- Generate Colab links for docs

**Future Usage:**
```bash
# Prepare all notebooks for Colab
python infrastructure/course_cli.py deploy colab

# Prepare specific notebook
python infrastructure/course_cli.py deploy colab --notebook L01
```

**Planned Functionality:**

**1. Add Colab Badge:**
```python
def add_colab_badge(notebook_path: Path, github_url: str) -> None:
    """Add 'Open in Colab' badge to notebook."""
    nb = nbformat.read(notebook_path, as_version=4)

    colab_url = f"https://colab.research.google.com/github/{github_url}/blob/main/{notebook_path.relative_to(PROJECT_ROOT)}"

    badge_cell = nbformat.v4.new_markdown_cell(
        f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
    )

    # Insert at top of notebook
    nb.cells.insert(0, badge_cell)

    nbformat.write(nb, notebook_path)
```

**2. Update Dataset Paths:**
```python
def update_dataset_paths(notebook_path: Path, github_raw_base: str) -> None:
    """Update local dataset paths to GitHub raw URLs."""
    nb = nbformat.read(notebook_path, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "code":
            # Replace local paths with GitHub raw URLs
            cell.source = cell.source.replace(
                "pd.read_csv('../datasets/",
                f"pd.read_csv('{github_raw_base}/datasets/"
            )

    nbformat.write(nb, notebook_path)
```

**Example transformation:**
```python
# Before (local)
df = pd.read_csv('../datasets/loan_data.csv')

# After (Colab)
df = pd.read_csv('https://raw.githubusercontent.com/user/repo/main/datasets/loan_data.csv')
```

**3. Add Setup Cell:**
```python
def add_setup_cell(notebook_path: Path, dependencies: List[str]) -> None:
    """Add cell to install dependencies."""
    setup_code = "# Install dependencies\n"
    for dep in dependencies:
        setup_code += f"!pip install -q {dep}\n"

    setup_cell = nbformat.v4.new_code_cell(setup_code)

    nb = nbformat.read(notebook_path, as_version=4)
    nb.cells.insert(1, setup_cell)  # After badge cell
    nbformat.write(nb, notebook_path)
```

**4. Generate Colab Links:**
```python
def generate_colab_links(manifest: dict, github_url: str) -> dict:
    """Generate Colab links for all notebooks."""
    links = {}

    for topic in manifest["topics"]:
        notebook = topic.get("assets", {}).get("notebook", {})
        if notebook:
            nb_path = notebook["file"]
            colab_url = f"https://colab.research.google.com/github/{github_url}/blob/main/{nb_path}"
            links[topic["id"]] = colab_url

    return links
```

**5. Validate Colab Execution:**
```python
def validate_colab_notebook(notebook_url: str) -> bool:
    """Validate notebook can be opened in Colab (stub)."""
    # Check URL is accessible
    # Verify notebook format
    # Optionally: Use Colab API to test execution
    pass
```

### Common Deployment Patterns

**1. Pre-Deployment Checks:**
```python
def check_prerequisites() -> bool:
    """Check deployment prerequisites."""
    # Git installed?
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("  [FAIL] Git not installed")
        return False

    # Git repo initialized?
    if not (PROJECT_ROOT / ".git").exists():
        print("  [FAIL] Not a git repository")
        return False

    # Remote configured?
    info = get_remote_info()
    if not info["has_remote"]:
        print("  [WARN] No remote configured")

    return True
```

**2. Deployment Status:**
```python
def print_deployment_status(success: bool, details: str = "") -> None:
    """Print deployment status message."""
    if success:
        print(f"  [PASS] Deployed successfully")
        if details:
            print(f"    {details}")
    else:
        print(f"  [FAIL] Deployment failed")
        if details:
            print(f"    Error: {details}")
```

**3. Rollback on Failure:**
```python
def deploy_with_rollback(deploy_func, *args, **kwargs) -> bool:
    """Execute deployment with automatic rollback on failure."""
    # Save current state
    subprocess.run(["git", "stash", "push", "-u"], capture_output=True)

    try:
        success = deploy_func(*args, **kwargs)
        if not success:
            # Rollback
            subprocess.run(["git", "stash", "pop"], capture_output=True)
            return False
        # Success - discard stash
        subprocess.run(["git", "stash", "drop"], capture_output=True)
        return True
    except Exception as e:
        # Rollback on exception
        subprocess.run(["git", "stash", "pop"], capture_output=True)
        print(f"  [FAIL] Exception during deployment: {e}")
        return False
```

### Testing Deployers

**GitHub Deployer Tests:**
```python
from deployers import deploy_to_github, get_remote_info, sync_github_pages

# Test remote info
info = get_remote_info()
assert isinstance(info, dict)
assert "remote_url" in info
assert "branch" in info

# Test GitHub Pages sync
success = sync_github_pages(source_dir="docs", verbose=True)
assert success, "Sync failed"

# Test deployment (dry run - don't actually push)
success = deploy_to_github(
    commit_message="Test commit",
    push=False,
    verbose=True
)
```

**Integration Test:**
```bash
# Full deployment workflow
python infrastructure/course_cli.py build all
python infrastructure/course_cli.py validate --all
python infrastructure/course_cli.py deploy github
```

### CI/CD Integration

**GitHub Actions Workflow:**
```yaml
name: Deploy Course Content

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Build content
        run: python infrastructure/course_cli.py build all

      - name: Validate content
        run: python infrastructure/course_cli.py validate --all

      - name: Deploy to GitHub Pages
        run: python infrastructure/course_cli.py deploy github
```

### Performance Considerations

**Git Operations:**
- Staging: Fast (<1s for 100s of files)
- Committing: Fast (<1s)
- Pushing: Depends on network and repo size (5-30s)

**Large File Handling:**
- Use `.gitignore` to exclude build artifacts
- Use Git LFS for PDFs (optional)
- Compress images before committing

**Optimization:**
- Only commit changed files (git add specific paths)
- Use shallow clones for CI/CD
- Batch commits instead of per-file commits

### Dependencies

**Required:**
- `git` command-line tool (for GitHub deployer)

**Optional:**
- `nbformat`, `nbconvert` (for Colab deployer)
- GitHub account with push access
- GitHub Pages enabled (for pages deployment)

**External Files:**
- `.git/` directory (git repository)
- `docs/` directory (GitHub Pages content)
- `notebooks/` directory (Colab notebooks)

### Security Considerations

**Credentials:**
- Never commit credentials or API keys
- Use SSH keys or personal access tokens for authentication
- Store tokens in environment variables or git credential manager

**Sensitive Data:**
- Review changes before committing (`git diff`)
- Add sensitive files to `.gitignore`
- Use `.gitattributes` to mark files as non-diffable

**Branch Protection:**
- Enable branch protection on main branch
- Require pull request reviews
- Enable status checks before merging

---

**MANUAL:** This file documents the deployment subsystem for publishing course content. GitHub deployer handles git operations and GitHub Pages sync. Colab deployer (planned) will prepare notebooks for Google Colab. Deployers are orchestrated via `course_cli.py deploy` command.
