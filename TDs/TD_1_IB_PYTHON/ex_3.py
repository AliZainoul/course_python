def is_numeric(value: str) -> bool:
    """
    Check if the given string can be safely converted to a float.

    Parameters
    ----------
    value : str
        The input string to test.

    Returns
    -------
    bool
        True if the string is a valid number, False otherwise.
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

# def is_numeric(value: str) -> bool:
#     """
#     Check whether a string represents a simple positive floating-point number.

#     This function validates unsigned numeric strings (integers or decimals)
#     without using `float()` or regular expressions.

#     It accepts:
#         - Digits only (e.g., "42")
#         - One decimal point (e.g., "3.14")
#         - Optional leading or trailing dot (".5" or "5.")

#     Limitations
#     -----------
#     ❌ Does NOT support:
#         - Negative numbers (e.g., "-3.4")
#         - Positive signs (e.g., "+5")
#         - Scientific notation (e.g., "1e3")
#         - Spaces or commas (e.g., "3,14")
#         - Unicode numerics (e.g., "Ⅷ", "²")

#     Parameters
#     ----------
#     value : str
#         The input string to check.

#     Returns
#     -------
#     bool
#         True if the string represents a valid simple float or integer, else False.

#     Examples
#     --------
#     >>> is_simple_float("3.14")
#     True
#     >>> is_simple_float("42")
#     True
#     >>> is_simple_float(".5")
#     True
#     >>> is_simple_float("-3.14")
#     False
#     >>> is_simple_float("1e3")
#     False
#     """
#     if not value:  # empty string
#         return False

#     # Reject multiple decimal points
#     if value.count('.') > 1:
#         return False

#     # Remove one decimal point (if any)
#     stripped = value.replace('.', '', 1)

#     # Check if remaining characters are digits
#     return stripped.isdigit()

def compare_values() -> None:
    """
    Interactively compare two user-input values and analyze their properties.

    This function prompts the user to enter two values and performs the following:
        1. **Type equality check**: Ensures both inputs share the same Python type.
           (Since both come from `input()`, they are always `str`, but this illustrates type checking.)
        2. **Numeric validation**: Determines whether each input can be safely converted to a float.
        3. **Value comparison**: If both are numeric, compares their numeric values and identifies
           which one is larger or if they are equal.

    The function is fully error-tolerant and will gracefully handle invalid or empty inputs.
    It prints the result of each stage to the console.

    Supported formats
    -----------------
    - Integers: "42"
    - Floats: "3.14"
    - Negative numbers: "-7.5"
    - Scientific notation: "1e3", "-2.5E-4"

    Notes
    -----
    - Non-numeric inputs (e.g., "abc", "3 4") are detected and excluded from numeric comparison.
    - Empty inputs or invalid conversions do not raise exceptions.

    Returns
    -------
    None
        This function prints its results directly to the console.

    Example
    -------
    >>> Enter the first value: -3.4
    >>> Enter the second value: 3.5
    Same type: True
    Both numeric: True
    bigger: 3.5 >= smaller: -3.4
    """

    try:
        # Prompt user for two values
        val1 = input("Enter the first value: ").strip()
        val2 = input("Enter the second value: ").strip()

        # Step 1: Type comparison (illustrative only — both are str)
        same_type = isinstance(val1, type(val2))
        print(f"Same type: {same_type}")

        # Step 2: Check numeric validity
        both_numeric = is_numeric(val1) and is_numeric(val2)
        print(f"Both numeric: {both_numeric}")

        # Step 3: Compare numerically if both are valid numbers
        if both_numeric:
            try:
                n1, n2 = float(val1), float(val2)
                bigger = max(n1, n2)
                smaller = min(n1, n2)

                result = (
                    f"bigger: {bigger} >= smaller: {smaller}"
                    if bigger != smaller
                    else f"bigger: {bigger} == smaller: {smaller}"
                )
                print(result)
            except Exception as e:
                print(f"Unexpected error during numeric comparison: {e}")
        else:
            print("Comparison not possible (non-numeric values).")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    compare_values()
