"""
Create a BankAccount class that includes properties for account number, account name, and balance.

The class should have methods for withdrawing, depositing, and transferring funds between accounts.

Ensure that withdrawals or transfers do not result in a negative balance.

"""
from daytwo.BankAccount import BankAccount

if __name__ == "__main__":
    acc1 = BankAccount("2251401976001", "Rashedul", 1000)
    acc2 = BankAccount("2251401976002", "Manik", 500)

    acc1.deposit(200)
    acc1.withdraw(500)
    acc1.transfer(acc2, 300)

    print(f"Rashedul final balance: {acc1.get_balance():.2f}")
    print(f"Manik final balance: {acc2.get_balance():.2f}")
