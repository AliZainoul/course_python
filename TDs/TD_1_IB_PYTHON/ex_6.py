def scientific_conversion():
    """
    Convertit un réel en notation scientifique (3 décimales),
    puis affiche la partie entière et fractionnaire.
    """
    try:
        num = float(input("Entrez un nombre réel : "))
        print(f"Notation scientifique : {num:.3e}")
        integer_part = int(num)
        fractional_part = abs(num - integer_part)
        print(f"Partie entière : {integer_part}")
        print(f"Partie fractionnaire : {fractional_part:.10f}")
    except ValueError:
        print("Entrée invalide.")


if __name__ == "__main__":
    scientific_conversion()
