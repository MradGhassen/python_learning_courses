class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self    
    def display_account_info(self):
        return f"{self.balance}"
    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name):
        self.name = name
        self.account = {"cheking" : BankAccount (.02, 1000), "savings" : BankAccount (.05,3000)}
    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance (self):
        print(f"User: {self.name} , checking balance {self.account['cheking'].display_account_info()}")
        print(f"User: {self.name} , savings balance {self.account['savings'].display_account_info()}")
        return  self

ghassen = User("ghassen")

ghassen.account['cheking'].deposit(100)
ghassen.display_user_balance()