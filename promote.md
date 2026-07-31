# Inventory Pseudocode

## Programming Language

```text
Use Python 3.

Define inventory as a list.
Each item in inventory must be a product dictionary with:
    name: a string
    quantity: an integer
    price: a float
```

## 1. Create the Inventory

```text
Create a list called inventory to store product dictionaries.

Create the first product as a dictionary:
    name is "Laptop"
    quantity is 5
    price is 899.99
Add the first product to inventory.

Create the second product as a dictionary:
    name is "Mouse"
    quantity is 20
    price is 19.99
Add the second product to inventory.

Create the third product as a dictionary:
    name is "Keyboard"
    quantity is 10
    price is 49.99
Add the third product to inventory.
```

## 2. Calculate the Total Inventory Value

```text
Function calculate_total_value(inventory):
    If inventory is not a list:
        Raise a TypeError saying inventory must be a list.

    Set total_value to 0.0

    For each product in inventory:
        If the product is not a dictionary:
            Raise a TypeError saying each product must be a dictionary.

        If name, quantity, or price is missing:
            Raise a ValueError listing the missing keys.

        If name is not a non-empty string:
            Raise a ValueError saying the product name is invalid.

        If quantity is not an integer:
            Raise a TypeError saying quantity must be an integer.

        If price is a bool, or not an int or float:
            Raise a TypeError saying price must be a number.

        If quantity or price is negative:
            Raise a ValueError saying quantity and price cannot be negative.

        Set product_value to product's quantity multiplied by product's price
        Add product_value to total_value

    Return total_value

Set final_total to calculate_total_value(inventory)
Print "Total inventory value: $" followed by final_total
```

## 3. Test Cases

```text
Test 1: Calculate the value of the full inventory
    Use the three products already stored in inventory.
    Call calculate_total_value with inventory.
    Check that the result is 5399.65.

Test 2: Calculate the value of an empty inventory
    Create an empty inventory list.
    Call calculate_total_value with the empty list.
    Check that the result is 0.0.

Test 3: Calculate the value of one product
    Create an inventory with one product:
        name is "Notebook"
        quantity is 4
        price is 2.50
    Call calculate_total_value with this inventory.
    Check that the result is 10.00.

Test 4: Reject a product with a missing key
    Create a product without price.
    Call calculate_total_value.
    Check that a ValueError is raised.

Test 5: Reject incorrect data types
    Create a product whose quantity is a string.
    Call calculate_total_value.
    Check that a TypeError is raised.

Test 6: Reject negative values
    Create a product whose quantity is negative.
    Call calculate_total_value.
    Check that a ValueError is raised.

Test 7: Reject an item that is not a dictionary
    Create an inventory containing a string.
    Call calculate_total_value.
    Check that a TypeError is raised.

Test 8: Reject inventory that is not a list
    Pass a dictionary instead of a list.
    Check that a TypeError is raised.

Test 9: Reject an empty product name
    Create a product whose name is only whitespace.
    Check that a ValueError is raised.

Test 10: Reject boolean quantity
    Create a product whose quantity is True.
    Check that a TypeError is raised.

Test 11: Accept an integer price
    Create a product whose price is the integer 10.
    Check that the total value is calculated correctly.

Test 12: Reject a negative price
    Create a product whose price is negative.
    Check that a ValueError is raised.
```
