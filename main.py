from extract_orders_from_mongodb import extract_orders
from transform_orders import transform_orders
from process_orders import load_transformed_orders

def main():
    # ETL-Prozess
    print("Extraktion...")
    orders = extract_orders()
    print(f"{len(orders)} Bestellungen extrahiert.")

    print("Transformation...")
    transformed_orders = transform_orders(orders)
    print(f"{len(transformed_orders)} Bestellungen transformiert.")

    print("Laden...")
    load_transformed_orders(transformed_orders)
    print("Daten erfolgreich geladen!")

if __name__ == "__main__":
    main()
