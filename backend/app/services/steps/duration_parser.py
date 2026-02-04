from __future__ import annotations
import re
from typing import Optional

# Supports:
# "10 minutes", "10 min", "10 mins"
# "30 seconds", "30 sec", "30s"
# "1 hour", "1 hr", "2h"
# "1 hour 10 minutes", "1h 10m", etc.

_UNIT_TO_SECONDS = {
    "s": 1, "sec": 1, "secs": 1, "second": 1, "seconds": 1,
    "m": 60, "min": 60, "mins": 60, "minute": 60, "minutes": 60,
    "h": 3600, "hr": 3600, "hrs": 3600, "hour": 3600, "hours": 3600,
}


_PATTERN = re.compile(
    r"(?P<num>\d+(?:\.\d+)?)\s*(?P<unit>hours?|hrs?|hr|h|minutes?|mins?|min|m|seconds?|secs?|sec|s)\b",
    re.IGNORECASE,
)

def parse_duration_seconds(text: str) -> Optional[int]:
    """
    Extract total duration in seconds from free text.
    Returns None if no duration found.
    """

    if not text:
        return None
    
    total = 0
    found = False

    for m in _PATTERN.finditer(text):
        found = True
        num = float(m.group("num"))
        unit = m.group("unit").lower()

        # normalize unit for mapping
        unit = unit.rstrip(".")
        if unit not in _UNIT_TO_SECONDS:
            continue

        total += int(num* _UNIT_TO_SECONDS[unit])

    return total if found and total > 0 else None