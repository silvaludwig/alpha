#exemplo expense management chat GPT

class Income:
    def __init__(self, source, amount, account):
        self.source = source
        self.amount = amount
        self.account = account

class Expense:
    def __init__(self, category, amount, account):
        self.category = category
        self.amount = amount
        self.account = account

class Category:
    def __init__(self, name):
        self.name = name

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class FinancialManager:
    def __init__(self):
        self.incomes = []
        self.expenses = []
        self.categories = []
        self.bank_accounts = []

    def add_income(self, source, amount, account):
        income = Income(source, amount, account)
        self.incomes.append(income)

    def add_expense(self, category, amount, account):
        expense = Expense(category, amount, account)
        self.expenses.append(expense)

    def add_category(self, name):
        category = Category(name)
        self.categories.append(category)

    def add_bank_account(self, name, balance):
        account = BankAccount(name, balance)
        self.bank_accounts.append(account)

    def display_incomes(self):
        print("Income Entries:")
        for income in self.incomes:
            print(f"Source: {income.source}, Amount: ${income.amount}, Account: {income.account}")

    def display_expenses(self):
        print("Expense Entries:")
        for expense in self.expenses:
            print(f"Category: {expense.category}, Amount: ${expense.amount}, Account: {expense.account}")

    def display_categories(self):
        print("Categories:")
        for category in self.categories:
            print(category.name)

    def display_bank_accounts(self):
        print("Bank Accounts:")
        for account in self.bank_accounts:
            print(f"Account: {account.name}, Balance: ${account.balance}")

# Example usage
manager = FinancialManager()
manager.add_bank_account("Savings", 1000)
manager.add_bank_account("Checking", 500)
manager.add_category("Groceries")
manager.add_income("Salary", 3000, "Savings")
manager.add_expense("Groceries", 100, "Checking")
manager.display_bank_accounts()
manager.display_categories()
manager.display_incomes()
manager.display_expenses()
