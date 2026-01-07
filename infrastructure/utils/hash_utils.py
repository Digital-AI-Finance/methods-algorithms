"""Hash utilities for file integrity verification."""
import hashlib
from pathlib import Path
from typing import Union


def compute_file_hash(file_path: Union[str, Path], algorithm: str = "sha256") -> str:
    """Compute hash of a file.

    Args:
        file_path: Path to the file
        algorithm: Hash algorithm (sha256, md5, sha1)

    Returns:
        Hexadecimal hash string

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If algorithm is not supported
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        hasher = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")

    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            hasher.update(chunk)

    return hasher.hexdigest()


def compute_string_hash(content: str, algorithm: str = "sha256") -> str:
    """Compute hash of a string.

    Args:
        content: String to hash
        algorithm: Hash algorithm (sha256, md5, sha1)

    Returns:
        Hexadecimal hash string
    """
    try:
        hasher = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")

    hasher.update(content.encode('utf-8'))
    return hasher.hexdigest()


def verify_hash(
    file_path: Union[str, Path],
    expected_hash: str,
    algorithm: str = "sha256"
) -> bool:
    """Verify file integrity against expected hash.

    Args:
        file_path: Path to the file
        expected_hash: Expected hash value
        algorithm: Hash algorithm used

    Returns:
        True if hash matches, False otherwise
    """
    try:
        actual_hash = compute_file_hash(file_path, algorithm)
        return actual_hash.lower() == expected_hash.lower()
    except (FileNotFoundError, ValueError):
        return False
