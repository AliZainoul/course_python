def reverse_string(s: str) -> str:
    """
    Renvoie la chaîne inversée.
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Vérifie si la chaîne est un palindrome.
    """
    print(s)
    s_clean = ''.join(filter(str.isalnum, s.lower()))
    print(s_clean)

    return s_clean == reverse_string(s_clean)


if __name__ == "__main__":
    text = input("Entrez un mot ou une phrase : ")
    print("Palindrome :", is_palindrome(text))
