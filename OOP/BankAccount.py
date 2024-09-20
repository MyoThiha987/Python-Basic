
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount,accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f'Account {self.name} created.\nBalance ${self.balance:.2f}')

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'\nDeposit completed')
        self.get_balance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account '{self.name}' only has a balance of {self.balance:.2f}")

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f'\nWithdraw completed')
            self.get_balance()

        except BalanceException as error:
            print(f'Withdraw interrupted : {error} ')

    def transfer(self,amount,account):
        try:
            print("\n********\n\nBeginning Transfer!!")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer completed!\n\n**********")

        except BalanceException as error:
            print(f"Transfer interrupted {error}")


class InterestRewardAccount(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print(f'\nDeposit completed')
        self.get_balance()


class SavingAccount(InterestRewardAccount):
    def __init__(self,initialAmount,accountName):
        super().__init__(initialAmount,accountName)
        self.fee = 5

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f'\nWithdraw completed')
            self.get_balance()

        except BalanceException as error:
            print(f"Withdraw  interrupted {error}")
