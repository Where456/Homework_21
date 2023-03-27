from classes.store import Store


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, title, amount):
        if self.get_unique_items_count() == 5:
            return 'Unique product limit is full'
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

    def get_info(self):
        for k, v in self.get_items().items():
            if v != 0:
                print(k, v)
        return ''
