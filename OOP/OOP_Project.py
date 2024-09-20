from BankAccount import *

Dave = BankAccount(10000,"Dave")
Sara = BankAccount(20000,"Sara")
Dave.get_balance()

Dave.deposit(2000)
Sara.deposit(1000)

Dave.withdraw(4000)
Sara.withdraw(200)

Dave.transfer(2000, Sara)

Jim = InterestRewardAccount(1000,'Jim')

Jim.get_balance()

Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingAccount(1000,'Blaze')
Blaze.get_balance()

Blaze.deposit(100)
Blaze .withdraw(10000)