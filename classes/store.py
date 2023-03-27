from classes.storage import Storage


class Store(Storage):
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def add(self, title, amount):
        if 0 < amount <= self._capacity:
            if title in self._items:
                self._items[title] += amount
            else:
                self._items[title] = amount
            self._capacity -= amount
        else:
            pass

    def remove(self, title, amount):
        if title in self._items:
            if 0 < amount <= self._capacity:
                self._items[title] -= amount
                self._capacity += amount
        else:
            pass

    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items.keys())

    def get_info(self):
        for k, v in self.get_items().items():
            if v != 0:
                print(k, v)
        return ''
