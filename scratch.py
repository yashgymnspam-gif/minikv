class Store:
    def __init__(self):
        self._data = {}

    def set(self, key, value):
        self._data[key] = value

    def get(self, key):
        return self._data.get(key)

    def delete(self, key):
        if key in self._data:
            del self._data[key]
            return True
        return False

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        return key in self._data

    def __repr__(self):
        return f"Store({len(self._data)} keys)"

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]


s = Store()
s["name"] = "Yash"
print(s["name"])
print(s.get("missing"))
print(s["missing"])
