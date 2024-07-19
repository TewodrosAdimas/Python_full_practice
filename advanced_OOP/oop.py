class Item:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity


item1 = Item("phone", 5000, 3)
print(item1.quantity)
print(type(item1))
