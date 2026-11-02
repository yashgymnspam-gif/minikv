import pytest

from minikv.store import Store


def test_get_missing_returns_none():
    s = Store()
    assert s.get("nope") is None


def test_len_after_two_sets():
    s = Store()
    s.set("name", "Yash")
    s.set("age", 21)
    assert len(s) == 2


def test_delete_missing_returns_false():
    s = Store()
    assert s.delete("ptr") is False


def test_contains_after_set():
    s = Store()
    s.set("a", 1)
    assert "a" in s


def test_getitem_missing_raises():
    s = Store()
    with pytest.raises(KeyError):
        s["missing"]
