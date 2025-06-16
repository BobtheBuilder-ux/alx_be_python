class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize bank account with optional initial balance"""
        self.account_balance = float(initial_balance)
    
    def deposit(self, amount):
        """Add the specified amount to account balance"""
        self.account_balance += float(amount)
    
    def withdraw(self, amount):
        """
        Deduct amount from balance if sufficient funds available
        Returns True if withdrawal successful, False otherwise
        """
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display current account balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")