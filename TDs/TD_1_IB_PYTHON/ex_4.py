def test_bounds_with_logical_operators():
    """
    Vérifie si une valeur est strictement comprise entre deux bornes,
    en utilisant explicitement les opérateurs logiques : and, or, not.
    """
    try:
        value = float(input("Entrez une valeur : "))
        lower = float(input("Entrez la borne inférieure : "))
        upper = float(input("Entrez la borne supérieure : "))

        # Test logique : entre les bornes mais différent des bornes
        is_between = (value > lower) and (value < upper)
        is_not_equal_to_bounds = not (value == lower or value == upper)

        result = is_between and is_not_equal_to_bounds

        print(f"La valeur est strictement entre les bornes (exclues) : {result}")

    except ValueError:
        print("Erreur : veuillez entrer uniquement des valeurs numériques valides.")


if __name__ == "__main__":
    test_bounds_with_logical_operators()
