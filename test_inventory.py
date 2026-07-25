import unittest

from inventory import calculate_total_value, inventory


class TestCalculateTotalValue(unittest.TestCase):
    def test_full_inventory(self):
        result = calculate_total_value(inventory)
        self.assertAlmostEqual(result, 5399.65, places=2)

    def test_empty_inventory(self):
        result = calculate_total_value([])
        self.assertEqual(result, 0.0)

    def test_single_product(self):
        single_product_inventory = [
            {
                "name": "Notebook",
                "quantity": 4,
                "price": 2.50,
            }
        ]

        result = calculate_total_value(single_product_inventory)
        self.assertAlmostEqual(result, 10.00, places=2)

    def test_missing_key(self):
        invalid_inventory = [{"name": "Notebook", "quantity": 4}]

        with self.assertRaisesRegex(ValueError, "missing required keys: price"):
            calculate_total_value(invalid_inventory)

    def test_incorrect_quantity_type(self):
        invalid_inventory = [
            {"name": "Notebook", "quantity": "four", "price": 2.50}
        ]

        with self.assertRaisesRegex(TypeError, "Quantity"):
            calculate_total_value(invalid_inventory)

    def test_negative_quantity(self):
        invalid_inventory = [
            {"name": "Notebook", "quantity": -4, "price": 2.50}
        ]

        with self.assertRaisesRegex(ValueError, "cannot be negative"):
            calculate_total_value(invalid_inventory)

    def test_product_is_not_a_dictionary(self):
        with self.assertRaisesRegex(TypeError, "must be a dictionary"):
            calculate_total_value(["Notebook"])


if __name__ == "__main__":
    unittest.main()
