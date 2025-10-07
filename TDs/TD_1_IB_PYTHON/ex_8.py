def clean_string(s: str) -> str:
    """
    Clean a string by performing the following operations:
        - Remove leading and trailing whitespace.
        - Convert all characters to lowercase.
        - Remove vowels (a, e, i, o, u, y).

    Args:
        s (str): The input string to clean.

    Returns:
        str: The cleaned string, without vowels and extra spaces.

    Example:
        >>> clean_string("  Python Language  ")
        'pthn lngg'
    """
    s = s.strip().lower()
    return ''.join(char for char in s if char not in "aeiouy")


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print("Cleaned string:", clean_string(user_input))
