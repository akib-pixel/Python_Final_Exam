from abc import ABC, abstractmethod

class Account(ABC):
    accounts = []

    def __init__(self, name, account_number, password, account_type):
        self.name = name
        self.account_no = account_number
        self.password = password
        self.balance = 0
        self.account_type = account_type
        Account.accounts.append(self)

    def change_info(self, name, password=None):
        self.name = name
        if password:
            self.password = password
            print(f"\n--> Name and Password are changed for Account No: {self.account_no}")
        else:
            print(f"\n--> Name is changed for Account No: {self.account_no}")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\n--> Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print(f"\n--> Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid withdrawal amount")

    @abstractmethod
    def show_info(self):
        pass


class SavingsAccount(Account):
    def __init__(self, name, account_number, password, interest_rate):
        super().__init__(name, account_number, password, "savings")
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print("\n--> Interest is applied!")
        self.deposit(interest)

    def show_info(self):
        print(f"Details of {self.account_type} account for {self.name}:")
        print(f"\tAccount Type: {self.account_type}")
        print(f"\tName: {self.name}")
        print(f"\tAccount No: {self.account_no}")
        print(f"\tCurrent Balance: ${self.balance}\n")


class SpecialAccount(Account):
    def __init__(self, name, account_number, password, limit):
        super().__init__(name, account_number, password, "special")
        self.limit = limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.limit:
            self.balance -= amount
            print(f"\n--> Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid withdrawal amount or overdraft limit reached")

    def show_info(self):
        print(f"Details of {self.account_type} account for {self.name}:")
        print(f"\tAccount Type: {self.account_type}")
        print(f"\tName: {self.name}")
        print(f"\tAccount No: {self.account_no}")
        print(f"\tCurrent Balance: ${self.balance}\n")


current_user = None

while True:
    if current_user is None:
        print("\n--> No user logged in!")
        choice = input("\n--> Register/Login (R/L): ").strip().upper()

        if choice == "R":
            name = input("Name: ")
            account_number = input("Account Number: ")
            password = input("Password: ")
            account_type = input("Savings Account or Special Account (sv/sp): ").strip().lower()

            if account_type == "sv":
                interest_rate = float(input("Interest rate: "))
                current_user = SavingsAccount(name, account_number, password, interest_rate)
            elif account_type == "sp":
                limit = float(input("Overdraft Limit: "))
                current_user = SpecialAccount(name, account_number, password, limit)
            else:
                print("Invalid account type selected.")
        elif choice == "L":
            account_number = input("Account Number: ")
            found = False
            for account in Account.accounts:
                if account.account_no == account_number:
                    current_user = account
                    found = True
                    break
            if not found:
                print("\n--> Account not found!")
        else:
            print("\n--> Invalid choice!")
    
    else:
        print(f"\nWelcome, {current_user.name}!\n")
        if current_user.account_type == "savings":
            print("1.Withdraw")
            print("2.Deposit")
            print("3.Show Info")
            print("4.Change Info")
            print("5.Apply Interest")
            print("6.Logout\n")

            option = input("Choose an option: ").strip()

            if option == "1":
                amount = float(input("Enter withdrawal amount: "))
                current_user.withdraw(amount)
            elif option == "2":
                amount = float(input("Enter deposit amount: "))
                current_user.deposit(amount)
            elif option == "3":
                current_user.show_info()
            elif option == "4":
                new_name = input("Enter new name: ")
                new_password = input("Enter new password (leave blank to keep current): ")
                current_user.change_info(new_name, new_password or None)
            elif option == "5":
                current_user.apply_interest()
            elif option == "6":
                current_user = None
            else:
                print("\n--> Invalid option!")
        
        elif current_user.account_type == "special":
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. Change Info")
            print("5. Logout\n")

            option = int(input("Chhose Option:"))

            if option == "1":
                amount = float(input("Enter withdrawal amount: "))
                current_user.withdraw(amount)
            elif option == "2":
                amount = float(input("Enter deposit amount: "))
                current_user.deposit(amount)
            elif option == "3":
                current_user.show_info()
            elif option == "4":
                new_name = input("Enter new name: ")
                new_password = input("Enter new password: ")
                current_user.change_info(new_name, new_password or None)
            elif option == "5":
                current_user = None
            else:
                print("\n--> Invalid option!")
