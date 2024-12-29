from etl.extract_orders_from_mongodb import extract_orders
from etl.transform_orders import transform_orders
from etl.process_orders import load_transformed_orders
from analytics.analyse_orders import run_analysis
from visualization.visualize_orders import run_visualization


def main():
    try:
        # etl-Prozess
        print("etl-Prozess starten...")

        # Extraktion
        print("Extraktion...")
        orders = extract_orders()
        if not orders:
            raise ValueError("Keine Daten in der Datenbank gefunden. Der ETL-Prozess wird abgebrochen.")
        print(f"{len(orders)} Bestellungen extrahiert.")

        # Transformation
        print("Transformation...")
        transformed_orders = transform_orders(orders)
        print(f"{len(transformed_orders)} Bestellungen transformiert.")

        # Laden
        print("Laden...")
        load_transformed_orders(transformed_orders)
        print("Daten erfolgreich geladen!")

        # Analyse
        cancellation_rate = run_analysis()

        # Visualisierung
        run_visualization(cancellation_rate)

    except ValueError as ve:
        print(f"Fehler: {ve}")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    main()
