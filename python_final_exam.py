"""
ami ekta file e sob korsi karon vinno vinno file create kore korle amar kache jamela lage . kon file a kon function seta vule jai . 
"""

import random

class Bank:
    def __init__(self):
        self.accounts = {} 
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(100000, 999999)
        for account_number in self.accounts:
            account_number = str(random.randint(100000, 999999))

        user = User(name, email, address, account_type, account_number)
        self.accounts[account_number] = user
        print(f"Account created successfully for {name} Account Number: {account_number}")
        return account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully")
        else:
            print("Account does not exist")

    def get_total_balance(self):
        self.total_balance = sum(user.balance for user in self.accounts.values())
        print(f"Total available balance in the bank: {self.total_balance}")

    def get_total_loan(self):
        print(f"Total loan amount given by the bank: {self.total_loan}")

    def toggle_loan_feature(self, status):
        self.loan_feature = status
        state = "on" if status else "off"
        print(f"Loan feature turned {state}.")


class User:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.transaction_history = []
        self.loans_taken = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"Deposited {amount}. Current Balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        elif amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrew {amount}. Current Balance: {self.balance}")
        else:
            print("Withdrawal amount must be greater than 0.")

    def check_balance(self):
        print(f"Available Balance: {self.balance}")

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if self.loans_taken >= 2:
            print("Loan limit reached.")
        elif bank.loan_feature:
            self.balance += amount
            self.loans_taken += 1
            bank.total_loan += amount
            self.transaction_history.append(f"Took a loan: {amount}")
            print(f"Loan of {amount} granted. Current Balance: {self.balance}")
        else:
            print("Loan feature is currently off.")

    def transfer(self, target_account_number, amount):
        if amount > self.balance:
            print("Insufficient balance to transfer.")
        elif target_account_number not in bank.accounts:
            print("Account does not exist.")
        else:
            self.balance -= amount
            bank.accounts[target_account_number].balance += amount
            self.transaction_history.append(f"Transferred {amount} to {target_account_number}")
            bank.accounts[target_account_number].transaction_history.append(f"Received {amount} from {self.account_number}")
            print(f"Transferred {amount} to {target_account_number}. Current Balance: {self.balance}")


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)

    def view_all_accounts(self):
        print("All User Accounts:")
        for account_number, user in self.bank.accounts.items():
            print(f"Account Number: {account_number}, Name: {user.name}, Balance: {user.balance}")

    def check_total_balance(self):
        self.bank.get_total_balance()

    def check_total_loan(self):
        self.bank.get_total_loan()

    def toggle_loan_feature(self, status):
        self.bank.toggle_loan_feature(status)

bank = Bank()
admin = Admin(bank)

account1 = admin.create_account("Akib", "akib@hasan.com", "Lakshmipur", "Savings")
account2 = admin.create_account("Sadia", "sadia123@gmail.com", "Dhaka uttara", "Current")

# User 
user1 = bank.accounts[account1]
user2 = bank.accounts[account2]

user1.deposit(500)
user1.withdraw(200)
user1.check_balance()
user1.view_transaction_history()

user1.take_loan(300)
user1.transfer(account2, 100)

admin.view_all_accounts()
admin.check_total_balance()
admin.check_total_loan()
