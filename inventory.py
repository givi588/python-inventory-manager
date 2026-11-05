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

def count_low_stock(products, threshold=5):
    count = 0

    for product in products:
        if is_low_stock(product["quantity"], threshold):
            count += 1

    return count

    

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
    total_units = calculate_total_units(products)
    low_stock_count = count_low_stock(products, threshold)

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
    print(f"Total Units: {total_units}")
    print(f"Low Stock Products: {low_stock_count}")



def export_inventory_report(products, output_path, threshold=5):
    with open(output_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "quantity", "stock_value", "status"])
        for product in products:
            name = product["name"]
            quantity = product["quantity"]
            stock_value = calculate_stock_value(product["price"], quantity)
            status = "LOW STOCK" if is_low_stock(quantity, threshold) else "OK"
            writer.writerow([name, quantity, stock_value, status])


def main():
    file_path = Path(__file__).resolve().parent / "inventory.csv"

    try:
        products = load_inventory(file_path)
        generate_report(products)
        output_path = Path(__file__).resolve().parent / "inventory_report.csv"
        export_inventory_report(products, output_path)
        print("CSV report exported successfully.")

    except (FileNotFoundError, ValueError, KeyError, TypeError, OSError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

