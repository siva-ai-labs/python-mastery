
# 05_order_discount.py

def calculate_discount(order_amount):
    if order_amount >= 5000:
        discount_rate = 0.20
    elif order_amount >= 2000:
        discount_rate = 0.10
    elif order_amount >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = order_amount * discount_rate
    final_amount = order_amount - discount

    return final_amount, discount


order_amount = 3500

final_price, discount = calculate_discount(order_amount)

print(f"Original Price: {order_amount} SEK")
print(f"Discount: {discount:.2f} SEK")
print(f"Final Price: {final_price:.2f} SEK")
