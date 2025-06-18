# === Color constants (ANSI) ===
ANSI_COLORS = {
    'green': '\033[92m',
    'red': '\033[91m',
    'reset': '\033[0m'
}

TABLE_WIDTH = 120
COMPARE_TABLE_WIDTH = 40

def colorize_bool(value: bool) -> str:
    """
    Return colored boolean string:
    green for True, red for False.
    """
    color = ANSI_COLORS['green'] if value else ANSI_COLORS['red']
    return f"{color}{value}{ANSI_COLORS['reset']}"

def print_tuples_info_table(tuples_info: list[tuple[str, tuple]]) -> None:
    """
    Print a single aligned table showing info of multiple tuples.
    tuples_info: list of tuples (name, tuple)
    """
    header = f"{'Nom':<20}{'id':<20}{'hash':<30}{'type':<20}{'Valeur'}"
    separator = "-" * TABLE_WIDTH
    print(header)
    print(separator)
    for name, t in tuples_info:
        print(f"{name:<20}{id(t):<20}{hash(t):<30}{str(type(t)):<20}{repr(t)}")
    print()  # blank line after table

def print_compare_tuples(name1: str, t1: tuple, name2: str, t2: tuple) -> None:
    """
    Print comparison table (equality and identity) between two tuples.
    """
    header = f"{'Comparaison':<25}{'Résultat'}"
    separator = "-" * COMPARE_TABLE_WIDTH
    print(header)
    print(separator)
    print(f"{name1} == {name2:<17}→ {colorize_bool(t1 == t2)}")
    print(f"{name1} is {name2:<17}→ {colorize_bool(t1 is t2)}\n")

def main() -> None:
    t_original: tuple = (1, 1, 1, 2, 33, 3, 4, 1, 2)
    t_copy: tuple = (1, 1, 1, 2, 33, 3, 4, 1, 2)

    # Print both tuples info in a single table
    print_tuples_info_table([
        ("t_original", t_original),
        ("t_copy", t_copy),
    ])

    # Print comparison info
    print_compare_tuples("t_original", t_original, "t_copy", t_copy)

if __name__ == "__main__":
    main()



'''
(base) 💻 ~/_COURSE_PYTHON_IB % python tuples.py
Nom                 id                  hash                          type                Valeur
------------------------------------------------------------------------------------------------------------------------
t_original          4451259600          -1058645544050122960          <class 'tuple'>     (1, 1, 1, 2, 33, 3, 4, 1, 2)
t_copy              4451259600          -1058645544050122960          <class 'tuple'>     (1, 1, 1, 2, 33, 3, 4, 1, 2)

Comparaison              Résultat
----------------------------------------
t_original == t_copy           → True
t_original is t_copy           → True

'''

"""
Why Two Separate Tuple Variables Can Have the Same Value and Same ID in Python
When you create two tuples with the exact same elements in Python, you expect their values to be equal — and indeed they are, since tuples compare equal if their contents match element-by-element.

However, it might come as a surprise that your two tuples also have the same id in memory. This means that instead of being two distinct objects with identical content, they actually reference the very same object in memory.

How is this possible?
Python performs an optimization called interning or object reuse for immutable objects like tuples, strings, and small integers. When Python creates an immutable object, it can reuse an existing object with the same content rather than creating a new one, to save memory and improve performance.

Example:
t_original = (1, 1, 1, 2, 33, 3, 4, 1, 2)
t_copy = (1, 1, 1, 2, 33, 3, 4, 1, 2)


Since the tuples are immutable and identical, the Python interpreter may store only one tuple object and bind both t_original and t_copy names to that same object. This is why:

t_original == t_copy returns True (same contents)
t_original is t_copy returns True (same object in memory)
id(t_original) == id(t_copy)

When does this happen?
For small or constant immutable objects defined directly in code at the module level or inside functions, Python often performs this optimization.

The exact behavior may depend on the Python implementation, version, or how and where the tuples are created.

If tuples are created dynamically at runtime, or contain mutable elements, interning is less likely.

Why is this optimization beneficial?
Memory efficiency: Saves memory by not duplicating identical immutable data.

Performance: Faster comparisons, since is can shortcut the equality check.

Consistency: Immutable objects being shared is safe and expected behavior.

Summary
Your two tuple variables refer to the same underlying tuple object because Python has optimized away duplicate immutable tuples with the same contents. This is why they have identical values and identical ids. It’s a neat demonstration of Python’s memory management and immutability guarantees.
"""