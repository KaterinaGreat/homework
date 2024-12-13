class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self: str):
        return f'{self.name}, {self.weight}, {self.category}.'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        from pprint import pprint
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def add(self, *products: Product):
        names = []
        file = open(self.__file_name, 'a+')
        file.seek(0)
        for line in file:
            name = line.split(', '[0])
            names.append(name)
        for product in products:
            if product.name in names:
                print(f'продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{product.name}, {product.weight}, {product.category}\n')
                names.append(product.name)
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1,p2,p3)
print(s1.get_products())