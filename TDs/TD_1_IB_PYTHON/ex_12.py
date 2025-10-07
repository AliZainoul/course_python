def display_people_table() -> None:
    """
    Displays a neatly aligned table of people with their:
      - Name
      - Age
      - Occupation

    Example:
        Name           Age  Occupation
        ----------------------------------------
        Alice          30   Engineer
        Bob            25   Developer
        Chloe          35   Designer

    Returns:
        None
    """
    people = [
        ("Alice", 30, "Engineer"),
        ("Bob", 25, "Developer"),
        ("Chloe", 35, "Designer"),
    ]

    WIDTH_NAME = 15
    WIDTH_AGE = 5
    WIDTH_JOB = 20

    # Use nested braces {} for the variable in format spec
    print(f"{'Name':<{WIDTH_NAME}}{'Age':<{WIDTH_AGE}}{'Occupation':<{WIDTH_JOB}}")
    print("-" * (WIDTH_NAME + WIDTH_AGE + WIDTH_JOB))

    for name, age, job in people:
        print(f"{name:<{WIDTH_NAME}}{age:<{WIDTH_AGE}}{job:<{WIDTH_JOB}}")


if __name__ == "__main__":
    display_people_table()
