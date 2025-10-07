def reverse_string(s: str) -> str:
    """
    Return the reversed version of a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.

    Example:
        >>> reverse_string("Python")
        'nohtyP'
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Check whether a given string is a palindrome.

    A palindrome is a word, phrase, or sequence that reads
    the same backward as forward, ignoring case and punctuation.

    The function:
        - Converts the string to lowercase.
        - Removes all non-alphanumeric characters.
        - Compares the cleaned string to its reversed version.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("Hello")
        False
    """
    # Normalize the string: lowercase and remove non-alphanumeric characters
    s_clean = ''.join(filter(str.isalnum, s.lower()))
    return s_clean == reverse_string(s_clean)


if __name__ == "__main__":
    text = input("Enter a word or phrase: ")
    print("Palindrome:", is_palindrome(text))
