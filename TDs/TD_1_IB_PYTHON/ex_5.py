import cmath
import math

def numeric_operations():
    """
    Demande deux nombres et affiche :
    - Quotient
    - Reste
    - Puissance
    - Racine carrée de la somme
    - Complexe formé
    """
    try:
        a = float(input("Nombre 1 : "))
        b = float(input("Nombre 2 : "))

        print(f"Quotient : {a / b:.2f}")
        print(f"Reste : {a % b:.2f}")
        print(f"Puissance : {a ** b:.2f}")
        print(f"Racine carrée de la somme : {math.sqrt(a + b):.2f}")
        print(f"Complexe : {complex(a, b)}")

    except ZeroDivisionError:
        print("Division par zéro interdite.")
    except ValueError:
        print("Entrée invalide.")


if __name__ == "__main__":
    numeric_operations()
