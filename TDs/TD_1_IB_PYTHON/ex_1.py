def display_user_info() -> None:
    """
    Prompt the user for their first name, last name, and year of birth,
    then display a formatted message centered within 40 characters.

    The function:
        - Strips unnecessary whitespace from inputs.
        - Capitalizes the first name and converts the last name to uppercase.
        - Displays the formatted message centered to a width of 40 characters,
          with a green background highlight to visualize centering.

    Returns:
        None
    """
    # Get user input
    first_name = input("Enter your first name: ").strip().capitalize()
    last_name = input("Enter your last name: ").strip().upper()
    birth_year = input("Enter your year of birth: ").strip()

    # Validate input
    if not birth_year.isdigit():
        print("Invalid input: year of birth should contain digits only.")
        return

    # Build the message
    message = f"{first_name} {last_name}, born in {birth_year}"

    # Highlight using ANSI escape codes:
    # \033[42m → Green background
    # \033[30m → Black text
    # \033[0m  → Reset formatting
    WIDTH = 40
    centered_message = message.center(WIDTH)
    print("\033[42m\033[30m" + centered_message + "\033[0m")


if __name__ == "__main__":
    display_user_info()
