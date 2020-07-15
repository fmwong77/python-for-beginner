class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """
    This class generates checking account objects
    """
    type = "checking"
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= (amount + self.fee)

jacks_checking = Checking("files/jack_balance.txt", 1)
jacks_checking.deposit(50)
print(jacks_checking.balance)
jacks_checking.transfer(100)
print(jacks_checking.balance)
print(jacks_checking.type)
jacks_checking.commit()

checking = Checking("files/balance.txt", 1)
checking.deposit(50)
print(checking.balance)
checking.transfer(100)
print(checking.balance)
print(jacks_checking.type)
print(checking.__doc__)
checking.commit()

# account = Account("files/balance.txt")
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.deposit(300)
# print(account.balance)
# account.commit()

