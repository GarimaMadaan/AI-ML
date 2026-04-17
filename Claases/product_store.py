class product:
    total_objects = 0
    def __init__(self, name, price): 
        self.name = name
        self.price = price
        product.total_objects += 1

    def get_info(self):
        print(f"Product name is {self.name} and price is {self.price}.")

    @staticmethod
    def calculate_discounted_price(price, discount):
        final_price = price - (price * discount / 100)
        print(final_price)    

p1 = product("laptop", 40_000)
p2 = product("mobile", 20_000)
p3 = product("tablet", 30_000) 

p1.calculate_discounted_price(40_000, 10)

p1.get_info()
p2.get_info()
p3.get_info()

print(f"Total products: {product.total_objects}")