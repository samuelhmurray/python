def calculate_dollars(pennies, dimes, quarters, nickels):
    total_cents = pennies * 1 + dimes * 10 + quarters * 25 + nickels * 5
    dollar_amount = total_cents / 100  # Convert total cents to dollars
    return dollar_amount


dollar_amount = calculate_dollars(pennies=342, nickels=9, dimes=32, quarters=4)

print(f"${dollar_amount}")
