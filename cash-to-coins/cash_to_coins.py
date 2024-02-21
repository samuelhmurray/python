import mathx


def calculate_coins(dollar_amount):
    quarters = math.floor(dollar_amount / 0.25)
    remaining_amount = dollar_amount - (quarters * 0.25)
    dimes = math.floor(remaining_amount / 0.10)
    remaining_amount -= dimes * 0.10
    nickels = math.floor(remaining_amount / 0.05)
    remaining_amount -= nickels * 0.05
    pennies = round(remaining_amount / 0.01)

    return quarters, dimes, nickels, pennies


# Example usage:
dollar_amount = 8.69
quarters, dimes, nickels, pennies = calculate_coins(dollar_amount)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
