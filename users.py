import accounts
insufFee = 5
int_rate = .03

class User:
    global insufFee
    global int_rate

    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = accounts.BankAccount(account, int_rate, 0)
        self.account_num2 = []

    def makeDeposit(self, account_name, amount):
        accounts.BankAccount.deposit(self.account, account_name, amount)
        return self

    def makeWithdraw(self, account, amount):
        accounts.BankAccount.withdraw(self.account, account, amount)
        return self

    def displayMyAccount(self, account):
        accounts.BankAccount.display_account_info(self.account, account)
        return self
    
    def accountYieldInterest(self, account):
        accounts.BankAccount.yield_interest(self.account, account)
        return self        
    
    def makeTransfer(self, amount, other_user, other_user_account):
        accounts.BankAccount.transfer_money(self.account, amount, other_user, other_user_account)

