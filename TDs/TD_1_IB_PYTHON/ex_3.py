def compare_values():
    """
    Interactive function to compare two user-input values and analyze their properties.

    The function performs three main checks:
    1. Type equality: Verifies if both inputs are of the same Python type
    2. Numeric validation: Checks if both inputs can be converted to valid numbers
    3. Value comparison: If both inputs are numeric, compares them using '>'

    Notes:
        - Numeric validation supports both integers (e.g., "123") and decimals (e.g., "12.34")
        - Non-numeric inputs will be detected and comparison will be skipped
        - The function handles user input directly and displays results to console

    Returns:
        None
    """
    # Get input values from user
    val1 = input("Entrez la première valeur : ")
    val2 = input("Entrez la deuxième valeur : ")

    # Check if both inputs are of the same type (they will be strings at this point)
    same_type = type(val1) == type(val2)

    # We should use isinstance(...)

    # Validate if both inputs are numeric by checking if they match the pattern of a number:
    # - Removes one decimal point (if exists) using replace('.', '', 1)
    # - Checks if remaining characters are all digits using isdigit()
    both_numeric = val1.replace('.', '', 1).isdigit() and val2.replace('.', '', 1).isdigit()
    print(val1.replace('.', '', 1), val2.replace('.', '', 1))

    # Display results of type comparison and numeric validation
    print(f"Types identiques : {same_type}")
    print(f"Numériques : {both_numeric}")

    # If both values are numeric, convert them to floats and compare
    if both_numeric:
        n1, n2 = float(val1), float(val2)
        print(f"{n1} > {n2} : {n1 > n2}")
    else:
        print("Comparaison impossible (valeurs non numériques).")


if __name__ == "__main__":
    compare_values()
