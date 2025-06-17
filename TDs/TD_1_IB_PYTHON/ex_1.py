def display_user_info():
    """
    Demande le prénom, nom et année de naissance à l'utilisateur
    puis affiche une phrase formatée justifiée sur 40 caractères.
    """
    first_name = input("Entrez votre prénom : ").strip().capitalize()
    last_name = input("Entrez votre nom : ").strip().upper()
    birth_year = input("Entrez votre année de naissance : ").strip()

    message = f"{first_name} {last_name}, né(e) en {birth_year}"
    print(message.center(40))


if __name__ == "__main__":
    display_user_info()
