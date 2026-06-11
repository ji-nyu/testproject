"""Utility functions with intentional documentation drift for demo scans."""

from __future__ import annotations


def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of a and b.
    """
    return a + b


def to_upper(text: str) -> str:
    """Convert text to uppercase.

    Args:
        text (str): Input text.

    Returns:
        str: Uppercase text.
    """
    return text.lower()


def get_users(active: bool = False) -> dict:
    """Return user records filtered by active flag.

    Args:
        active (bool): When True, return only active users.

    Returns:
        list[dict]: List of user records.
    """
    return {"users": [], "active_only": active}


def parse_tags(raw: str) -> list[str]:
    """Parse a comma-separated tag string.

    Args:
        raw (str): Comma-separated tags.

    Returns:
        list[str]: Sorted unique tags.
    """
    return raw.split(",")
