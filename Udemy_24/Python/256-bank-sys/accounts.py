import abc


class Account(abc.ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance
    
    
    @abc.abstractclassmethod
    def withdraw(self, amount):
        ...


    def deposit(self, amount):
        self.balance += amount
        self.details(f'(Deposit {amount})')

    def details(self, msg=''):
        print(f'Your balance: {self.balance:.2f} {msg}')


