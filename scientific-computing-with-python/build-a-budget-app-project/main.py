class Category:
    
    def __init__(self, expence_cat):
        self.expence_cat = expence_cat
        self.ledger = []
        self.balance = 0.00

    def __str__(self):
        output = f'{self.expence_cat!s:*^30}'
        for item in self.ledger:
            amount = item['amount']
            des = item['description'][:30-len(str(amount))-1:]
            leng = len(des)
            output += f'\n{des}{amount:>{30-leng}}'
        output += f'\n{self.get_balance()}'
        return output

    def deposit(self, amount, description = ''):
        #dict_val = {'amount': f'{amount:.2f}', 'description': f'intial {description}'}
        dict_val = {'amount': amount, 'description': description}
        self.ledger.append(dict_val)
        self.balance += amount

    def withdraw(self, amount, description = ''):
        dict_val = {'amount': amount * -1, 'description': description}
        self.ledger.append(dict_val)
        if self.check_funds(amount):
            self.balance += amount * -1
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budget_category):
        var = budget_category.expence_cat
        dict_val = {'amount': amount * -1, 'description': f'Transfer to {var}'}
        self.ledger.append(dict_val)
        if self.check_funds(amount):
            self.balance += amount * -1
            budget_category.deposit(amount, 'deposit')
            #budget_category.ledger.append({'amount': amount, 'description': description})
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

def create_spend_chart(categories):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

#Test case 6
#food.deposit(900, 'deposit')
#food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
#print(food)