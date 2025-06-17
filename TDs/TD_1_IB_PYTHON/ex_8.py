def clean_string(s: str) -> str:
    """
    Nettoie une chaîne :
    - Supprime les espaces aux extrémités
    - Met en minuscules
    - Supprime les voyelles
    """
    s = s.strip().lower()
    return ''.join(char for char in s if char not in "aeiouy")


if __name__ == "__main__":
    user_input = input("Entrez une chaîne : ")
    print("Chaîne nettoyée :", clean_string(user_input))
