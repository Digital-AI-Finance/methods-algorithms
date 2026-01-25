# Utils Module - Utility Functions

<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 -->

## Purpose

Utility subsystem providing common functionality shared across infrastructure modules. Includes retry strategies for transient failures, file hashing for change detection, and error handling patterns.

## Key Files

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `__init__.py` | Module exports | minimal | Package initialization |
| `retry_strategy.py` | Retry logic with exponential backoff | 112 | `RetryStrategy.execute()`, `_add_to_manual_review()` |
| `hash_utils.py` | File hashing for change detection | TBD | `calculate_hash()`, `has_file_changed()` (stub) |

## For AI Agents

### Module Architecture

Utilities follow a **reusable component pattern**:

```python
# Import and use across infrastructure
from utils import RetryStrategy, calculate_hash

# Use retry strategy
retry = RetryStrategy(max_retries=3)
result = retry.execute(risky_operation, arg1, arg2, operation_name="download_dataset")

# Use hashing
file_hash = calculate_hash("slides/L01_overview.pdf")
```

### Retry Strategy (`retry_strategy.py`)

**Purpose:** Execute operations with automatic retry logic and exponential backoff.

**Key Features:**
- Configurable retry attempts (default: 3)
- Exponential backoff between retries (1s, 2s, 4s, ...)
- Automatic logging of failures
- Manual review queue for operations that fail all retries

**Class Structure:**

```python
class RetryStrategy:
    """Execute operations with retry logic and exponential backoff."""

    def __init__(
        self,
        max_retries: int = 3,
        base_delay: float = 1.0,
        manual_review_path: Optional[Path] = None
    ):
        self.max_retries = max_retries          # Number of retry attempts
        self.base_delay = base_delay            # Initial delay (seconds)
        self.manual_review_path = manual_review_path or Path("manual_review.json")
        self._manual_review_items: list = []
```

**Execute with Retry:**

```python
def execute(
    self,
    operation: Callable[..., T],
    *args,
    operation_name: str = "operation",
    **kwargs
) -> Optional[T]:
    """Execute operation with retry logic.

    Args:
        operation: Function to execute
        *args: Positional arguments for operation
        operation_name: Name for logging purposes
        **kwargs: Keyword arguments for operation

    Returns:
        Operation result or None if all retries failed
    """
    last_error = None

    for attempt in range(self.max_retries):
        try:
            result = operation(*args, **kwargs)
            if attempt > 0:
                logger.info(f"{operation_name} succeeded on attempt {attempt + 1}")
            return result
        except Exception as e:
            last_error = e
            if attempt < self.max_retries - 1:
                delay = self.base_delay * (2 ** attempt)  # Exponential backoff
                logger.warning(
                    f"{operation_name} failed (attempt {attempt + 1}/{self.max_retries}): {e}. "
                    f"Retrying in {delay}s..."
                )
                time.sleep(delay)
            else:
                logger.error(
                    f"{operation_name} failed after {self.max_retries} attempts: {e}"
                )

    # All retries failed - add to manual review
    self._add_to_manual_review(operation_name, str(last_error))
    return None
```

**Retry Timing:**
- Attempt 1: Immediate execution
- Attempt 2: Wait 1s (base_delay × 2^0)
- Attempt 3: Wait 2s (base_delay × 2^1)
- Attempt 4: Wait 4s (base_delay × 2^2)

**Manual Review Queue:**

When all retries fail, operation is added to manual review:

```python
def _add_to_manual_review(self, operation_name: str, error: str) -> None:
    """Add failed operation to manual review list."""
    item = {
        "type": "retry_failed",
        "operation": operation_name,
        "error": error,
        "attempts": self.max_retries,
        "timestamp": datetime.now().isoformat(),
        "suggested_action": f"Manually verify and retry {operation_name}"
    }
    self._manual_review_items.append(item)
    self._save_manual_review()
```

**Manual Review File Format:**

`manual_review.json`:
```json
{
  "items": [
    {
      "type": "retry_failed",
      "operation": "download_dataset",
      "error": "HTTPError: 404 Not Found",
      "attempts": 3,
      "timestamp": "2026-01-25T14:30:00",
      "suggested_action": "Manually verify and retry download_dataset"
    }
  ]
}
```

