import time
from dataclasses import dataclass


@dataclass
class Entry:
    value: object
    expires_at: float | None = None

    @property
    def is_expired(self):
        if self.expires_at is not None:
            return time.time() >= self.expires_at
        return False


class Store:
    def __init__(self):
        self._data = {}

    def set(self, key, value, ttl=None):
        expires_at = None
        if ttl is not None:
            expires_at = time.time() + ttl
        self._data[key] = Entry(value, expires_at)

    def get(self, key):
        entry = self._live_entry(key)
        if entry is None:
            return None
        return entry.value

    def delete(self, key):
        if key in self._data:
            del self._data[key]
            return True
        return False

    def __len__(self):
        for key in list(self._data):
            self._live_entry(key)
        return len(self._data)

    def __contains__(self, key):
        return self._live_entry(key) is not None

    def __repr__(self):
        return f"Store({len(self)} keys)"

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        entry = self._live_entry(key)
        if entry is None:
            raise KeyError(key)
        return entry.value

    def _live_entry(self, key):
        entry = self._data.get(key)
        if entry is None:
            return None
        if entry.is_expired:
            self.delete(key)
            return None
        return entry
