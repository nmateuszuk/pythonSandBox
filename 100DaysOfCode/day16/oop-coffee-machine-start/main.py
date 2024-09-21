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

    if coffeeMachine.is_resource_sufficient(menu.find_drink(pick)):
        print(f"cost of drink {menu.return_price(pick)} ")
        if moneyMachine.make_payment(menu.return_price(pick)):
            coffeeMachine.make_coffee(menu.find_drink(pick))
        else:
            continue
    else:
        continue
