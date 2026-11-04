# Python Inventory Manager

import csv
from pathlib import Path


def calculate_stock_value(price, quantity):
    return price * quantity


def is_low_stock(quantity, threshold=5):
    return quantity <= threshold


def calculate_inventory_value(products):
    total = 0

    for product in products:
        total += calculate_stock_value(
            product["price"],
            product["quantity"]
        )

    return total

def calculate_total_units(products):
    total = 0

    for product in products:
        total += product["quantity"]

    return total


def load_inventory(file_path):
    products = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, skipinitialspace=True)

        required_columns = {"name", "price", "quantity"}

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError("Invalid CSV columns.")

        for row in reader:
            name = row["name"].strip()
            price = int(row["price"])
            quantity = int(row["quantity"])

            if not name or price < 0 or quantity < 0:
                raise ValueError("Invalid product data.")

            products.append({
                "name": name,
                "price": price,
                "quantity": quantity
            })

    return products


def generate_report(products, threshold=5):
    total_value = calculate_inventory_value(products)
    
def generate_report(products, threshold=5):
    total_value = calculate_inventory_value(products)
    total_units = calculate_total_units(products)


    print("=== INVENTORY REPORT ===")

    for product in products:
        name = product["name"]
        quantity = product["quantity"]
        price = product["price"]

        stock_value = calculate_stock_value(price, quantity)

        if is_low_stock(quantity, threshold):
            status = "LOW STOCK"
        else:
            status = "OK"

        print(
            f"{name} | Qty: {quantity} | "
            f"Value: ${stock_value} | {status}"
        )

    print("------------------------")
    print(f"Total Inventory Value: ${total_value}")
    
    print("------------------------")
    print(f"Total Inventory Value: ${total_value}")
    print(f"Total Units: {total_units}")



def main():
    file_path = Path(__file__).resolve().parent / "inventory.csv"

    try:
        products = load_inventory(file_path)
        generate_report(products)

    except (FileNotFoundError, ValueError, KeyError, TypeError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

