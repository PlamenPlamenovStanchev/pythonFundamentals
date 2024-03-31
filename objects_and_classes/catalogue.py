# class Catalogue:
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product_name):
#         self.products.append(product_name)
#
#     def get_by_letter(self, first_letter):
#         return sorted([product for product in self.products if product.startswith(first_letter)])
#
#     def __repr__(self):
#         items_str = "\n".join(sorted(self.products))
#         return f"Items in the {self.name} catalogue:\n{items_str}"
#
#
# catalogue1 = Catalogue("Electronics")
# catalogue1.add_product("Laptop")
# catalogue1.add_product("Television")
# catalogue1.add_product("Smartphone")
# catalogue1.add_product("Camera")
#
# print(catalogue1)
#
#
# print(catalogue1.get_by_letter("S"))
#
#
#
# print(catalogue.get_by_letter())


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string += "\n".join(sorted(self.products))
        return returning_string
