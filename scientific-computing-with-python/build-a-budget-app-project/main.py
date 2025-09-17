import budget
from budget import Category

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