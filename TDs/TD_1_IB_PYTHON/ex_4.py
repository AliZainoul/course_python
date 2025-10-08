def test_strict_bounds() -> None:
    """
    Prompt the user for a numeric value and two bounds, then check
    whether the value is strictly between the bounds (excluding the bounds)
    using explicit logical operators: and, or, not.

    The function:
        - Ensures the lower bound is less than the upper bound.
        - Uses a logical combination of `and` and `not` to exclude the bounds.
        - Displays the result to the user.

    Example:
        Input:
            Value: 5
            Lower bound: 2
            Upper bound: 8
        Output:
            True

        Input:
            Value: 2
            Lower bound: 2
            Upper bound: 8
        Output:
            False

    Returns:
        None
    """
    try:
        # Prompt for input
        value = float(input("Enter a value: "))
        lower = float(input("Enter the lower bound: "))
        upper = float(input("Enter the upper bound: "))

        # Validate bounds
        if lower > upper:
            raise ValueError("Lower bound must be strictly less than upper bound.")

        # Logical test: value strictly between bounds using and, or, not
        result = (value > lower) and (value < upper) and not (value == lower or value == upper)
        # result = lower < value < upper

        # print(f"Is the value = {value} strictly between the bounds lower = {lower} and upper = {upper} (excluded)? {result}")
        print(f"Is the {value=} strictly between the bounds {lower=} and {upper=} (excluded)? {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")


if __name__ == "__main__":
    test_strict_bounds()
