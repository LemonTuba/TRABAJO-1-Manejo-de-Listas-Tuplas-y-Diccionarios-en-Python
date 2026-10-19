from pathlib import Path
import io
import contextlib
import importlib.util
from unittest.mock import patch

file_path = Path("/mnt/data/2630276_SifuentesDante_Colecciones.py")

code = r'''# ============================================================
# PYTHON COLLECTIONS: LISTS, TUPLES AND DICTIONARIES
# ============================================================
# Cover Page
# Name: Dante Cecilio Sifuentes Martinez.
# Student ID: 2630276.
# Group: IM 1-3.
#
# Executive Summary
# A list is an ordered and mutable collection that can store
# multiple values and be modified during program execution.
# A tuple is an ordered and immutable collection, useful for
# data that should not change, such as coordinates or fixed data.
# A dictionary stores data as key-value pairs, making it useful
# when information must be found by a unique key.
# This document contains six problems using lists, tuples,
# dictionaries, strings, numbers, loops, searches and updates.
# Each problem includes inputs, outputs, validations and test cases.
#
# Principles and Good Practices
# - Use lists when elements need to be added or removed frequently.
# - Use tuples for fixed data that should not be modified.
# - Use dictionaries when information is searched by a key.
# - Avoid modifying a list while iterating over it unless necessary.
# - Use descriptive dictionary keys such as "name", "age", or "price".
# - Write readable code and clear messages for the user.
# ============================================================


# ============================================================
# Problem 1: Shopping list basics
# ============================================================
# Description:
# Works with a list of products and demonstrates basic list
# operations. It creates a list, adds an item, counts the items,
# and checks whether a searched product is in the list.
#
# Inputs:
# - initial_items_text (string): comma-separated products.
# - new_item (string): product to add.
# - search_item (string): product to search.
#
# Outputs:
# - Items list
# - Total items
# - Found item
#
# Validations:
# - initial_items_text cannot be empty.
# - Empty items after splitting are rejected.
# - new_item and search_item cannot be empty.
#
# Test cases:
# 1) Normal: "apple,banana,orange", "milk", "banana"
# 2) Border: "apple", "bread", "bread"
# 3) Error: "", "milk", "apple"
#
# Diagrama de flujo:
# Input text -> Validate -> split/strip -> append -> len/in ->
# Display list, count and boolean.

def problem_1():
    print("\n--- Problem 1: Shopping list basics ---")

    initial_items_text = input(
        "Enter initial items separated by commas: "
    ).strip()
    new_item = input("Enter a new item: ").strip()
    search_item = input("Enter an item to search: ").strip()

    if not initial_items_text or not new_item or not search_item:
        print("Error: invalid input")
        return

    items_list = [
        item.strip() for item in initial_items_text.split(",")
        if item.strip()
    ]

    if not items_list:
        print("Error: invalid input")
        return

    items_list.append(new_item)
    is_in_list = search_item in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {str(is_in_list).lower()}")


# ============================================================
# Problem 2: Points and distances with tuples
# ============================================================
# Description:
# Uses tuples to represent two points in a 2D plane.
# The program calculates the Euclidean distance between the points
# and creates a tuple containing their midpoint.
#
# Inputs:
# - x1, y1, x2, y2 (float): coordinates of two points.
#
# Outputs:
# - Point A
# - Point B
# - Distance
# - Midpoint
#
# Validations:
# - All four inputs must be convertible to float.
# - No additional range restrictions are required.
#
# Test cases:
# 1) Normal: (0, 0), (3, 4)
# 2) Border: (2, 2), (2, 2)
# 3) Error: (0, abc), (3, 4)
#
# Diagrama de flujo:
# Input coordinates -> Convert to float -> Create tuples ->
# Calculate distance and midpoint -> Display results.

def problem_2():
    print("\n--- Problem 2: Points and distances with tuples ---")

    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
    except ValueError:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance:.2f}")
    print(f"Midpoint: {midpoint}")


# ============================================================
# Problem 3: Product catalog with dictionary
# ============================================================
# Description:
# Manages a small product catalog using a dictionary.
# The product name is the key and the unit price is the value.
# The program reads a product and quantity and calculates the total.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - Unit price
# - Quantity
# - Total
# - Error if the product does not exist
#
# Validations:
# - product_name cannot be empty.
# - quantity must be greater than 0.
# - The product must exist in the dictionary.
#
# Test cases:
# 1) Normal: "apple", 3
# 2) Border: "orange", 1
# 3) Error: "computer", 2
#
# Diagrama de flujo:
# Input product/quantity -> Validate -> Check dictionary key ->
# Calculate total -> Display result.

def problem_3():
    print("\n--- Problem 3: Product catalog with dictionary ---")

    product_prices = {
        "apple": 10.0,
        "banana": 8.0,
        "orange": 12.0,
        "milk": 25.0
    }

    product_name = input("Enter product name: ").strip().lower()

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Error: invalid input")
        return

    if not product_name or quantity <= 0:
        print("Error: invalid input")
        return

    if product_name not in product_prices:
        print("Error: product not found")
        return

    unit_price = product_prices[product_name]
    total_price = unit_price * quantity

    print(f"Unit price: {unit_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price:.2f}")


# ============================================================
# Problem 4: Student grades with dict and list
# ============================================================
# Description:
# Stores students in a dictionary where each key is a student name
# and each value is a list of grades. It calculates the average
# and determines whether the student passed with a boolean.
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - Grades
# - Average
# - Passed
# - Error if the student does not exist
#
# Validations:
# - student_name cannot be empty.
# - Student must exist in the dictionary.
# - Grade list must not be empty before calculating the average.
#
# Test cases:
# 1) Normal: "Alice"
# 2) Border: "Charlie"
# 3) Error: "David"
#
# Diagrama de flujo:
# Input student name -> Validate -> Search dictionary ->
# Check grades -> Calculate average -> Passed condition -> Display.

def problem_4():
    print("\n--- Problem 4: Student grades with dict and list ---")

    grades = {
        "Alice": [90.0, 85.0, 95.0],
        "Bob": [60.0, 70.0, 65.0],
        "Charlie": [70.0, 70.0, 70.0]
    }

    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Error: invalid input")
        return

    if student_name not in grades:
        print("Error: student not found")
        return

    grades_list = grades[student_name]

    if not grades_list:
        print("Error: invalid input")
        return

    average = sum(grades_list) / len(grades_list)
    is_passed = (average >= 70.0)

    print(f"Grades: {grades_list}")
    print(f"Average: {average:.2f}")
    print(f"Passed: {str(is_passed).lower()}")


# ============================================================
# Problem 5: Word frequency counter
# ============================================================
# Description:
# Reads a sentence, converts it to lowercase, and creates a list
# of words. A dictionary counts how many times each word appears.
# The program also finds the most common word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Words list
# - Frequencies
# - Most common word
#
# Validations:
# - sentence cannot be empty.
# - Simple punctuation is removed using replace().
# - The resulting word list must not be empty.
#
# Test cases:
# 1) Normal: "apple banana apple orange"
# 2) Border: "hello"
# 3) Error: "!!!"
#
# Diagrama de flujo:
# Input sentence -> Lowercase/clean punctuation -> Split into list ->
# Count words in dictionary -> Find maximum frequency -> Display.

def problem_5():
    print("\n--- Problem 5: Word frequency counter ---")

    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    punctuation = ".,;:!?\"'()[]{}"
    cleaned_sentence = sentence.lower()

    for symbol in punctuation:
        cleaned_sentence = cleaned_sentence.replace(symbol, " ")

    words_list = cleaned_sentence.split()

    if not words_list:
        print("Error: invalid input")
        return

    frequency_dict = {}

    for word in words_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    most_common_word = words_list[0]

    for word in frequency_dict:
        if frequency_dict[word] > frequency_dict[most_common_word]:
            most_common_word = word

    print(f"Words list: {words_list}")
    print(f"Frequencies: {frequency_dict}")
    print(f"Most common word: {most_common_word}")


# ============================================================
# Problem 6: Simple contact book (dictionary CRUD)
# ============================================================
# Description:
# Implements a mini contact book using a dictionary.
# The user can ADD, SEARCH, or DELETE a contact. ADD creates or
# updates a contact, SEARCH finds a phone number, and DELETE removes
# a contact from the dictionary.
#
# Inputs:
# - action_text (string): ADD, SEARCH, or DELETE.
# - name (string): contact name.
# - phone (string): phone number only for ADD.
#
# Outputs:
# - ADD: Contact saved
# - SEARCH: Phone or contact-not-found error
# - DELETE: Contact deleted or contact-not-found error
#
# Validations:
# - Normalize action_text to uppercase.
# - Action must be ADD, SEARCH, or DELETE.
# - name cannot be empty.
# - phone cannot be empty for ADD.
#
# Test cases:
# 1) Normal: ADD, "Daniel", "8341234567"
# 2) Border: SEARCH, "Alice"
# 3) Error: UPDATE, "Alice"
#
# Diagrama de flujo:
# Input action -> Validate action/name -> ADD/SEARCH/DELETE ->
# Update dictionary if needed -> Display result.

def problem_6():
    print("\n--- Problem 6: Simple contact book ---")

    contacts = {
        "Alice": "8341111111",
        "Bob": "8342222222",
        "Charlie": "8343333333"
    }

    action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()

    if action_text not in ("ADD", "SEARCH", "DELETE"):
        print("Error: invalid input")
        return

    name = input("Enter contact name: ").strip()

    if not name:
        print("Error: invalid input")
        return

    if action_text == "ADD":
        phone = input("Enter phone: ").strip()

        if not phone:
            print("Error: invalid input")
            return

        contacts[name] = phone
        print(f"Contact saved: {name}, {phone}")

    elif action_text == "SEARCH":
        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print(f"Contact deleted: {name}")
        else:
            print("Error: contact not found")


# ============================================================
# Main menu
# ============================================================

def main():
    print("==============================================")
    print("Python Collections: Lists, Tuples and Dicts")
    print("==============================================")

    while True:
        print("\nChoose a problem:")
        print("1. Shopping list")
        print("2. Points and distances")
        print("3. Product catalog")
        print("4. Student grades")
        print("5. Word frequency counter")
        print("6. Contact book")
        print("0. Exit")

        option = input("Enter an option: ").strip()

        if option == "1":
            problem_1()
        elif option == "2":
            problem_2()
        elif option == "3":
            problem_3()
        elif option == "4":
            problem_4()
        elif option == "5":
            problem_5()
        elif option == "6":
            problem_6()
        elif option == "0":
            print("Goodbye.")
            break
        else:
            print("Error: invalid input")


# ============================================================
# Conclusions
# ============================================================
# Lists are useful when a collection needs to change frequently,
# because elements can be added, removed, or updated.
# Tuples are useful for fixed data because their contents cannot
# be changed after creation.
# Dictionaries make it easy to organize and search information
# through key-value pairs.
# Combining dictionaries with lists is useful for structures such
# as student records, inventories, and other grouped information.
# These collections make programs more organized, flexible,
# and easier to process.
#
# ============================================================
# References
# ============================================================
# 1) Python Documentation - Built-in Types: Lists
#    https://docs.python.org/3/library/stdtypes.html#list
# 2) Python Documentation - Built-in Types: Tuples
#    https://docs.python.org/3/library/stdtypes.html#tuple
# 3) Python Documentation - Mapping Types: dict
#    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# 4) Python Documentation - Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
# 5) Python Documentation - More on Lists
#    https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#
# ============================================================
# END OF FILE
# ============================================================

if __name__ == "__main__":
    main()
'''

