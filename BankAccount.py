class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance 
        BankAccount.accounts.append(self)
    def depposit (self, amount):
        self.balance += amount
        return self
    def withdraw (self,amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds:Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info (self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest (self):
        if self.balance > 0:
         self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

ghassen = BankAccount(.01,500)
ghada = BankAccount(.02,500)
ghassen.depposit(50).depposit(50).depposit(50).withdraw(50).yield_interest().display_account_info()
ghada.depposit(50).depposit(50).depposit(50).withdraw(50).yield_interest().display_account_info()

BankAccount.print_all_accounts()