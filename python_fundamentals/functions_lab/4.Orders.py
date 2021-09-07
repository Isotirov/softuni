def order_calculate(prod, qt):
    if prod == "coffee":
        price = 1.50 * qt
        return price
    elif prod == "water":
        price = 1.00 * qt
        return price
    elif prod == "coke":
        price = 1.40 * qt
        return price
    elif prod == "snacks":
        price = 2.00 * qt
        return price


product = input()
quantity = int(input())
print(f"{order_calculate(product, quantity):.2f}")