class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # balance is a private member
        #private member: start with __

    def get_balance(self):
        print("parent BankAccount is called\n")
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount


class SavingAccount(BankAccount):
    def __init__(self, initial_balance):
        #BankAccount.__init__(self, initial_balance) #needs self in here
         super().__init__(initial_balance)


    def get_balance(self):
        #calling parent from child
        #return BankAccount.get_balance(self)  #needs self
        return super().get_balance()

obj = SavingAccount(200)
print(obj.get_balance())


