import csv
from pathlib import Path


def calculate_stock_value(price, quantity):
    return price * quantity


def is_low_stock(quantity, threshold=5):
    return quantity <= threshold


def calculate_inventory_value(products):
    return sum(
        calculate_stock_value(product["price"], product["quantity"])
        for product in products
    )


def calculate_total_units(products):
    return sum(product["quantity"] for product in products)


def count_low_stock(products, threshold=5):
    return sum(
        is_low_stock(product["quantity"], threshold)
        for product in products
    )


def load_inventory(file_path):
    products = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        required_columns = {"name", "price", "quantity"}

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain name, price, and quantity columns.")

        for line_number, row in enumerate(reader, start=2):
            try:
                name = row["name"].strip()
                price = int(row["price"])
                quantity = int(row["quantity"])
            except (ValueError, TypeError, AttributeError):
                raise ValueError(
                    f"Invalid data on line {line_number}."
                ) from None

            if not name:
                raise ValueError(
                    f"Product name is missing on line {line_number}."
                )

            if price < 0 or quantity < 0:
                raise ValueError(
                    f"Negative price or quantity on line {line_number}."
                )

            products.append({
                "name": name,
                "price": price,
                "quantity": quantity,
            })

    return products


def generate_report(products, threshold=5):
    print("=== INVENTORY REPORT ===")

    for product in products:
        name = product["name"]
        quantity = product["quantity"]
        stock_value = calculate_stock_value(
            product["price"], quantity
        )
        status = "LOW STOCK" if is_low_stock(quantity, threshold) else "OK"

        print(
            f"{name} | Qty: {quantity} | "
            f"Value: ${stock_value} | {status}"
        )

    print("------------------------")
    print(f"Total Inventory Value: ${calculate_inventory_value(products)}")
    print(f"Total Units: {calculate_total_units(products)}")
    print(f"Low Stock Products: {count_low_stock(products, threshold)}")


def export_inventory_report(products, output_path, threshold=5):
    with open(output_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "quantity", "stock_value", "status"])

        for product in products:
            quantity = product["quantity"]
            stock_value = calculate_stock_value(
                product["price"], quantity
            )
            status = "LOW STOCK" if is_low_stock(quantity, threshold) else "OK"

            writer.writerow([
                product["name"],
                quantity,
                stock_value,
                status,
            ])


def main():
    folder = Path(__file__).resolve().parent
    input_path = folder / "inventory.csv"
    output_path = folder / "inventory_report.csv"

    try:
        products = load_inventory(input_path)
        generate_report(products)
        export_inventory_report(products, output_path)
        print("CSV report exported successfully.")

    except (OSError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
