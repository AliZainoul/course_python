def quote_analysis():
    """
    Affiche une citation multi-lignes en raw string,
    puis compte les mots et la fréquence d'un mot donné.
    """
    quote = r"""C'est en vain que l'on cherche au loin le bonheur
    quand on oublie de le cultiver à l'intérieur de soi-même."""

    print("Citation :\n", quote)

    words = quote.lower().split()
    word_count = len(words)
    search = input("Mot à rechercher : ").lower()
    frequency = words.count(search)

    print(f"Nombre de mots : {word_count}")
    print(f"Fréquence du mot '{search}' : {frequency}")


if __name__ == "__main__":
    quote_analysis()
