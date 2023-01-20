import users

insufFee = 5
int_rate = .03

class BankAccount:

    global insufFee
    global int_rate

    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = round(balance,2)

    def deposit (self, account, amount):
        if account == account:
            if amount > 0:
                self.balance += amount
                print(f"{self.name}: New balance is ${self.balance}")
            else: 
                self.balance = 0
            return  self

    def withdraw(self, account, amount):
        if account == account:
            if BankAccount.can_withdraw (self.balance, amount):
                # take balance less amount less 5
                self.balance -= amount
                print(f"{self.name}: New balance is ${self.balance}")
                return self
            else:
                self.balance -= insufFee
                print(f"{self.name}: Insufficent funds in account balance. An insufficient funds fee will be charged for ${insufFee}. Account balance after ${insufFee} is ${self.balance}")
            return self

    @staticmethod
    def can_withdraw (balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    def display_account_info(self, account):
        if account == account:
            print(f"{self.name}: Your account balance currently is ${self.balance}")
            return self 

    def yield_interest(self, account):
        if account == account:
            if self.balance > 0:
                previousBalance = self.balance
                self.balance = self.balance * (1 + self.int_rate)
                print(f"{self.name}: You have earned ${round(self.balance - previousBalance,2)} in interest this period. Your new balance is ${self.balance}")
            return self

    def transfer_money(self, account, amount, other_user, other_user_account):
        if account == account:
            if BankAccount.can_withdraw (self.balance, amount):
                # take balance less amount less 5
                self.balance -= amount
                print(f"{self.name}: New balance is ${self.balance}")
                BankAccount.deposit(other_user, other_user_account, amount)
                return self
            else:
                self.balance -= insufFee
                print(f"{self.name}: Insufficent funds in account balance. An insufficient funds fee will be charged for ${insufFee}. Account balance after ${insufFee} is ${self.balance}")
            return self

