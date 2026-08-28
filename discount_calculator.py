def calculate_total(price, quantity):
    return price * quantity


def apply_discount(price, quantity):
    total = calculate_total(price, quantity)
    if quantity >= 20:
        total = total * 0.90  # 10% discount
    elif quantity >= 10:
        total = total * 0.95  # 5% discount
    return total


order_a = apply_discount(35.00, 25)  # 20+ units -> 10% off
order_b = apply_discount(28.50, 15)  # 10-19 units -> 5% off

print("Order A final price:", order_a)
print("Order B final price:", order_b)