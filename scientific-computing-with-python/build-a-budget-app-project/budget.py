class Category:
    
    def __init__(self, expence_cat):
        self.expence_cat = expence_cat
        self.ledger = []
        self.balance = 0

    def __str__(self):
        title = f'{self.expence_cat!s:*^30}'
        output = ''
        for item in self.ledger:
            output += f"\n{item['description'][:23]:23}{item['amount']:>7.2f}"
        total = f'\nTotal: {self.get_balance()}'
        return title + output + total

    def deposit(self, amount, description = ''):
        dict_val = {'amount': amount, 'description': description}
        self.ledger.append(dict_val)
        self.balance += amount

    def withdraw(self, amount, description = ''):
        dict_val = {'amount': amount * -1, 'description': description}
        if self.check_funds(amount):
            self.balance += amount * -1
            self.ledger.append(dict_val)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budget_category):
        dict_val = {'amount': amount * -1, 'description': f'Transfer to {budget_category.expence_cat}'}
        
        if self.check_funds(amount):
            self.balance += amount * -1
            self.ledger.append(dict_val)
            budget_category.deposit(amount, f'Transfer from {self.expence_cat}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True
