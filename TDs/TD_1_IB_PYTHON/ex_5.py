import math
import cmath


def numeric_operations() -> None:
    """
    Prompt the user for two numeric values and display the results of various operations.

    The function performs and displays:
        - The quotient (a / b)
        - The remainder (a % b)
        - The power (a ** b)
        - The square root of their sum (√(a + b))
        - The complex number formed by combining a and b (a + bj)

    Notes:
        - Uses both `math` and `cmath` modules for handling real and complex numbers.
        - Handles division by zero and invalid numeric input gracefully.

    Example:
        Input:
            a = 4
            b = 2
        Output:
            Quotient: 2.00
            Remainder: 0.00
            Power: 16.00
            Square root of the sum: 2.45
            Complex number: (4+2j)

    Returns:
        None
    """
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        # Perform numeric operations
        quotient = a / b
        remainder = a % b
        power = a ** b
        square_root_sum = (
            math.sqrt(a + b)
            if a + b >= 0
            else cmath.sqrt(a + b)  # Handle complex roots gracefully
        )
        complex_number = complex(a, b)

        # Display results
        print(f"Quotient: {quotient:.2f}")
        print(f"Remainder: {remainder:.2f}")
        print(f"Power: {power:.2f}")
        print(f"Square root of the sum: {square_root_sum:.2f}")
        print(f"Complex number: {complex_number}")

    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
    except ValueError:
        print("Error: please enter valid numeric values.")
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")


if __name__ == "__main__":
    numeric_operations()
