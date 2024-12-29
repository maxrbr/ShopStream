import json

from datetime import datetime
from pymongo import MongoClient
from collections import Counter, defaultdict

def get_database():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    connection_string = config["mongodb_connection_string"]
    client = MongoClient(connection_string)
    return client["shopstream"]

def calculate_average_order_value():
    db = get_database()
    processed_orders_collection = db["processed_orders"]
    orders = list(processed_orders_collection.find())
    total_revenue = sum(order["total_price"] for order in orders)
    average_order_value = total_revenue / len(orders) if orders else 0
    print(f"Durchschnittlicher Bestellwert: {average_order_value:.2f}")

def most_sold_products():
    db = get_database()
    processed_orders_collection = db["processed_orders"]
    orders = list(processed_orders_collection.find())
    product_counter = Counter(order["product"] for order in orders)
    most_sold = product_counter.most_common(5)
    print("Top 5 meistverkaufte Produkte:")
    for product, count in most_sold:
        print(f"{product}: {count} Verkäufe")

def revenue_per_customer():
    db = get_database()
    processed_orders_collection = db["processed_orders"]
    orders = list(processed_orders_collection.find())
    customer_revenue = {}
    for order in orders:
        customer = order["customer_name"]
        customer_revenue[customer] = customer_revenue.get(customer, 0) + order["total_price"]
    print("Umsatz pro Kunde:")
    for customer, revenue in customer_revenue.items():
        print(f"{customer}: {revenue:.2f} EUR")


def calculate_cancellation_rate():
    db = get_database()
    processed_orders_collection = db["processed_orders"]
    orders = list(processed_orders_collection.find())

    monthly_data = defaultdict(lambda: {"total": 0, "cancelled": 0})
    for order in orders:
        order_date = datetime.strptime(order["order_date"], "%Y-%m-%d")
        month = order_date.strftime("%Y-%m")
        monthly_data[month]["total"] += 1
        if order["status"] == "cancelled":
            monthly_data[month]["cancelled"] += 1

    cancellation_rate = {
        month: (data["cancelled"] / data["total"]) * 100 if data["total"] > 0 else 0
        for month, data in monthly_data.items()
    }

    return dict(sorted(cancellation_rate.items()))

def run_analysis():
    print("Analyse starten...")
    calculate_average_order_value()
    most_sold_products()
    revenue_per_customer()
    print("Starte Analyse der Rücklaufquote...")
    cancellation_rate = calculate_cancellation_rate()
    print("Rücklaufquote pro Monat:")
    for month, rate in cancellation_rate.items():
        print(f"{month}: {rate:.2f}%")
    print("Analyse abgeschlossen.")

if __name__ == "__main__":
    run_analysis()
