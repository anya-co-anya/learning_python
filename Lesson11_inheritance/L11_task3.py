# Product Store

class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price

    def __str__(self):
        return {'type': self.type, 'name': self.name, 'price': self.price}

    def add_price_premium(self, price_premium):  # to increase price
        self.price += self.price*price_premium

    def add_discount(self, discount):  # to decrease price
        self.price -= self.price*discount



class ProductStore:
    price_premium = 0.3
    __income = 0

    def __init__(self):
        self.__product_list = []
        self.__product_amount = {}

    # adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
    def add(self, product, amount):
        if product in self.__product_list:
            self.__product_amount[hash(product)] += amount
        else:
            product.add_price_premium(self.price_premium)
            self.__product_list.append(product)
            self.__product_amount[hash(product)] = amount

    # adds a discount for all products specified by input identifiers (type or name).The discount must be specified in percentage
    def set_discount(self, identifier='', percent=0, identifier_type='name'):
        if identifier_type == 'name':
            for product in self.__product_list:
                if product.name == identifier:
                    product.add_discount(percent / 100)
        elif identifier_type == 'type':
            for product in self.__product_list:
                if product.type == identifier:
                    product.add_discount(percent / 100)
        else: raise ValueError('Incorrect identifier')

    def get_product(self, name=''):  # Custom function, returns product object by name
        found_products = []
        for product in self.__product_list:
            if product.name == name:
                found_products.append(product)
        if len(found_products) == 1:
            return found_products[0]
        else:
            raise ValueError('Several or No products with the same name')

    # removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
    def sell_product(self, product_name, amount):
        product = self.get_product(product_name)
        try:
            if self.__product_amount[hash(product)] >= amount:
                self.__product_amount[hash(product)] -= amount
                self.__income += product.price * amount
            else:
                raise ValueError('Not enough product in the store')
        except:
            raise ValueError('No such product in the store')

    # returns amount of many earned by ProductStore instance.
    def get_income(self):
        return self.__income

    # returns information about all available products in the store
    def get_all_products(self):
        for product in self.__product_list:
            print(f'product: {product.__str__()} \namount in the store: {self.__product_amount[hash(product)]}\n')

    # get_product_info(product_name) - returns a tuple with product name and amount of items in the store
    def get_product_info(self, product_name):
        product = self.get_product(product_name)
        return (product.name, self.__product_amount[hash(product)])



if __name__ == '__main__':
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    p3 = Product('Food', 'Burger', 5)

    store = ProductStore()

    store.add(p, 10)
    store.add(p2, 45)
    store.add(p3, 45)

    store.set_discount('Food', 50, 'type')
    print(p2.price, p3.price)

    store.sell_product('Ramen', 40)
    print(f'Income: {store.get_income()}')
    store.get_all_products()
    print(store.get_product_info('Ramen'))

