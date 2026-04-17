class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self): 
        print(f"Balance for {self.name} is {self.__balance}.")  

    def set_balance(self, balance):
        if balance < 0:
            print("Balance cannot be negative.")
        else:
            self.__balance = balance     

acc1 = BankAccount("John", 1000)
print(acc1.name) # John
acc1.get_balance()

acc1.set_balance(2000)
acc1.get_balance()