
# SIVA AI LABS
# Python Data Structures - Stack
# Use case: Undo Order Status Changes

orders = {
    101: {"customer": "Alex", "status": "PLACED"},
    102: {"customer": "Emma", "status": "PLACED"},
    103: {"customer": "David", "status": "PACKED"}
}

# Stack to track changes
undo_stack = []


def update_order_status(order_id, new_status):
    if order_id not in orders:
        return "Order not found"

    old_status = orders[order_id]["status"]

    if old_status == new_status:
        return "Order already has this status"

    # Save previous state before updating
    undo_stack.append({
        "order_id": order_id,
        "old_status": old_status,
        "new_status": new_status
    })

    orders[order_id]["status"] = new_status

    return f"Order {order_id}: {old_status} -> {new_status}"


def undo_last_change():
    if not undo_stack:
        return "Nothing to undo"

    # LIFO: remove most recent action
    last_change = undo_stack.pop()

    order_id = last_change["order_id"]
    old_status = last_change["old_status"]

    orders[order_id]["status"] = old_status

    return f"Undo successful: Order {order_id} restored to {old_status}"


def show_orders():
    for order_id, details in orders.items():
        print(order_id, details)


# Test
print(update_order_status(101, "PACKED"))
print(update_order_status(101, "SHIPPED"))
print(update_order_status(102, "CANCELLED"))

print("\nCurrent orders:")
show_orders()

print("\nUndo latest change:")
print(undo_last_change())

print("\nUndo another change:")
print(undo_last_change())

print("\nOrders after undo:")
show_orders()
