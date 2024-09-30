items = ["dog food", "oatmeal", "yougurt", "eggs", "bread"]
prices = [30, 3, 4, 2, 5]
for i in range(len(items)):
    print(f"I bought {items[i]} for {prices[i]}")
cost = 0
for price in prices:
    cost = cost + price
print(f"I spent ${cost}")

least = prices.index(min(prices))
print(f"I spent the least on {items[least]}, it was ${prices[least]}.")
