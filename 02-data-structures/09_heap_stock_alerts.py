
import heapq
from itertools import count

# Priority queue
alert_queue = []

# Unique sequence for stable ordering
sequence = count()


def calculate_priority(stock):
    if stock == 0:
        return 1
    elif stock <= 5:
        return 2
    elif stock <= 10:
        return 3
    else:
        return 4


def add_stock_alert(store_id, article_code, stock):
    if stock < 0:
        return "Stock cannot be negative"

    priority = calculate_priority(stock)

    alert = {
        "store_id": store_id,
        "article_code": article_code,
        "stock": stock,
        "priority": priority
    }

    heapq.heappush(
        alert_queue,
        (priority, next(sequence), alert)
    )

    return f"Alert created for {article_code}"


def process_next_alert():
    if not alert_queue:
        return "No alerts available"

    priority, _, alert = heapq.heappop(alert_queue)

    return {
        "store_id": alert["store_id"],
        "article_code": alert["article_code"],
        "stock": alert["stock"],
        "priority": priority
    }


# Generate alerts
add_stock_alert("SE001", "ART1001", 15)
add_stock_alert("SE002", "ART1002", 0)
add_stock_alert("SE003", "ART1003", 4)
add_stock_alert("SE001", "ART1004", 8)
add_stock_alert("SE002", "ART1005", 0)

print("Processing stock alerts by priority:\n")

while alert_queue:
    alert = process_next_alert()
    print(alert)
