class BankAccount:
 def __init__(self, account_balance=0):
       self.account_balance= account_balance 
       def deposit(self, amount):
             self.account_balance += amount
             return self.account_balance
       
       def withdraw(self, amount):
             if 0 < amount <= self.account_balance:
              return True
             return False
       def display_balance(self):
             return ["Current Balance:"], {self.account_balance}

    
