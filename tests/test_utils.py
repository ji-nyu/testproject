"""Tests for testproject utils (behavior matches code, not outdated docs)."""

from testproject.utils import add, get_users, parse_tags, to_upper


def test_add():
    assert add(2, 3) == 5


def test_to_upper_returns_lower_in_code():
    """Code uses lower() — documents claim uppercase (semantic drift demo)."""
    assert to_upper("Hello") == "hello"


def test_get_users_returns_dict():
    result = get_users(active=True)
    assert isinstance(result, dict)
    assert "users" in result


def test_parse_tags_not_sorted():
    """Code does not sort — semantic drift vs README/docstring."""
    assert parse_tags("b,a,c") == ["b", "a", "c"]
