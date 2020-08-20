stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0
for item in stock:
    total_price += stock.get(item, 0)*prices.get(item, 0)

print(f'Total price of the stock is {total_price}')