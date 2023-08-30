# Create a file with the User class, including the __init__ and make_deposit methods
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

# Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.account_balance -= amount # this method decrease the user's balance by the amount specified
        return self

# Add a display_user_balance method to the User class
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.account_balance}') # this method print the user's name and account balance to the terminal
        return self

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self
        return other_user

Adrien = User("Adrien", "adrien@python.com")
Nibbles = User("Mr Nibbles ", "Mr Nibbles@python.com")
Benny = User("Benny Bob", "Benny_Bob@python.com")
Adrien.make_deposit(150).make_deposit(150).make_deposit(150).make_withdrawal(145).display_user_balance()
Nibbles.make_deposit(1000).make_deposit(1000).make_withdrawal(400).make_withdrawal(400).display_user_balance()  
Benny.make_deposit(10000).make_withdrawal(500).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()
Nibbles.transfer_money(Adrien,400)
