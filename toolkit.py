"""Small collection of text utility functions."""


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards, ignoring case and spaces."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def slugify(text: str) -> str:
    """Convert text into a lowercase, hyphen-separated slug."""
    cleaned = "".join(ch if ch.isalnum() else "-" for ch in text.lower())
    while "--" in cleaned:
        cleaned = cleaned.replace("--", "-")
    return cleaned.strip("-")


def word_count(text: str) -> int:
    """Count the number of words in text."""
    return len(text.split())
