from pymongo import MongoClient
import json

def extract_orders():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    connection_string = config["mongodb_connection_string"]
    client = MongoClient(connection_string)
    db = client["shopstream"]
    orders_collection = db["orders"]
    return list(orders_collection.find())
