"""Check for updates from GitHub releases"""

import requests
from version import CURRENT_VERSION, GITHUB_API_URL


def get_latest_version():
    """Fetch latest version from GitHub releases."""
    try:
        response = requests.get(GITHUB_API_URL, timeout=5)
        if response.status_code == 200:
            latest_tag = response.json().get("tag_name", "").lstrip("v")
            return latest_tag if latest_tag else None
    except requests.RequestException:
        return None
    return None


def compare_versions(current, latest):
    """Compare version numbers. Returns True if update available."""
    try:
        curr_parts = [int(x) for x in current.split(".")]
        latest_parts = [int(x) for x in latest.split(".")]
        
        # Pad with zeros if needed
        while len(curr_parts) < len(latest_parts):
            curr_parts.append(0)
        while len(latest_parts) < len(curr_parts):
            latest_parts.append(0)
        
        return latest_parts > curr_parts
    except (ValueError, AttributeError):
        return False


def check_for_updates():
    """Check if update is available. Returns (has_update, latest_version)."""
    latest = get_latest_version()
    if latest:
        has_update = compare_versions(CURRENT_VERSION, latest)
        return has_update, latest
    return False, None
