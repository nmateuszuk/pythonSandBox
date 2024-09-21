from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

coffeeMachine.report()
print(f"Available drinks : {menu.get_items()}")

while True:
    pick = input("Enter a drink name (or 'off' to exit): ").lower()
    if pick == 'off':
        break
    if not menu.find_drink(pick):
        print("Drink not found. Please try again.")
        continue

    drink = menu.find_drink(pick)
    if coffeeMachine.is_resource_sufficient(drink):
        print(f"cost of drink {drink.cost} ")
        if moneyMachine.make_payment(drink.cost):
            coffeeMachine.make_coffee(drink)
        else:
            continue
    else:
        continue
