"""Retry strategy for handling transient failures with exponential backoff."""
import time
import logging
from typing import Callable, Any, Optional, TypeVar
from pathlib import Path
import json

T = TypeVar('T')

logger = logging.getLogger(__name__)


class RetryStrategy:
    """Execute operations with retry logic and exponential backoff."""

    def __init__(
        self,
        max_retries: int = 3,
        base_delay: float = 1.0,
        manual_review_path: Optional[Path] = None
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.manual_review_path = manual_review_path or Path("manual_review.json")
        self._manual_review_items: list = []

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
                    delay = self.base_delay * (2 ** attempt)
                    logger.warning(
                        f"{operation_name} failed (attempt {attempt + 1}/{self.max_retries}): {e}. "
                        f"Retrying in {delay}s..."
                    )
                    time.sleep(delay)
                else:
                    logger.error(
                        f"{operation_name} failed after {self.max_retries} attempts: {e}"
                    )

        self._add_to_manual_review(operation_name, str(last_error))
        return None

    def _add_to_manual_review(self, operation_name: str, error: str) -> None:
        """Add failed operation to manual review list."""
        from datetime import datetime

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

    def _save_manual_review(self) -> None:
        """Save manual review items to JSON file."""
        try:
            existing = []
            if self.manual_review_path.exists():
                with open(self.manual_review_path, 'r') as f:
                    data = json.load(f)
                    existing = data.get("items", [])

            all_items = existing + self._manual_review_items
            with open(self.manual_review_path, 'w') as f:
                json.dump({"items": all_items}, f, indent=2)

            self._manual_review_items = []
        except Exception as e:
            logger.error(f"Failed to save manual review: {e}")

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
