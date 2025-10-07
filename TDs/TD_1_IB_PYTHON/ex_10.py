def diagonal_display(s: str) -> None:
    """
    Display the characters of a string diagonally.

    Each character of the string is printed on a new line,
    indented progressively to form a diagonal layout.

    Example:
        Input:
            "Hello"
        Output:
            H
             e
              l
               l
                o

    Args:
        s (str): The string to display.

    Returns:
        None
    """
    for i, char in enumerate(s):
        print(" " * i + char)


def remove_odd_indexed_chars(s: str) -> str:
    """
    Remove characters at odd indices from the string.

    This function keeps only characters at even indices (0, 2, 4, ...).

    Example:
        >>> remove_odd_indexed_chars("abcdef")
        'ace'

    Args:
        s (str): The input string.

    Returns:
        str: The resulting string with odd-indexed characters removed.
    """
    return s[::2]


if __name__ == "__main__":
    text = input("Enter a string: ")
    diagonal_display(text)
    print("Without odd-indexed letters:", remove_odd_indexed_chars(text))
