def convert_temperature() -> None:
    """
    Convert a temperature from Celsius to Fahrenheit.

    The function:
        - Prompts the user to enter a temperature in Celsius.
        - Converts the input value to Fahrenheit using the formula:
              Fahrenheit = (Celsius × 9 / 5) + 32
        - Displays both values rounded to two decimal places.
        - Handles invalid (non-numeric) user inputs gracefully.

    Returns:
        None
    """
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        print("Please enter a valid numeric value.")
    except KeyboardInterrupt:
        print("\nConversion canceled by user.")


if __name__ == "__main__":
    convert_temperature()
