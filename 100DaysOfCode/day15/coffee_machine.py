from coffee_data import data

initial_state = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}


def return_count(quarters, dimes, nickels, pennies, price):
    given = 0
    given += quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if given < price:
        print("Sorry that's not enough money. Money refunded")
        return -given
    return given-price


def if_sufficient(drink):
    dict = {}
    dict["water"] = drink["water"] <= initial_state["water"]
    dict["milk"] = drink["milk"] <= initial_state["milk"]
    dict["coffee"] = drink["coffee"] <= initial_state["coffee"]

# Test Boolean Value of Dictionary
# Using list comprehension
    if all([value for value in dict.values()]):
        return True
    else:
        # for i in dict:
        #     if dict[i] is False:
        #         print(f"Sorry there is not enough {i}")
        for key, value in dict.items():
            if value is False:
                print(f"Sorry there is not enough {key}")
                return False


pick = ""

while pick != "off":
    pick = input("What would you like? (espresso/latte/cappucion): ").lower()

    if pick == "off":
        break

    if pick == "report":
        print(initial_state)
        continue
    if pick not in data:
        print("Invalid selection. Please try again.")
        continue

    if if_sufficient(data[pick]):
        price = data[pick]["price"]
        print(f"{pick} costs ${price:.2f}")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        change = return_count(quarters, dimes, nickels, pennies, price)

        if change >= 0:
            print(f"Here is ${change:.2f} in change.")
            print(f"Here is your {pick}. Enjoy!")
            initial_state['water'] -= data[pick]['water']
            initial_state['milk'] -= data[pick]['milk']
            initial_state['coffee'] -= data[pick]['coffee']
            initial_state['money'] += price
        else:
            print(f"Return {-change}. Pick another drink")
    else:
        print("Pick another drink")
        continue
