from classes.shop import Shop
from classes.store import Store


class Request:
    def __init__(self, data):
        data = data.split()
        self._from_ = data[4]
        self._to = data[6]
        self._amount = int(data[1])
        self._product = data[2]

    @property
    def to(self):
        return self._to

    @property
    def from_(self):
        return self._from_

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product

    def check(self, shop: Shop, store: Store):
        if self.to == 'склад':
            if self.product not in shop.get_items(): return False
        if self.to == 'магазин':
            if self.product not in store.get_items(): return False
        return True
