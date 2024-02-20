stockDict = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak",
    "GE": "General Electric",
}

purchases = [
    ("GE", 100, "10-sep-2001", 48),
    ("CAT", 100, "1-apr-1999", 24),
    ("GE", 200, "1-jul-1998", 56),
]

# Create a dictionary to accumulate purchases by ticker symbol
purchase_summary = {}

# Populate the purchase summary dictionary
for purchase in purchases:
    stock_symbol, shares, date, price = purchase
    total_purchase_value = shares * price
    if stock_symbol in purchase_summary:
        purchase_summary[stock_symbol].append((shares, price, total_purchase_value))
    else:
        purchase_summary[stock_symbol] = [(shares, price, total_purchase_value)]

# Print the purchase summary
for stock_symbol, purchases in purchase_summary.items():
    print(f"\n------ {stockDict[stock_symbol]} ------")
    total_portfolio_value = 0
    for shares, price, total_value in purchases:
        print(f"{shares} shares at {price} dollars each")
        total_portfolio_value += total_value
    print(f"\nTotal value of stock in portfolio: ${total_portfolio_value}")
