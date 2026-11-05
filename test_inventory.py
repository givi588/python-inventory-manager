import csv
import tempfile
import unittest
from pathlib import Path

from inventory import (
    calculate_stock_value,
    is_low_stock,
    calculate_inventory_value,
    calculate_total_units,
    count_low_stock,
    export_inventory_report,
)


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.products = [
            {"name": "Keyboard", "price": 30, "quantity": 12},
            {"name": "Mouse", "price": 25, "quantity": 3},
            {"name": "Monitor", "price": 150, "quantity": 7},
            {"name": "Headphones", "price": 60, "quantity": 2},
            {"name": "USB Cable", "price": 10, "quantity": 4},
        ]

    def test_stock_value(self):
        self.assertEqual(calculate_stock_value(30, 12), 360)

    def test_low_stock(self):
        self.assertTrue(is_low_stock(3))

    def test_normal_stock(self):
        self.assertFalse(is_low_stock(12))

    def test_stock_boundary(self):
        self.assertTrue(is_low_stock(5))

    def test_inventory_total(self):
        self.assertEqual(calculate_inventory_value(self.products), 1645)

    def test_empty_inventory(self):
        self.assertEqual(calculate_inventory_value([]), 0)

    def test_total_units(self):
        self.assertEqual(calculate_total_units(self.products), 28)

    def test_count_low_stock(self):
        self.assertEqual(count_low_stock(self.products), 3)

    def test_export_inventory_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "inventory_report.csv"
            export_inventory_report(self.products, output_path)
            self.assertTrue(output_path.exists())
            with open(output_path, "r", encoding="utf-8", newline="") as file:
                rows = list(csv.DictReader(file))
            self.assertEqual(len(rows), 5)
            self.assertEqual(rows[0]["name"], "Keyboard")
            self.assertEqual(rows[0]["stock_value"], "360")
            self.assertEqual(rows[0]["status"], "OK")
            self.assertEqual(rows[1]["name"], "Mouse")
            self.assertEqual(rows[1]["status"], "LOW STOCK")
            self.assertEqual(
                sum(int(row["stock_value"]) for row in rows),
                1645,
            )


if __name__ == "__main__":
    unittest.main()
