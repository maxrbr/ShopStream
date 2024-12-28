from pymongo import MongoClient
import json

def load_transformed_orders(transformed_orders):
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    connection_string = config["mongodb_connection_string"]
    client = MongoClient(connection_string)
    db = client["shopstream"]
    processed_orders_collection = db["processed_orders"]
    processed_orders_collection.insert_many(transformed_orders)