file_path.write_text(code, encoding="utf-8")

# Syntax validation
compile(code, str(file_path), "exec")

# Import without running the interactive main menu.
spec = importlib.util.spec_from_file_location("collections_assignment", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Validate all 18 required cases: 3 cases x 6 problems.
tests = [
    ("P1 normal", module.problem_1, ["apple,banana,orange", "milk", "banana"], False),
    ("P1 border", module.problem_1, ["apple", "bread", "bread"], False),
    ("P1 error", module.problem_1, ["", "milk", "apple"], True),

    ("P2 normal", module.problem_2, ["0", "0", "3", "4"], False),
    ("P2 border", module.problem_2, ["2", "2", "2", "2"], False),
    ("P2 error", module.problem_2, ["0", "abc", "3", "4"], True),

    ("P3 normal", module.problem_3, ["apple", "3"], False),
    ("P3 border", module.problem_3, ["orange", "1"], False),
    ("P3 error", module.problem_3, ["computer", "2"], True),

    ("P4 normal", module.problem_4, ["Alice"], False),
    ("P4 border", module.problem_4, ["Charlie"], False),
    ("P4 error", module.problem_4, ["David"], True),

    ("P5 normal", module.problem_5, ["apple banana apple orange"], False),
    ("P5 border", module.problem_5, ["hello"], False),
    ("P5 error", module.problem_5, ["!!!"], True),

    ("P6 normal", module.problem_6, ["ADD", "Daniel", "8341234567"], False),
    ("P6 border", module.problem_6, ["SEARCH", "Alice"], False),
    ("P6 error", module.problem_6, ["UPDATE", "Alice"], True),
]

for name, function, values, should_error in tests:
    iterator = iter(values)
    output = io.StringIO()

    with patch(
        "builtins.input",
        side_effect=lambda prompt="": next(iterator)
    ), contextlib.redirect_stdout(output):
        function()

    result = output.getvalue()

    if should_error:
        assert "Error:" in result, f"Failed: {name}"
    else:
        assert "Error:" not in result, f"Failed: {name}"