**Retrieve Pending Reviews:**

```python
def get_pending_reviews(self) -> list:
    """Get items pending manual review."""
    if not self.manual_review_path.exists():
        return []
    try:
        with open(self.manual_review_path, 'r') as f:
            data = json.load(f)
            return data.get("items", [])
    except Exception:
        return []
```

**Usage Examples:**

**Basic Retry:**
```python
from utils import RetryStrategy

def download_file(url: str, dest: Path) -> None:
    """Download file (may fail transiently)."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    dest.write_bytes(response.content)

# Execute with retry
retry = RetryStrategy(max_retries=3, base_delay=1.0)
result = retry.execute(
    download_file,
    "https://example.com/data.csv",
    Path("data.csv"),
    operation_name="download_dataset"
)

if result is None:
    print("Download failed after all retries")
```

**Custom Retry Configuration:**
```python
# More aggressive retry (5 attempts, 2s base delay)
retry = RetryStrategy(max_retries=5, base_delay=2.0)
result = retry.execute(slow_operation, arg1, arg2, operation_name="compute_metrics")

# Quick retry (2 attempts, 0.5s base delay)
retry = RetryStrategy(max_retries=2, base_delay=0.5)
result = retry.execute(fast_check, operation_name="check_api_status")
```

**Check Manual Review Queue:**
```python
retry = RetryStrategy()

# Execute some operations (some may fail)
retry.execute(op1, operation_name="operation_1")
retry.execute(op2, operation_name="operation_2")
retry.execute(op3, operation_name="operation_3")

# Check what needs manual review
pending = retry.get_pending_reviews()
for item in pending:
    print(f"FAILED: {item['operation']} - {item['error']}")
    print(f"  Suggested: {item['suggested_action']}")
```

**Use Cases:**

**1. Network Operations:**
```python
retry = RetryStrategy(max_retries=3)

# Download external resource
result = retry.execute(
    urllib.request.urlopen,
    "https://api.example.com/data",
    timeout=10,
    operation_name="fetch_api_data"
)
```

**2. File System Operations:**
```python
retry = RetryStrategy(max_retries=2)

# Copy file (may fail if file locked)
result = retry.execute(
    shutil.copy,
    src_path,
    dst_path,
    operation_name="copy_file"
)
```

**3. External Tool Invocation:**
```python
retry = RetryStrategy(max_retries=3)

def run_pdflatex(tex_file: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["pdflatex", str(tex_file)],
        capture_output=True,
        timeout=120,
        check=True
    )

result = retry.execute(
    run_pdflatex,
    tex_path,
    operation_name="compile_latex"
)
```

**Testing:**
```python
from utils import RetryStrategy

# Test successful operation
def always_succeeds(x):
    return x * 2

retry = RetryStrategy(max_retries=3)
result = retry.execute(always_succeeds, 5, operation_name="test_success")
assert result == 10

# Test failing operation
attempts = 0
def fails_twice(x):
    global attempts
    attempts += 1
    if attempts < 3:
        raise ValueError("Not yet!")
    return x * 2

attempts = 0
retry = RetryStrategy(max_retries=3, base_delay=0.1)
result = retry.execute(fails_twice, 5, operation_name="test_retry")
assert result == 10  # Should succeed on 3rd attempt

# Test complete failure
def always_fails(x):
    raise RuntimeError("Always fails")

retry = RetryStrategy(max_retries=2)
result = retry.execute(always_fails, 5, operation_name="test_failure")
assert result is None

# Check manual review
pending = retry.get_pending_reviews()
assert len(pending) == 1
assert pending[0]["operation"] == "test_failure"
```

### Hash Utils (`hash_utils.py`)

**Purpose:** Calculate file hashes for change detection (STUB - not yet implemented).

**Planned Features:**
- Calculate SHA256 hashes of files
- Detect if file has changed since last build
- Store hash cache for incremental builds
- Compare directory hashes

