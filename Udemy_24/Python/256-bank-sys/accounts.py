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
        print('--')


class SavingsAccount(Account):
    def withdraw(self, amount):
        amount_after_withdraw = self.balance - amount
        if amount_after_withdraw >=0:
            self.balance -= amount
            self.details(f'(Withdraw {amount})')
            return self.balance

        print('Impossible to withdraw')
        self.details(f'(Denied {amount})')

class CurrentAccount(Account):
    def __init__(self, agency, account, balance=0, limit=0):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdraw(self, amount):
        amount_after_withdraw = self.balance - amount
        max_limit = -self.limit

        if amount_after_withdraw >= max_limit:
            self.balance -= amount
            self.details(f'(Withdraw {amount})')
            return self.balance

        print('Impossible to withdraw')
        print(f'Your limit is {-self.limit:.2f}')
        self.details(f'(Denied {amount})')


if __name__ == '__main__':
    savings_account_test_1 = SavingsAccount(111, 222, 0)
    savings_account_test_1.withdraw(1)
    savings_account_test_1.deposit(10)
    savings_account_test_1.withdraw(5)
    print('###')
    current_account_test_1 = CurrentAccount(111, 222, 0, 100)
    current_account_test_1.withdraw(1)
    current_account_test_1.deposit(10)
    current_account_test_1.withdraw(109)

