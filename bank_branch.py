import accounts
import users

kyle = users.User('Kyle','krunge1@hotmail.com', 'Checking')
kyleSaving = users.User('Kyle', 'krunge1#@', 'Savings')
bob = users.User('Bob', 'bob@email', 'Checking')

kyle.makeDeposit('Checking', 300).accountYieldInterest('Checking').displayMyAccount('Checking').makeWithdraw('Checking', 500)
kyleSaving.makeDeposit('Savings', 500).accountYieldInterest('Savings').displayMyAccount('Savings')

bob.makeDeposit('Checking', 5000).makeWithdraw('Checking', 350).makeDeposit('Checking', 5000)