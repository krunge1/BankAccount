import accounts
import users

kyle = users.User('Kyle','krunge1@hotmail.com','Checking')
kyleSaving = users.User('Kyle', 'krunge1#@', 'Savings')
bob = users.User('Bob', 'bob@email', 'Checking')

kyle.account.deposit('Checking', 300).yield_interest('Checking').display_account_info('Checking').withdraw('Checking', 500)
kyleSaving.account.deposit('Savings', 500).yield_interest('Savings').display_account_info('Savings')

bob.account.deposit('Checking', 5000).withdraw('Checking', 350).deposit('Checking', 5000).transfer_money('Checking', 4000,kyle.account, 'Checking')

kyle.account.transfer_money('Checking', 5000, kyleSaving.account, 'Savings')