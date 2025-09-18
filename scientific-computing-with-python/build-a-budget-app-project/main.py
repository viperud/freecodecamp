import budget
from budget import Category

def create_spend_chart(categories):
    total_balance = 0
    title = 'Percentage spent by category'
    output = ''
    for category in categories:
        total_balance += category.get_balance()
    total_balance = total_balance 
    per_list = []
    for category in categories:
        cat_per = int((category.get_balance() / total_balance) * 100)
        round_per = cat_per - (cat_per % 10 if cat_per % 10 < 5 else -5)
        per_list.append(round_per)
    total_per = 100
    while total_per >= 0:
        output += f'\n{total_per:3}| '
        for cat_per in per_list:
            if cat_per >= total_per:
                output += 'o  '
            else:
                output += '   '
            cat_per -= 10
        total_per -= 10
    output += '\n'

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.expence_cat, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"
    return (title + output + footer).rstrip("\n")

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