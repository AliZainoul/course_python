"""
TD 2 — Python Fundamentals: Functions, Data Structures & Best Practices
Author: Ali Zainoul (ali.zainoul.az@gmail.com)
Date: 2025-06-20

This script provides clean, testable, and well-structured solutions to all TD2 exercises,
written in English, using senior-level practices (type hints, separation of concerns,
explicit naming, clear docstrings, and robustness).
"""

from typing import Iterator
import copy
import string

# === Exercise 1 ===
def compute_stats(a: float = 1.0, b: float = 2.0, c: float = 3.0) -> tuple[float, float, float]:
    """Return the sum, average, and product of three numbers."""
    total = a + b + c
    average = total / 3
    product = a * b * c
    return total, average, product


# === Exercise 2 ===
def analyze_values(*args: float, sort: bool = False) -> tuple[float, float]:
    """Return the minimum and maximum of any number of integer arguments."""
    if not args:
        raise ValueError("At least one integer is required.")
    if sort:
        print("Sorted values:", sorted(args))
    return min(args), max(args)


# === Exercise 3 ===
def filter_long_words(words: list[str], min_length: int = 5) -> list[str]:
    """Return words whose length is strictly greater than min_length."""
    return list(filter(lambda w: len(w) > min_length, words))

    # Using map to filter words (one of several ways to achieve this)
    # return list(map(lambda w: w if len(w) > min_length else None, words))


# === Exercise 4 ===
def generate_powers(base: int, limit: int) -> Iterator[int]:
    """Yield successive powers of `base` less than `limit`."""
    power = 1
    while power < limit:
        yield power
        power *= base


# === Exercise 5 ===
GLOBAL_VAR = "I am global"

def inspect_namespaces() -> None:
    """Print local and global variables within nested scopes."""
    local_var = "I am local"

    def inner():
        internal_var = "I am internal"
        print("Inner locals:", dir())

    inner()
    print("Outer locals:", dir())
    print("Globals:", list(globals().keys()))


# === Exercise 6 ===
# def evaluate_expression() -> None:
#     """Ask user for an arithmetic expression, evaluate it, and store it dynamically."""
#     expression = input("Enter an arithmetic expression (e.g. 2 + 3 * 4): ")
#     result = eval(expression)
#     print("Result:", result)

#     exec(f"history = '{expression} = {result}'")
#     print(history)


# === Exercise 7 ===
def tuple_properties(t: tuple) -> None:
    """Print identity, hash and value of a tuple."""
    print("Tuple:", t)
    print("ID:", id(t))
    print("Hash:", hash(t))
    print("Self identity (t is t):", t is t)


# === Exercise 8 ===
def return_coordinates() -> tuple[int, int, int, int]:
    """Return a 4-element tuple representing coordinates."""
    return 10, 20, 30, 40

def unpack_and_average_coordinates() -> None:
    """Unpack the coordinates and compute the average."""
    x, y, z, t = return_coordinates()
    print(f"x={x}, y={y}, z={z}, t={t}")
    print("Average:", sum((x, y, z, t)) / 4)


# === Exercise 9 ===
def mutate_list(values: list[int]) -> None:
    """Append 99 to the list (side effect demonstration)."""
    values.append(99)

def demonstrate_list_copy() -> None:
    """Show the difference between mutable alias and deep copy."""
    original = [1, 2, 3]
    mutate_list(original)
    print("Modified:", original)

    duplicate = copy.deepcopy([1, 2, 3])
    mutate_list(duplicate)
    print("Deep copied:", duplicate)


# === Exercise 10 ===
def reversed_even_integers(n: int = 10) -> list[int]:
    """Return the first n even integers in reversed order."""
    return list(reversed(range(0, n * 2, 2)))


# === Exercise 11 ===
def print_glossary() -> None:
    """Display and update a simple dictionary of definitions."""
    glossary = {
        "variable": "Named memory reference",
        "function": "Reusable block of code",
        "loop": "Repeats instructions"
    }
    for term in sorted(glossary):
        print(f"{term}: {glossary[term]}")

    glossary["variable"] = "Data container"
    del glossary["loop"]
    print("\nUpdated glossary:", glossary)


# === Exercise 12 ===
def set_operations() -> None:
    """Perform union, intersection and symmetric difference on two sets."""
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Symmetric Difference:", a ^ b)


