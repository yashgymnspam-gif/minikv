import time
from dataclasses import dataclass


@dataclass
class Entry:
    value: str
    expires_at: float | None = None

    @property
    def is_expired(self):
        if self.expires_at is not None:
            return time.time() >= self.expires_at
        return False


e1 = Entry("a")
e2 = Entry("b", time.time() + 100)
e3 = Entry("c", time.time() - 1)
e4 = Entry("d", time.time() + 1)
