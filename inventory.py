inventory = []

product_1 = {
    "name": "Laptop",
    "quantity": 5,
    "price": 899.99,
}
inventory.append(product_1)

product_2 = {
    "name": "Mouse",
    "quantity": 20,
    "price": 19.99,
}
inventory.append(product_2)

product_3 = {
    "name": "Keyboard",
    "quantity": 10,
    "price": 49.99,
}
inventory.append(product_3)


def calculate_total_value(inventory):
    if not isinstance(inventory, list):
        raise TypeError("Inventory must be a list.")

    total_value = 0.0

    required_keys = {"name", "quantity", "price"}

    for index, product in enumerate(inventory):
        if not isinstance(product, dict):
            raise TypeError(f"Product at index {index} must be a dictionary.")

        missing_keys = required_keys - product.keys()
        if missing_keys:
            missing = ", ".join(sorted(missing_keys))
            raise ValueError(
                f"Product at index {index} is missing required keys: {missing}."
            )

        if not isinstance(product["name"], str) or not product["name"].strip():
            raise ValueError(
                f"Product at index {index} must have a non-empty string name."
            )

        if isinstance(product["quantity"], bool) or not isinstance(
            product["quantity"], int
        ):
            raise TypeError(
                f"Quantity for product '{product['name']}' must be an integer."
            )

        if not isinstance(product["price"], float):
            raise TypeError(
                f"Price for product '{product['name']}' must be a float."
            )

        if product["quantity"] < 0 or product["price"] < 0:
            raise ValueError(
                f"Quantity and price for product '{product['name']}' "
                "cannot be negative."
            )

        product_value = product["quantity"] * product["price"]
        total_value += product_value

    return total_value


if __name__ == "__main__":
    final_total = calculate_total_value(inventory)
    print(f"Total inventory value: ${final_total:.2f}")
