# TO IGNORE

def compare_values() -> None:
    """
    Interactively compare two user-input values and analyze their properties.

    The function performs three main checks:
        1. **Type equality:** Verifies if both inputs are of the same Python type.
        2. **Numeric validation:** Checks if both inputs can be converted to valid numbers.
        3. **Value comparison:** If both inputs are numeric, compares them using the '>' operator.

    Notes:
        - Numeric validation supports both integers (e.g., "123") and decimals (e.g., "12.34").
        - Non-numeric inputs are detected and skipped from comparison.
        - The function handles user input directly and prints results to the console.

    Returns:
        None
    """
    # Prompt the user for two values
    val1 = input("Enter the first value: ").strip()
    val2 = input("Enter the second value: ").strip()

    # Type comparison (both are strings from input, but this line illustrates type checking)
    same_type = isinstance(val1, type(val2)) # Always True since both are str

    # Check if both values are numeric
    def is_numeric(value: str) -> bool:
        """Check if a string represents a valid integer or float number."""
        return value.isnumeric()
        # if value.count('.') > 1:  # More than one decimal point -> invalid
        #     return False
        # return value.replace('.', '', 1).isdigit()

    # TEST negative numbers ! 

    print(is_numeric(val1))
    print(is_numeric(val2))
    both_numeric = is_numeric(val1) and is_numeric(val2)


    # Display results of type and numeric checks
    print(f"Same type: {same_type}")
    print(f"Both numeric: {both_numeric}")

    # Compare numeric values if both are valid numbers
    if both_numeric:
        n1, n2 = float(val1), float(val2)
        bigger = max(n1, n2)
        smaller = min(n1, n2)

        # Single-line conditional expression (ternary)
        result = (
            f"bigger: {bigger} >= smaller: {smaller}"
            if bigger != smaller
            else f"bigger: {bigger} == smaller: {smaller}"
        )

        print(result)
    else:
        print("Comparison not possible (non-numeric values).")



if __name__ == "__main__":
    compare_values()
