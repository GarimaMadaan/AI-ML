class Laptop:

    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage} storage and {self.storage_type} storage type   .")    

    @classmethod
    def get_stroage_type(cls):
        print(f"Laptop has {cls.storage_type} storage.")    

    @staticmethod
    def calculate_discounted_price(price, discount):
        final_price = price - (price * discount / 100)
        print(final_price)

l1 = Laptop("8GB", "1TB")
l2 = Laptop("16GB", "512GB")        

l1.get_info()
l2.get_info()

Laptop.get_stroage_type()
# objects have higher priority than class when accessing attributes, whatever belongs to the class will also belong to the object, but whatever belongs to the object will not belong to the class, so when we access storage_type through l1, it will first check if l1 has storage_type attribute, if it does not find it, then it will check the class Laptop for storage_type attribute and it will find it there and return "ssd". if we access storage_type through Laptop class, it will directly check the class for storage_type attribute and return "ssd". so both l1.get_stroage_type() and Laptop.get_stroage_type() will return "ssd".
l1.get_stroage_type()

l1.calculate_discounted_price(40_000, 10)