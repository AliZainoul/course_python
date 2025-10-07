def sentence_analysis() -> None:
    """
    Analyze a sentence provided by the user.

    This function performs the following analyses:
      - Counts the number of words.
      - Identifies the longest word.
      - Sorts the words alphabetically in reverse order.
      - Displays the sentence with each word capitalized.

    Example:
        Input:
            "Knowledge is power"
        Output:
            Number of words: 3
            Longest word: Knowledge
            Words sorted (reverse order): ['power', 'is', 'Knowledge']
            Capitalized sentence: Knowledge Is Power

    Returns:
        None
    """
    sentence = input("Enter a sentence: ").strip()
    words = sentence.split()

    print(f"Number of words: {len(words)}")
    print(f"Longest word: {max(words, key=len)}")
    print(f"Words sorted (reverse order): {sorted(words, reverse=True)}")
    print("Capitalized sentence:", ' '.join(word.capitalize() for word in words))


if __name__ == "__main__":
    sentence_analysis()
