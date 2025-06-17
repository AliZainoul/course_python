def convert_temperature():
    """
    Convertit une température de Celsius à Fahrenheit.
    """
    try:
        celsius = float(input("Entrez la température en Celsius : "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        print("Veuillez entrer une valeur numérique valide.")


if __name__ == "__main__":
    convert_temperature()
