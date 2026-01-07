"""Activity logger - tracks all course development actions."""
import json
import uuid
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
from contextlib import contextmanager

PROJECT_ROOT = Path(__file__).parent.parent.parent
LOG_PATH = Path(__file__).parent / "activity_log.json"

# Event types
EVENT_TYPES = [
    "file_created",
    "file_modified",
    "file_deleted",
    "cli_command",
    "validation_run",
    "build_run",
    "download_attempt",
    "git_operation",
    "error",
    "info"
]


class ActivityLogger:
    """Context-aware activity logger."""

    def __init__(self, session_id: Optional[str] = None):
        self.session_id = session_id or str(uuid.uuid4())[:8]
        self._events: List[Dict] = []

    def log(
        self,
        event_type: str,
        target: str,
        details: Optional[Dict] = None,
        actor: str = "system"
    ) -> str:
        """Log an event.

        Args:
            event_type: Type of event (see EVENT_TYPES)
            target: Target file/resource
            details: Additional event details
            actor: Who/what triggered the event

        Returns:
            Event ID
        """
        event_id = str(uuid.uuid4())[:12]

        event = {
            "id": event_id,
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "actor": actor,
            "target": target,
            "details": details or {},
            "session_id": self.session_id
        }

        self._events.append(event)
        _append_to_log(event)

        return event_id

    @contextmanager
    def track_operation(self, operation_name: str, target: str):
        """Context manager for tracking operations."""
        start_time = datetime.now()
        error = None

        try:
            yield
        except Exception as e:
            error = str(e)
            raise
        finally:
            duration_ms = (datetime.now() - start_time).total_seconds() * 1000
            self.log(
                "cli_command" if error is None else "error",
                target,
                {
                    "operation": operation_name,
                    "duration_ms": duration_ms,
                    "success": error is None,
                    "error": error
                }
            )


# Global logger instance
_logger: Optional[ActivityLogger] = None


def get_logger() -> ActivityLogger:
    """Get or create global logger."""
    global _logger
    if _logger is None:
        _logger = ActivityLogger()
    return _logger


def log_event(
    event_type: str,
    target: str,
    details: Optional[Dict] = None,
    actor: str = "system"
) -> str:
    """Log an event using global logger."""
    return get_logger().log(event_type, target, details, actor)


def get_recent_activity(limit: int = 50) -> List[Dict]:
    """
    Get recent activity from log.

    Args:
        limit: Maximum events to return

    Returns:
        List of recent events
    """
    events = _load_log()
    return events[-limit:][::-1]  # Most recent first


def get_activity_by_type(
    event_type: str,
    limit: int = 50
) -> List[Dict]:
    """
    Get activity filtered by event type.

    Args:
        event_type: Type of event to filter
        limit: Maximum events to return

    Returns:
        List of matching events
    """
    events = _load_log()
    filtered = [e for e in events if e.get("event_type") == event_type]
    return filtered[-limit:][::-1]


def get_activity_by_target(
    target_pattern: str,
    limit: int = 50
) -> List[Dict]:
    """
    Get activity filtered by target pattern.

    Args:
        target_pattern: Pattern to match in target field
        limit: Maximum events to return

    Returns:
        List of matching events
    """
    events = _load_log()
    filtered = [e for e in events if target_pattern.lower() in e.get("target", "").lower()]
    return filtered[-limit:][::-1]


def export_activity_log(
    format: str = "markdown",
    output_path: Optional[Path] = None
) -> str:
    """
    Export activity log.

    Args:
        format: Output format (markdown, json, html)
        output_path: Output file path (optional)

    Returns:
        Exported content string
    """
    events = _load_log()

    if format == "json":
        content = json.dumps(events, indent=2)
    elif format == "html":
        content = _export_html(events)
    else:
        content = _export_markdown(events)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return content


def get_activity_stats() -> Dict:
    """Get activity statistics."""
    events = _load_log()

    stats = {
        "total_events": len(events),
        "by_type": {},
        "by_actor": {},
        "sessions": set(),
        "date_range": {
            "first": None,
            "last": None
        }
    }

    for event in events:
        # By type
        event_type = event.get("event_type", "unknown")
        stats["by_type"][event_type] = stats["by_type"].get(event_type, 0) + 1

        # By actor
        actor = event.get("actor", "unknown")
        stats["by_actor"][actor] = stats["by_actor"].get(actor, 0) + 1

        # Sessions
        stats["sessions"].add(event.get("session_id", ""))

        # Date range
        timestamp = event.get("timestamp")
        if timestamp:
            if stats["date_range"]["first"] is None:
                stats["date_range"]["first"] = timestamp
            stats["date_range"]["last"] = timestamp

    stats["sessions"] = len(stats["sessions"])
    return stats


def _load_log() -> List[Dict]:
    """Load activity log from file."""
    if not LOG_PATH.exists():
        return []

    try:
        with open(LOG_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("events", [])
    except (json.JSONDecodeError, Exception):
        return []


def _save_log(events: List[Dict]) -> None:
    """Save activity log to file."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        json.dump({"events": events}, f, indent=2)


def _append_to_log(event: Dict) -> None:
    """Append single event to log."""
    events = _load_log()
    events.append(event)
    _save_log(events)


def _export_markdown(events: List[Dict]) -> str:
    """Export events to markdown."""
    lines = [
        "# Activity Log",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Total events: {len(events)}",
        "",
        "| Time | Type | Target | Actor |",
        "|------|------|--------|-------|"
    ]

    for event in events[-100:]:  # Last 100
        time = event.get("timestamp", "")[:16].replace("T", " ")
        etype = event.get("event_type", "")
        target = event.get("target", "")[:30]
        actor = event.get("actor", "")

        lines.append(f"| {time} | {etype} | {target} | {actor} |")

    return "\n".join(lines)


def _export_html(events: List[Dict]) -> str:
    """Export events to HTML."""
    rows = []
    for event in events[-100:]:
        time = event.get("timestamp", "")[:16].replace("T", " ")
        etype = event.get("event_type", "")
        target = event.get("target", "")
        actor = event.get("actor", "")

        rows.append(f"<tr><td>{time}</td><td>{etype}</td><td>{target}</td><td>{actor}</td></tr>")

    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Activity Log</title>
    <style>
        body {{ font-family: sans-serif; margin: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background: #f4f4f4; }}
    </style>
</head>
<body>
    <h1>Activity Log</h1>
    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Events: {len(events)}</p>
    <table>
        <tr><th>Time</th><th>Type</th><th>Target</th><th>Actor</th></tr>
        {"".join(rows)}
    </table>
</body>
</html>"""
