class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid or insufficient balance")

    def get_balance(self):
        return self.__balance

# Test
acc = BankAccount("Aditya", 10000)
acc.deposit(5000)
acc.withdraw(2000)
print("Balance:", acc.get_balance())