**Future Usage:**
```python
from utils import calculate_hash, has_file_changed, get_directory_hash

# Calculate file hash
hash_value = calculate_hash("slides/L01_overview.pdf")

# Check if file changed
if has_file_changed("slides/L01_overview.pdf", cache_path=".build_cache"):
    print("File changed - rebuild needed")

# Get hash of all files in directory
dir_hash = get_directory_hash("slides/L01_Introduction_Linear_Regression")
```

**Planned Implementation:**

**1. Calculate File Hash:**
```python
def calculate_hash(file_path: Path, algorithm: str = "sha256") -> str:
    """Calculate hash of file contents."""
    import hashlib

    hash_obj = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()
```

**2. Check if File Changed:**
```python
def has_file_changed(file_path: Path, cache_path: Path = Path(".build_cache")) -> bool:
    """Check if file has changed since last build."""
    if not file_path.exists():
        return False

    # Load hash cache
    cache = {}
    if cache_path.exists():
        with open(cache_path, 'r') as f:
            cache = json.load(f)

    # Calculate current hash
    current_hash = calculate_hash(file_path)

    # Compare with cached hash
    cache_key = str(file_path.relative_to(PROJECT_ROOT))
    if cache_key in cache:
        return cache[cache_key] != current_hash

    # Not in cache - assume changed
    return True
```

**3. Update Hash Cache:**
```python
def update_hash_cache(file_path: Path, cache_path: Path = Path(".build_cache")) -> None:
    """Update hash cache with current file hash."""
    cache = {}
    if cache_path.exists():
        with open(cache_path, 'r') as f:
            cache = json.load(f)

    cache_key = str(file_path.relative_to(PROJECT_ROOT))
    cache[cache_key] = calculate_hash(file_path)

    with open(cache_path, 'w') as f:
        json.dump(cache, f, indent=2)
```

**4. Directory Hash:**
```python
def get_directory_hash(dir_path: Path, algorithm: str = "sha256") -> str:
    """Calculate combined hash of all files in directory."""
    import hashlib

    hash_obj = hashlib.new(algorithm)

    # Sort files for consistent ordering
    files = sorted(dir_path.rglob("*"))

    for file_path in files:
        if file_path.is_file():
            # Hash filename
            hash_obj.update(str(file_path.relative_to(dir_path)).encode())
            # Hash contents
            with open(file_path, 'rb') as f:
                hash_obj.update(f.read())

    return hash_obj.hexdigest()
```

**Use Cases for Hashing:**

**1. Incremental Builds:**
```python
# Only rebuild if source changed
tex_file = Path("slides/L01_overview.tex")
pdf_file = tex_file.with_suffix(".pdf")

if has_file_changed(tex_file) or not pdf_file.exists():
    build_slides(tex_file)
    update_hash_cache(tex_file)
else:
    print(f"[SKIP] {tex_file.name} - no changes")
```

**2. Chart Regeneration:**
```python
# Only regenerate charts if script changed
chart_script = Path("slides/L01.../01_simple_regression/chart.py")
chart_pdf = chart_script.parent / "chart.pdf"

if has_file_changed(chart_script) or not chart_pdf.exists():
    run_chart_script(chart_script)
    update_hash_cache(chart_script)
```

**3. Cache Invalidation:**
```python
# Clear cache for specific topic
def clear_topic_cache(topic_id: str, cache_path: Path = Path(".build_cache")):
    """Remove cached hashes for a topic."""
    if not cache_path.exists():
        return

    with open(cache_path, 'r') as f:
        cache = json.load(f)

    # Remove entries for this topic
    cache = {k: v for k, v in cache.items() if topic_id not in k}

    with open(cache_path, 'w') as f:
        json.dump(cache, f, indent=2)
```

### Common Utility Patterns

**1. Safe File Operations:**
```python
def safe_read_json(file_path: Path, default: dict = None) -> dict:
    """Read JSON file with error handling."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default or {}

def safe_write_json(file_path: Path, data: dict) -> bool:
    """Write JSON file with error handling."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Failed to write JSON: {e}")
        return False
```

