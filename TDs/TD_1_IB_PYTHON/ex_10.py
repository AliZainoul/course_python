def diagonal_display(s: str):
    """
    Affiche les lettres d'une chaîne en diagonale.
    """
    for i, char in enumerate(s):
        print(" " * i + char)


def remove_odd_indexed_chars(s: str) -> str:
    """
    Supprime les caractères aux indices impairs.
    """
    return s[::2]


if __name__ == "__main__":
    text = input("Entrez une chaîne : ")
    diagonal_display(text)
    print("Sans lettres impaires :", remove_odd_indexed_chars(text))
