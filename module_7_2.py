class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        list_products = ''
        file = open(self.__file_name, 'r')
        list_products = str(file.read())
        file.close()
        return list_products

    def add(self, *products):
        new_products = []
        for product in products:
            if product.name in str(self.get_products()):
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                new_products.append(str(product) + '\n')
        file = open(self.__file_name, 'a')

        for product in new_products:
            print(file.write(str(product)))

        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())