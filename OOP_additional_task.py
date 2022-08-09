class Product:
    def __init__(self, prod_name: str, prod_price_uah: int, prod_amount: int):
        self.prod_name = prod_name
        self.prod_price_uah = prod_price_uah
        self.prod_amount = prod_amount

    def __str__(self):
        return f'{self.__class__.__name__} name: {self.prod_name} - ' \
               f'{self.prod_amount} pcs ({self.prod_price_uah} UAH per each)'

    def __repr__(self):
        return f'{self.__class__.__name__} name: {self.prod_name} - ' \
               f'{self.prod_amount} pcs ({self.prod_price_uah} UAH per each)'


class ProductStorage:
    def __init__(self):
        self.product = None
        self.storage = []

    def add_to_storage(self, product: Product):
        self.product = product
        return self.storage.append(product)

    def delete_from_storage(self, product: Product):
        self.product = product
        return self.storage.remove(product)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.storage}'

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.storage}'


class ShoppingCart:
    def __init__(self, p_storage: ProductStorage):
        self.p_storage = p_storage
        self.name = None
        self.amount = 0
        self.cart = []

    def add_item(self, name, amount):
        self.name = name
        self.amount = amount
        for item in self.p_storage.storage:
            if name == item.prod_name:
                if amount <= item.prod_amount:
                    self.cart.append({
                        'name': item.prod_name,
                        'amount': amount,
                        'price_uah': item.prod_price_uah
                    })
                else:
                    print(f'We don\'t have {amount} {name}s, '
                          f'only {item.prod_amount} pcs available')
        else:
            print(f'Sorry, we don\'t have {name} in our store.')

    def delete_item(self, name, amount):
        self.name = name
        self.amount = amount
        for item in self.cart:
            if name == item.name:
                self.cart.remove(item)

    def payment_receipt(self):
        total_sum = 0
        for item in self.cart:
            total_sum += item['price_uah'] * item['amount']
        print(f'Your order price: {total_sum} UAH')

        for i in self.cart:
            for j in self.p_storage.storage:
                if i['name'] == j.prod_name:
                    j.prod_amount = j.prod_amount - i['amount']

    def __str__(self):
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__.__name__}'


def main():
    prod1 = Product('T-shirt', 200, 20)
    prod2 = Product('Hoodie', 800, 7)
    storage1 = ProductStorage()
    storage1.add_to_storage(prod1)
    storage1.add_to_storage(prod2)
    cart1 = ShoppingCart(storage1)
    cart1.add_item('T-shirt', 2)
    cart1.add_item('Hoodie', 3)
    cart1.payment_receipt()
    print(cart1.p_storage.storage)


if __name__ == '__main__':
    main()
