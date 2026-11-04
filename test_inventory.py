import unittest

from inventory import (
    calculate_stock_value,
    is_low_stock,
    calculate_inventory_value,
    calculate_total_units,
    count_low_stock
)


class TestInventory(unittest.TestCase):

    
    def test_count_low_stock(self):
        products = [
            {"quantity": 2},
            {"quantity": 8},
            {"quantity": 4}
        ]

        result = count_low_stock(products)

        self.assertEqual(result, 2)


    def test_stock_value(self):
        result = calculate_stock_value(30, 12)
        self.assertEqual(result, 360)

    def test_low_stock(self):
        self.assertTrue(is_low_stock(3))

    def test_normal_stock(self):
        self.assertFalse(is_low_stock(12))

    def test_stock_boundary(self):
        self.assertTrue(is_low_stock(5))
        self.assertFalse(is_low_stock(6))

    def test_inventory_total(self):
        products = [
            {"name": "Keyboard", "price": 30, "quantity": 12},
            {"name": "Mouse", "price": 25, "quantity": 3}
        ]

        result = calculate_inventory_value(products)
        self.assertEqual(result, 435)

    def test_empty_inventory(self):
        self.assertEqual(calculate_inventory_value([]), 0)

    def test_total_units(self):
        products = [
            {"name": "Mouse", "price": 25, "quantity": 3},
            {"name": "Keyboard", "price": 30, "quantity": 12}
        ]

        result = calculate_total_units(products)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
