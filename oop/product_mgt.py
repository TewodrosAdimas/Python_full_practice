class Product():
    def __init__(self,name,price,quality) :
        self.name = name
        self.price = price
        self.quality = quality

    def cal(self):
        print(f"Total price of {self.name} is {self.price * self.quality}")

product1 = Product('car', 500, 2)
product2 = Product('house', 800, 3)

product1.cal()
product2.cal()