# Create a file with the User class, including the __init__ and make_deposit methods
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

# Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.account_balance -= amount # this method decrease the user's balance by the amount specified
# Add a display_user_balance method to the User class
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.account_balance}') # this method print the user's name and account balance to the terminal
# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

Adrien = User("Adrien", "adrien@python.com")
Nibbles = User("Mr Nibbles ", "Mr Nibbles@python.com")
Benny = User("Benny Bob", "Benny_Bob@python.com")
Adrien.make_deposit(150) # output: 150
Adrien.make_deposit(150) # output: 300
Adrien.make_deposit(150) # output: 450
Adrien.make_withdrawal(145) # output: 305
print(f'User: {Adrien.name} ,Balance: {Adrien.account_balance}')	# output: 305
Nibbles.make_deposit(1000) # output: 1000
Nibbles.make_deposit(1000) # output: 2000
Nibbles.make_withdrawal(400) # output: 1600
Nibbles.make_withdrawal(400) # output: 1200
print(f'User: {Nibbles.name} ,Balance: {Nibbles.account_balance}')	# output: 1200
Benny.make_deposit(10000) # output: 10000
Benny.make_withdrawal(500) # output: 9500
Benny.make_withdrawal(1000) # output: 8500
Benny.make_withdrawal(1000) # output: 7500
print(f'User: {Benny.name} ,Balance: {Benny.account_balance}')	# output: 7500


Nibbles.transfer_money(Adrien,400)
print(f'User: {Nibbles.name} ,Balance: {Nibbles.account_balance}')	
print(f'User: {Adrien.name} ,Balance: {Adrien.account_balance}')	 
