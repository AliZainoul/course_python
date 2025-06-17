def display_people_table():
    """
    Affiche un tableau aligné des personnes avec :
    - nom, âge, métier
    """
    people = [
        ("Alice", 30, "Ingénieure"),
        ("Bob", 25, "Développeur"),
        ("Chloé", 35, "Designer"),
    ]

    print(f"{'Nom':<15}{'Âge':<5}{'Métier':<20}")
    print("-" * 40)
    for name, age, job in people:
        print(f"{name:<15}{age:<5}{job:<20}")


if __name__ == "__main__":
    display_people_table()
