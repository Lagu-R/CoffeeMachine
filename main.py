# Import info about resources and items from module catalog.py
from catalog import MENU, resources

# A variable that represents the amount in the Coffee Machine
coin = 0


# check if resources is sufficient
def resources_sufficient(ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Calculate number of coins what inserted
def coin_calc():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many 0.25 coins")) * 0.25
    total += int(input("How many 0.1 coins")) * 0.1
    total += int(input("How many 0.05 coins")) * 0.05
    total += int(input("How many 0.01 coins")) * 0.01
    return total


# this function is about payment control . if user inserted enough money  return True
# otherwise return False
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global coin
        coin += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# make coffe by input parameters
# also subtract order coffee ingredients from CoffeMachine resources
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# check if Coffee Machine is on
is_on = True

# Whole Coffee machine program which Loop our function
# and make coffee for us <3 :) 
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${coin}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment = coin_calc()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

