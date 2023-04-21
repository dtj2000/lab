class Account:
    def __init__(self, account_name: str, balance: float):
        """
        Initializes an Account object with the given account_name and balance.

        Parameters:
        account_name (str): The name of the account.
        balance (float): The initial balance of the account.
        """
        self.__account_name = account_name
        self.__balance = balance

    def deposit(self, amount: float) -> bool:
        """
        Deposits the given amount into the account.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        bool: True if the deposit was successful, False otherwise.
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the given amount from the account.

        Parameters:
        amount (float): The amount to withdraw.

        Returns:
        bool: True if the withdrawal was successful, False otherwise.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
        float: The current balance of the account.
        """
        return self.__balance

    def get_name(self) -> str:
        """
        Returns the name of the account.

        Returns:
        str: The name of the account.
        """
        return self.__account_name
