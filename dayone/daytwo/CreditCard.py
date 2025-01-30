class CreditCard:
    MAX_LIMIT = 500000  # Maximum limit
    DAILY_WITHDRAWAL_LIMIT = 100000  # Daily limit
    PER_TRANSACTION_LIMIT = 20000  # Per transaction withdrawal limit

    def __init__(self, card_number, cardholder_name):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.current_spending = 0
        self.daily_withdrawal = 0

    def withdraw_cash(self, amount):
        if amount > self.PER_TRANSACTION_LIMIT:
            print("Transaction failed: Exceeds per-transaction limit of 20K.")
            return

        if self.daily_withdrawal + amount > self.DAILY_WITHDRAWAL_LIMIT:
            print("Transaction failed: Exceeds daily withdrawal limit of 100K.")
            return

        if self.current_spending + amount > self.MAX_LIMIT:
            print("Transaction failed: Exceeds maximum credit limit of 500K.")
            return

        self.daily_withdrawal += amount
        self.current_spending += amount
        print(f"Withdrawal successful: {amount}. Remaining credit: {self.MAX_LIMIT - self.current_spending}")

    def pay_bill(self, amount):
        if self.current_spending + amount > self.MAX_LIMIT:
            print("Payment failed: Exceeds maximum credit limit of 500K.")
            return

        self.current_spending += amount
        print(f"Bill payment successful: {amount}. Remaining credit: {self.MAX_LIMIT - self.current_spending}")

    def reset_daily_withdrawal(self):
        self.daily_withdrawal = 0
        print("Daily withdrawal limit reset.")

    def check_balance(self):
        return self.MAX_LIMIT - self.current_spending
