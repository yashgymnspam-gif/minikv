import time

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


def test_set_then_get_returns_value():
    s = Store()
    s.set("a", 1)
    assert s.get("a") == 1


def test_setitem_then_getitem():
    s = Store()
    s["a"] = 1
    assert s["a"] == 1


def test_contains_missing_key_is_false():
    s = Store()
    assert "nope" not in s


def test_length_ignores_expired_keys():
    s = Store()
    s.set("a", 1, ttl=0.05)
    s.set("b", 1)
    time.sleep(0.1)
    assert len(s) == 1


def test_key_expires():
    s = Store()
    s.set("a", 1, ttl=0.05)
    assert s.get("a") == 1
    time.sleep(0.1)
    assert s.get("a") is None


def test_no_ttl_never_expires():
    s = Store()
    s.set("name", "Yash")
    time.sleep(0.1)
    assert s.get("name") == "Yash"


def test_get_removes_expired_key():
    s = Store()
    s.set("a", 1, ttl=0.05)
    time.sleep(0.1)
    assert s.get("a") is None
    assert "a" not in s._data
