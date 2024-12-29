import matplotlib.pyplot as plt
from pymongo import MongoClient
from collections import Counter
import json

def get_database():
    with open("../config.json", "r") as config_file:
        config = json.load(config_file)
    client = MongoClient(config["mongodb_connection_string"])
    return client["shopstream"]

def plot_most_sold_products():
    db = get_database()
    processed_orders_collection = db["processed_orders"]
    orders = list(processed_orders_collection.find())

    product_counter = Counter(order["product"] for order in orders)
    most_sold = product_counter.most_common(5)

    product_names, counts = zip(*most_sold)

    plt.figure(figsize=(8, 6))
    plt.bar(product_names, counts, color='skyblue')
    plt.title("Top 5 meistverkaufte Produkte")
    plt.xlabel("Produkt")
    plt.ylabel("Anzahl Verkäufe")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def run_visualization():
    print("Visualisierung der Top 5 meistverkauften Produkte...")
    plot_most_sold_products()

if __name__ == "__main__":
    run_visualization()
