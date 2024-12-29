import matplotlib.pyplot as plt
from pymongo import MongoClient
from collections import Counter
import json

def get_database():
    with open("config.json", "r") as config_file:
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


def plot_cancellation_rate(cancellation_rate):
    """
    Erstellt ein Liniendiagramm für die Rücklaufquote pro Monat.

    Args:
        cancellation_rate (dict): Dictionary mit Monaten als Schlüssel und Rücklaufquote als Wert.
                                  Beispiel: {'2024-01': 5.0, '2024-02': 4.2, ...}
    """
    # Daten vorbereiten
    months = list(cancellation_rate.keys())
    rates = list(cancellation_rate.values())

    # Diagramm erstellen
    plt.figure(figsize=(10, 6))
    plt.plot(months, rates, marker='o', linestyle='-', color='blue', label="Rücklaufquote (%)")
    plt.title("Rücklaufquote pro Monat", fontsize=16)
    plt.xlabel("Monat", fontsize=14)
    plt.ylabel("Rücklaufquote (%)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.tight_layout()

    # Diagramm anzeigen
    plt.show()

def run_visualization(cancellation_rate):
    print("Visualisierung der Top 5 meistverkauften Produkte...")
    plot_most_sold_products()
    print("Visualisierung der Rücklaufquote...")
    plot_cancellation_rate(cancellation_rate)

if __name__ == "__main__":
    run_visualization()
