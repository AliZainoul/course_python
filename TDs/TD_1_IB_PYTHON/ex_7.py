import re


def quote_analysis() -> None:
    """
    Display a multi-line quote (as a raw string), then analyze it by:
        - Counting the total number of words.
        - Measuring the frequency of a user-specified word.

    The function:
        - Uses a raw multi-line string for the quote.
        - Converts all words to lowercase for consistent comparison.
        - Removes punctuation to ensure accurate word counting.
        - Prompts the user for a target word and displays its frequency.

    Example:
        Quote:
            "Happiness cannot be found far away
            if one forgets to cultivate it within oneself."

        Input:
            "happiness"
        Output:
            Number of words: 14
            Frequency of the word 'happiness': 1

    Returns:
        None
    """
    quote = r"""Happiness cannot be found far away
    if one forgets to cultivate it within oneself.
    True happiness grows quietly inside the heart,
    nourished by gratitude, kindness, and inner peace.
    Those who seek it outside often return empty-handed,
    while those who tend it within carry light wherever they go."""


    print("Quote:\n", quote)

    # Normalize text: lowercase and remove punctuation for clean analysis
    words = re.findall(r"\b\w+\b", quote.lower())
    word_count = len(words)

    search = input("Enter a word to search for: ").lower()
    frequency = words.count(search)

    print(f"Number of words: {word_count}")
    print(f"Frequency of the word '{search}': {frequency}")


if __name__ == "__main__":
    quote_analysis()
