products = {}
while True:
    command = input()
    if command == "buy":
        break
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        if price != products[name]["price"]:
            products[name]["price"] = price
for product, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{product} -> {total_price:.2f}")