**2. Progress Indicators:**
```python
def with_progress(items: List, description: str = "Processing"):
    """Wrapper for progress indication."""
    total = len(items)
    for i, item in enumerate(items, 1):
        print(f"\r{description}: {i}/{total}", end="", flush=True)
        yield item
    print()  # Newline after completion
```

**3. Temporary File Handling:**
```python
from contextlib import contextmanager
import tempfile

@contextmanager
def temporary_directory():
    """Context manager for temporary directory."""
    temp_dir = Path(tempfile.mkdtemp())
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
```

### Testing Utilities

**Retry Strategy Tests:**
```python
import time
from utils import RetryStrategy

# Test exponential backoff
def test_backoff_timing():
    attempts = []
    def track_attempts():
        attempts.append(time.time())
        raise ValueError("Test error")

    retry = RetryStrategy(max_retries=3, base_delay=0.5)
    retry.execute(track_attempts, operation_name="test")

    # Check delays between attempts
    assert len(attempts) == 3
    assert attempts[1] - attempts[0] >= 0.5  # 1st retry after 0.5s
    assert attempts[2] - attempts[1] >= 1.0  # 2nd retry after 1.0s

# Test manual review queue
def test_manual_review():
    def always_fails():
        raise RuntimeError("Always fails")

    retry = RetryStrategy(max_retries=2)
    result = retry.execute(always_fails, operation_name="test_op")

    assert result is None
    pending = retry.get_pending_reviews()
    assert len(pending) == 1
    assert pending[0]["operation"] == "test_op"
    assert "Always fails" in pending[0]["error"]
```

**Hash Utils Tests (when implemented):**
```python
from utils import calculate_hash, has_file_changed

def test_hash_calculation():
    # Create test file
    test_file = Path("test.txt")
    test_file.write_text("Hello, World!")

    # Calculate hash
    hash1 = calculate_hash(test_file)
    assert len(hash1) == 64  # SHA256 is 64 hex chars

    # Same content = same hash
    hash2 = calculate_hash(test_file)
    assert hash1 == hash2

    # Different content = different hash
    test_file.write_text("Different content")
    hash3 = calculate_hash(test_file)
    assert hash1 != hash3

    # Cleanup
    test_file.unlink()
```

### Performance Considerations

**Retry Strategy:**
- Minimal overhead if operation succeeds first time
- Exponential backoff prevents overwhelming failing services
- Manual review prevents infinite retry loops

**File Hashing:**
- SHA256 is fast (~200 MB/s on modern CPUs)
- Cache hashes in memory for repeated checks
- Use mtime as quick pre-check before hashing

**Optimization:**
- Hash only files that matter (source files, not temp files)
- Use incremental hashing for large files
- Parallelize hashing for multiple files

### Dependencies

**Retry Strategy:**
- Python standard library (time, logging, json, pathlib, datetime)

**Hash Utils:**
- Python standard library (hashlib, json, pathlib)

**External Files:**
- `manual_review.json` (created automatically)
- `.build_cache` (created automatically for hashes)

### Future Enhancements

**1. Advanced Retry Strategies:**
```python
# Circuit breaker pattern
class CircuitBreaker(RetryStrategy):
    """Stop retrying if too many failures in time window."""
    pass

# Jittered backoff (avoid thundering herd)
class JitteredRetry(RetryStrategy):
    """Add random jitter to backoff delays."""
    pass
```

**2. Hash Cache Optimization:**
```python
# Use file mtime for quick checks
def has_file_changed_fast(file_path: Path, cache_path: Path) -> bool:
    """Check mtime first, hash only if mtime changed."""
    pass

# Parallel hashing
def calculate_directory_hash_parallel(dir_path: Path) -> str:
    """Use multiprocessing for large directories."""
    pass
```

**3. Logging Utilities:**
```python
# Structured logging
def setup_infrastructure_logging(log_file: Path = None):
    """Configure logging for infrastructure modules."""
    pass
```

---

**MANUAL:** This file documents utility functions shared across infrastructure modules. Primary utility is RetryStrategy for handling transient failures. Hash utilities (planned) will support incremental builds. Use these utilities in validators, builders, and deployers for robust error handling.
