
# 01_list_order_management.py

orders = [
    {"id": 1001, "customer": "Alex", "amount": 1200, "status": "PLACED"},
    {"id": 1002, "customer": "Emma", "amount": 2500, "status": "SHIPPED"},
    {"id": 1003, "customer": "John", "amount": 800, "status": "PLACED"}
]

def add_order(order):
    if any(o["id"] == order["id"] for o in orders):
        print("Order ID already exists")
        return

    orders.append(order)
    print(f"Order {order['id']} created")


def cancel_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            if order["status"] != "PLACED":
                print("Only placed orders can be cancelled")
                return

            order["status"] = "CANCELLED"
            print(f"Order {order_id} cancelled")
            return

    print("Order not found")


def get_active_orders():
    return [
        order for order in orders
        if order["status"] != "CANCELLED"
    ]


add_order({
    "id": 1004,
    "customer": "Sara",
    "amount": 1500,
    "status": "PLACED"
})

cancel_order(1001)

print("\nActive Orders:")
for order in get_active_orders():
    print(order)
