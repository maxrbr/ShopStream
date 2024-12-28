from pymongo import MongoClient
from faker import Faker
import random
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

connection_string = config["mongodb_connection_string"]
client = MongoClient(connection_string)
db = client["shopstream"]  # Datenbank erstellen oder verbinden
orders_collection = db["orders"]  # Collection für Bestellungen

# Faker initialisieren
faker = Faker()

# Beispiel: Daten generieren
def generate_order_data(num_orders):
    orders = []
    for _ in range(num_orders):
        order = {
            "order_id": faker.uuid4(),
            "customer_name": faker.name(),
            "email": faker.email(),
            "product": faker.word(ext_word_list=["Laptop", "Smartphone", "Tablet", "Headphones"]),
            "quantity": random.randint(1, 5),
            "price": round(random.uniform(50, 500), 2),
            "order_date": faker.date_time_this_year().isoformat()
        }
        orders.append(order)
    return orders

# Daten generieren und in MongoDB laden
num_orders = 100  # Anzahl der Bestellungen
orders = generate_order_data(num_orders)
orders_collection.insert_many(orders)

print(f"{num_orders} Bestellungen wurden erfolgreich in MongoDB gespeichert.")
