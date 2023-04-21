class Account:
    def __init__(self, account_name, balance):
        self.__account_name = account_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__account_name