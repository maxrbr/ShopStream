from etl.extract_orders_from_mongodb import extract_orders
from etl.transform_orders import transform_orders
from etl.process_orders import load_transformed_orders
from analytics.analyse_orders import run_analysis
from visualization.visualize_orders import run_visualization


# Hauptprogramm: Steuerung des etl-Prozesses und der Analyse
def main():
    # etl-Prozess
    print("etl-Prozess starten...")
    print("Extraktion...")
    orders = extract_orders()
    print(f"{len(orders)} Bestellungen extrahiert.")

    print("Transformation...")
    transformed_orders = transform_orders(orders)
    print(f"{len(transformed_orders)} Bestellungen transformiert.")

    print("Laden...")
    load_transformed_orders(transformed_orders)
    print("Daten erfolgreich geladen!")

    # Analyse durchführen
    run_analysis()

    #Visualisierung erstellen
    run_visualization()

if __name__ == "__main__":
    main()
