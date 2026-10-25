
orders = [{"id": 101, "customer": "Alex", "amount": 1500, "status": "PLACED"},
          {"id": 102, "customer": "Emma", "amount": 2500, "status": "PLACED"},
          {"id": 103, "customer": "David", "amount": 900, "status": "SHIPPED"}, {
              "id": 104,
              "customer": "John",
              "amount": 1800,
              "status": "PLACED"
          }]

# 1. Add a new order

# 2. Update an order
for order in orders:
    if order["id"] == 102:
        order["status"] = "SHIPPED"

# 3. Find an order
order_101 = next(
    (order for order in orders if order["id"] == 101),
    None
)

print("Order 101:", order_101)

# 4. Find pending orders
pending_orders = [
    order for order in orders
    if order["status"] == "PLACED"
]

print("Pending orders:", pending_orders)

# 5. Calculate total sales
total_sales = sum(order["amount"] for order in orders)

print("Total sales:", total_sales)
