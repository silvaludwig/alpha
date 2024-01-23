class ShoppingCart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])
    
    def insert_products(self, *products):
        for product in products:
            self._products.append(product)
    
    def list_products(self):
        print()
        for product in self._products:
            print(product.name, product.price)
        print()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


shoppin_cart = ShoppingCart()
p1, p2 = Product('pencil', 1.20), Product('shirt', 20)
shoppin_cart.insert_products(p1, p2)
shoppin_cart.list_products()
print(shoppin_cart.total())




    