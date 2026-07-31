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

    def test_inventory_is_not_a_list(self):
        with self.assertRaisesRegex(TypeError, "Inventory must be a list"):
            calculate_total_value({"name": "Notebook", "quantity": 1, "price": 1.0})

    def test_inventory_is_none(self):
        with self.assertRaisesRegex(TypeError, "Inventory must be a list"):
            calculate_total_value(None)

    def test_empty_product_name(self):
        invalid_inventory = [{"name": "  ", "quantity": 1, "price": 1.0}]

        with self.assertRaisesRegex(ValueError, "non-empty string name"):
            calculate_total_value(invalid_inventory)

    def test_product_name_is_not_a_string(self):
        invalid_inventory = [{"name": 123, "quantity": 1, "price": 1.0}]

        with self.assertRaisesRegex(ValueError, "non-empty string name"):
            calculate_total_value(invalid_inventory)

    def test_boolean_quantity(self):
        invalid_inventory = [{"name": "Notebook", "quantity": True, "price": 1.0}]

        with self.assertRaisesRegex(TypeError, "Quantity"):
            calculate_total_value(invalid_inventory)

    def test_float_quantity(self):
        invalid_inventory = [{"name": "Notebook", "quantity": 1.5, "price": 2.0}]

        with self.assertRaisesRegex(TypeError, "Quantity"):
            calculate_total_value(invalid_inventory)

    def test_integer_price_is_accepted(self):
        products = [{"name": "Cable", "quantity": 2, "price": 10}]

        result = calculate_total_value(products)
        self.assertAlmostEqual(result, 20.0, places=2)

    def test_incorrect_price_type(self):
        invalid_inventory = [
            {"name": "Notebook", "quantity": 1, "price": "2.50"}
        ]

        with self.assertRaisesRegex(TypeError, "Price"):
            calculate_total_value(invalid_inventory)

    def test_boolean_price(self):
        invalid_inventory = [{"name": "Notebook", "quantity": 1, "price": True}]

        with self.assertRaisesRegex(TypeError, "Price"):
            calculate_total_value(invalid_inventory)

    def test_negative_price(self):
        invalid_inventory = [
            {"name": "Notebook", "quantity": 1, "price": -2.50}
        ]

        with self.assertRaisesRegex(ValueError, "cannot be negative"):
            calculate_total_value(invalid_inventory)

    def test_zero_quantity_and_price(self):
        products = [{"name": "Sample", "quantity": 0, "price": 0.0}]

        result = calculate_total_value(products)
        self.assertEqual(result, 0.0)

    def test_extra_keys_are_ignored(self):
        products = [
            {"name": "Cable", "quantity": 2, "price": 3.5, "sku": "C-01"}
        ]

        result = calculate_total_value(products)
        self.assertAlmostEqual(result, 7.0, places=2)

    def test_missing_name_key(self):
        invalid_inventory = [{"quantity": 1, "price": 1.0}]

        with self.assertRaisesRegex(ValueError, "missing required keys: name"):
            calculate_total_value(invalid_inventory)

    def test_product_is_none(self):
        with self.assertRaisesRegex(TypeError, "must be a dictionary"):
            calculate_total_value([None])


if __name__ == "__main__":
    unittest.main()
