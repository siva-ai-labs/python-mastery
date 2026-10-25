
from collections import deque

# FIFO queue
order_queue = deque()

# Store processed orders
processed_orders = []


def place_order(order_id, customer, amount):
    # Prevent duplicate order IDs
    existing_ids = {
        order["order_id"] for order in order_queue
    }
    existing_ids.update(
        order["order_id"] for order in processed_orders
    )

    if order_id in existing_ids:
        return f"Order {order_id} already exists"

    if amount <= 0:
        return "Order amount must be positive"

    order = {
        "order_id": order_id,
        "customer": customer,
        "amount": amount,
        "status": "PLACED"
    }

    order_queue.append(order)

    return f"Order {order_id} added to queue"


def process_next_order():
    if not order_queue:
        return "No orders waiting"

    # FIFO: process oldest order
    order = order_queue.popleft()

    order["status"] = "PROCESSED"
    processed_orders.append(order)

    return f"Processed order: {order['order_id']}"


def show_pending_orders():
    print("\nPending Orders:")

    for order in order_queue:
        print(order)


def show_processed_orders():
    print("\nProcessed Orders:")

    for order in processed_orders:
        print(order)


# Simulate incoming orders
print(place_order("ORD101", "Alex", 1500))
print(place_order("ORD102", "Emma", 2500))
print(place_order("ORD103", "David", 900))

show_pending_orders()

# Process two orders
print("\nProcessing:")
print(process_next_order())
print(process_next_order())

show_pending_orders()
show_processed_orders()