# === Exercise 13 ===
def list_comprehension_examples() -> tuple[list[int], list[int]]:
    """Return squares under 100 and their even values."""
    squares = [x**2 for x in range(1, 100) if x**2 < 100]
    even_squares = [s for s in squares if s % 2 == 0]
    return squares, even_squares


# === Exercise 14 ===
def dict_and_set_comprehensions() -> tuple[dict[str, int], set[int]]:
    """Generate a dict with squared indices and a set of word lengths."""
    letter_map = {letter: i**2 for i, letter in enumerate(string.ascii_lowercase)}
    words = ["python", "deeplearning", "marketing", "deep", "data", "science"]
    lengths = {len(word) for word in words}
    return letter_map, lengths


# === Exercise 15 ===
def generate_power_tuple(limit: int = 11) -> tuple[int, ...]:
    """Return a tuple of powers of 2 up to 2**limit."""
    return tuple(2**i for i in range(limit))


# === Main test suite ===
def main() -> None:
    """Run all exercises and print results."""

    ######## PART 1: Functions, Exercises 1 to 6 ########

    print("-"*32 + " [EX1] compute_stats " + "-"*32 + '\n')
    print("[EX1] compute_stats:", compute_stats())

    print("-"*32 + " [EX2] analyze_values " + "-"*32+ '\n')
    print("[EX2] analyze_values:", analyze_values(
        *(float(element) for element in input("Pleaser enter your numbers (sep = space): ").split()), sort=True)
    )

    print("-"*32 + " [EX3] filter_long_words " + "-"*32+ '\n')
    print("[EX3] filter_long_words:", filter_long_words(["sun", "python", "developer"]))

    print("-"*32 + " [EX4] generate_powers " + "-"*32+ '\n')
    print("[EX4] generate_powers:", list(generate_powers(2, 50)))

    print("-"*32 + " [EX5] inspect_namespaces " + "-"*32+ '\n')
    print("[EX5] inspect_namespaces:" , inspect_namespaces())

    # Uncomment to run Exercise 6, but be cautious with eval/exec
    # print("-"*32 + " [EX6] evaluate_expression " + "-"*32+ '\n')
    # evaluate_expression()



    ######## PART 2: Immutable Data Types, Exercises 7 to 8 ########

    print("-"*32 + " [EX7] tuple_properties " + "-"*32+ '\n')
    print("[EX7] tuple_properties:",tuple_properties((1, 2, 3)))

    print("-"*32 + " [EX8] return_coordinates " + "-"*32+ '\n')
    print("[EX8] return_coordinates:", return_coordinates())

    print("-"*32 + " [EX8] unpack_and_average_coordinates " + "-"*32+ '\n')
    print("[EX8] unpack_and_average_coordinates:", unpack_and_average_coordinates())

    ######## PART 3: Mutable Data Types, Exercises 9 to 12 ########
    print("-"*32 + " [EX9] demonstrate_list_copy " + "-"*32+ '\n')
    print("[EX9] demonstrate_list_copy:", demonstrate_list_copy())
    
    print("-"*32 + " [EX10] reversed_even_integers " + "-"*32+ '\n')
    print("[EX10] reversed_even_integers:", reversed_even_integers())

    print("-"*32 + " [EX11] print_glossary " + "-"*32+ '\n')
    print("[EX11] print_glossary:",     print_glossary())

    print("-"*32 + " [EX12] set_operations " + "-"*32+ '\n')
    print("[EX12] set_operations:", set_operations())

    ######## PART 4: Comprehensions, Exercises 13 to 15 ########

    print("-"*32 + " [EX13] Squares " + "-"*32+ '\n')
    squares, evens = list_comprehension_examples()
    print("[EX13] Squares:", squares, "Even Squares:", evens)

    letter_map, lengths = dict_and_set_comprehensions()
    print("-"*32 + " [EX14] Dict " + "-"*32+ '\n')
    print("[EX14] Dict:", list(letter_map.items())[:5])

    print("-"*32 + " [EX14] Set " + "-"*32+ '\n')
    print("[EX14] Set:", lengths)

    print("-"*32 + " [EX15] Powers of 2 " + "-"*32+ '\n')
    print("[EX15] Powers of 2:", generate_power_tuple())

if __name__ == "__main__":
    main()
