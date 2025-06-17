def sentence_analysis():
    """
    Analyse une phrase :
    - Nombre de mots
    - Mot le plus long
    - Mots triés alphabétiquement (ordre inverse)
    - Phrase avec chaque mot capitalisé
    """
    sentence = input("Entrez une phrase : ").strip()
    words = sentence.split()

    print(f"Nombre de mots : {len(words)}")
    print(f"Mot le plus long : {max(words, key=len)}")
    print(f"Mots triés (ordre inverse) : {sorted(words, reverse=True)}")
    print("Phrase capitalisée :", ' '.join(word.capitalize() for word in words))


if __name__ == "__main__":
    sentence_analysis()
