class BankAccount:
    def __init__(self, account_name='', account_number='', balance=0.0):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn {amount:.2f}. New balance: {self.balance:.2f}")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def transfer(self, recipient_account, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                recipient_account.balance += amount
                print(f"Transferred {amount:.2f} to {recipient_account.account_name}. New balance: {self.balance:.2f}")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Transfer amount must be positive.")

    def get_balance(self):
        return self.balance
