def scientific_conversion() -> None:
    """
    Convert a real number into scientific notation (3 decimal places),
    then display its integer and fractional parts.

    The function:
        - Prompts the user to input a real number.
        - Displays the number in scientific notation using 3 decimal places.
        - Separates and displays the integer and fractional parts of the number.
        - Handles invalid inputs gracefully.

    Example:
        Input:
            1234.56789
        Output:
            Scientific notation: 1.235e+03
            Integer part: 1234
            Fractional part: 0.5678900000

    Returns:
        None
    """
    try:
        num = float(input("Enter a real number: "))

        print(f"Scientific notation: {num:.3e}")

        integer_part = int(num)
        fractional_part = abs(num - integer_part)

        print(f"Integer part: {integer_part}")
        print(f"Fractional part: {fractional_part:.10f}")

    except ValueError:
        print("Error: please enter a valid numeric value.")
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")


if __name__ == "__main__":
    scientific_conversion()
