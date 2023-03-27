from classes.request import Request
from classes.shop import Shop
from classes.store import Store


def main():
    store = Store(items={
        'конфеты': 10,
        'шоколад': 1,
        'вишня': 3
    })
    shop = Shop({
        'яблоки': 1,
        'груша': 5,
        'виноград': 2
    })

    while True:
        print('Для отправки товара из склада в магазин:\nДоставить (кол-во) (товар) из склад в магазин')
        print('Для отправки товара из магазина в склад:\nДоставить (кол-во) (товар) из магазина в склад')
        print('Сейчас на складе:')
        print(store.get_info())
        print('Сейчас в магазине:')
        print(shop.get_info())
        user = input('Введите: ').lower()
        if user == 'зaвершить':
            print('end')
            break
        request = Request(user)
        if request.check(shop, store):
            if request.to == 'магазин':
                shop.add(request.product, int(request.amount))
                store.remove(request.product, int(request.amount))
            else:
                store.add(request.product, int(request.amount))
                shop.remove(request.product, int(request.amount))


if __name__ == '__main__':
    main()
