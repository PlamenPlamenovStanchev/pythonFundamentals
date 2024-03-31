# class Storage:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#
#     def add_product(self, product):
#         if len(self.storage) < self.capacity:
#             self.storage.append(product)
#             return f"Product {product} added to the storage."
#         else:
#             return "Storage is full. Cannot add more products."
#
#     def get_products(self):
#         return self.storage
#
#
# storage1 = Storage(3)
# print(storage1.add_product("Item1"))
# print(storage1.add_product("Item2"))
# print(storage1.add_product("Item3"))
# print(storage1.add_product("Item4"))
#
# print(storage1.get_products())


class Storage:
    storage = []
    def __init__(self, capacity):
        self.capacity = capacity

    def add_product (self, product: str):
        if self.capacity > len(Storage.storage):
            Storage.storage.append(product)

    def get_product(self):
        return Storage.starage
