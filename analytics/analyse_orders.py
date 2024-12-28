import json
from pymongo import MongoClient
from collections import Counter

# Verbindung zur MongoDB herstellen
def get_database():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    connection_string = config["mongodb_connection_string"]
    client = MongoClient(connection_string)
    return client["shopstream"]

# Durchschnittlicher Bestellwert berechnen
def calculate_average_order_value():
    db = get_database()
    processed_orders_collection = db["processed_orders"]
    orders = list(processed_orders_collection.find())
    total_revenue = sum(order["total_price"] for order in orders)
    average_order_value = total_revenue / len(orders) if orders else 0
    print(f"Durchschnittlicher Bestellwert: {average_order_value:.2f}")

# Meistverkaufte Produkte analysieren
def most_sold_products():
    db = get_database()
    processed_orders_collection = db["processed_orders"]
    orders = list(processed_orders_collection.find())
    product_counter = Counter(order["product"] for order in orders)
    most_sold = product_counter.most_common(5)
    print("Top 5 meistverkaufte Produkte:")
    for product, count in most_sold:
        print(f"{product}: {count} Verkäufe")

# Umsatz pro Kunde berechnen
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

# Funktion zum Starten aller Analysen
def run_analysis():
    print("Analyse starten...")
    calculate_average_order_value()
    most_sold_products()
    revenue_per_customer()
    print("Analyse abgeschlossen.")

if __name__ == "__main__":
    run_analysis()
