from datetime import datetime

def transform_orders(orders):
    transformed_orders = []
    for order in orders:
        total_price = order["quantity"] * order["price"]
        transformed_order = {
            "order_id": order["order_id"],
            "customer_name": order["customer_name"],
            "email": order["email"],
            "product": order["product"],
            "quantity": order["quantity"],
            "price": order["price"],
            "total_price": round(total_price, 2),
            "status": order.get("status") if total_price > 100 else "pending",
            "order_date": datetime.fromisoformat(order["order_date"]).strftime("%Y-%m-%d"),
        }
        transformed_orders.append(transformed_order)
    return transformed_orders
