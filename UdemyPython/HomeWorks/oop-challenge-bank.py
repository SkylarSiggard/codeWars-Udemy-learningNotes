#Object Oriented Programming Challenge¶
#For this challenge, create a bank account class that has two attributes:
#owner
#balance
#and two methods:
#deposit
#withdraw
#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,deposit):
        self.balance = self.balance + deposit
        print(f"we just added {deposit}. total is now {self.balance}")
    def withdraw(self,withdraw):
        if withdraw > self.balance:
            print(f"Error: you dont have that much in your balance your balance is {self.balance}")
        else:
            self.balance = self.balance - withdraw
            print(f"we just took out {withdraw}. total is now {self.balance}")
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
