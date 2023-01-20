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
