"""
# File : tuples_advanced.py

Module de comparaison de tuples — identité et égalité

Ce script permet de générer, copier et comparer des tuples Python en affichant leurs
informations internes (id, hash, type, valeur) et en colorant les résultats des comparaisons.

Utilise ANSI pour colorer les résultats :
- ✅ `True` → vert
- ❌ `False` → rouge

Fonctionnalités principales :
- Génération dynamique de N tuples `(1,), (1, 2), ..., (1, 2, ..., N)`
- Trois variantes de copie pour tester l'égalité (`==`) et l'identité (`is`)
- Mode verbeux pour afficher les détails de chaque tuple
- Ligne de commande via `argparse` pour contrôler le comportement

────────────────────────────────────────────────────────────
🎛️ OPTIONS D’EXÉCUTION (CLI)
────────────────────────────────────────────────────────────

usage: tuples_advanced.py [-n NUMBER] [-v VARIANT] [--verbose]

Arguments :
  -n, --number     Nombre de tuples à générer (par défaut : 14)

  -v, --variant    Méthode de copie à utiliser (obligatoire si précisé) :
                   ▸ 1 → Copie via `tuple(t)` à partir de la liste originale
                   ▸ 2 → Nouvelle génération indépendante avec `generate_tuples(n)`
                   ▸ 3 → Définition manuelle d’une liste statique (jusqu'à 14)

  --verbose        Affiche les métadonnées complètes de chaque tuple
                   (id, hash, type, valeur)

────────────────────────────────────────────────────────────
📌 EXEMPLES D’UTILISATION
────────────────────────────────────────────────────────────

1. Comparaison simple de 14 tuples avec la variante 1 (copie directe) :
    $ python tuples_advanced.py

2. Générer et comparer 14 tuples avec une copie par régénération (variante 2) :
    $ python tuples_advancedu.py -v 2

3. Générer et comparer 10 tuples avec une copie par régénération (variante 2) :
    $ python tuples_advancedu.py -n 10 -v 2

4. Tester les 5 premiers tuples avec la copie statique (variante 3) + affichage complet :
    $ python tuples_advancedu.py -n 5 -v 3 --verbose

────────────────────────────────────────────────────────────
Auteur : ali.zainoul.az@gmail.com
Date : 2025-06-18
"""


import argparse
from typing import Generator

# === ANSI escape sequences for colorized output ===
ANSI_COLORS = {
    'green': '\033[92m',
    'red': '\033[91m',
    'reset': '\033[0m'
}

def colorize_bool(value: bool) -> str:
    """
    Return a string representation of a boolean value,
    colored green for True and red for False.
    """
    color = ANSI_COLORS['green'] if value else ANSI_COLORS['red']
    return f"{color}{value}{ANSI_COLORS['reset']}"

def generate_tuples(n: int) -> Generator[tuple, None, None]:
    """
    Generate n tuples of increasing size filled with integers (1 to i).
    """
    for i in range(1, n + 1):
        yield tuple(range(1, i + 1))

def print_infos(name: str, t: tuple) -> None:
    """
    Print detailed information about a tuple: name, id, hash, value and type.
    """
    print(f"{name}:")
    print(f"  id     : {id(t)}")
    print(f"  hash   : {hash(t)}")
    print(f"  value  : {t}")
    print(f"  type   : {type(t)}\n")

def compare_and_display(name1: str, t1: tuple, name2: str, t2: tuple, verbose: bool) -> None:
    """
    Compare two tuples and print identity and equality checks, optionally with full details.
    """
    if verbose:
        print_infos(name1, t1)
        print_infos(name2, t2)
    print(f"{name1} == {name2} → {colorize_bool(t1 == t2)}")
    print(f"{name1} is {name2} → {colorize_bool(t1 is t2)}")
    print("-" * 60)

def get_copied_list(version: int, original: list[tuple], n: int) -> list[tuple]:
    """
    Return a list of copied tuples based on the selected variant.
    """
    match version:
        case 1:
            return [tuple(t) for t in original]
        case 2:
            return [tuple(t) for t in generate_tuples(n)]
        case 3:
            return [
                (1,), (1, 2), (1, 2, 3), (1, 2, 3, 4), (1, 2, 3, 4, 5),
                (1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7, 8),
                (1, 2, 3, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
                (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
            ][:n]
        case _:
            raise ValueError("Invalid variant: choose 1, 2 or 3.")

def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Compare original tuples to their copies with identity and equality checks."
    )
    parser.add_argument(
        "-n", "--number", type=int, default=14,
        help="Number of tuples to generate (default: 14)"
    )
    parser.add_argument(
        "-v", "--variant", type=int, choices=[1, 2, 3], default=1,
        help="Copy variant: 1 (copy original), 2 (generate again), 3 (static definition)"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Display full tuple information (id, hash, type, value)"
    )
    return parser.parse_args()

def main():
    """
    Main execution: parse arguments, generate and compare tuples.
    """
    args = parse_args()

    list_of_tuples = list(generate_tuples(args.number))
    copied_list_of_tuples = get_copied_list(args.variant, list_of_tuples, args.number)

    print(f"\n=== Comparing {args.number} tuples using variant {args.variant} ===\n")

    for i, (t_orig, t_copy) in enumerate(zip(list_of_tuples, copied_list_of_tuples), start=1):
        name_orig = f"t{i}"
        name_copy = f"copy_t{i}"
        compare_and_display(name_orig, t_orig, name_copy, t_copy, verbose=args.verbose)

if __name__ == "__main__":
    main()




"""
🧪 Résultats observés
✅ Variante 1 : copied_list_of_tuples = [tuple(t) for t in list_of_tuples]
Résultat : == → True et is → True pour tous les tuples

✅ Interprétation :
Bien que tuple(t) semble créer une nouvelle instance, ici t est déjà un tuple.

Python détecte que l’objet est immutable et déjà un tuple, donc il renvoie directement l’objet original.

Cela explique pourquoi is renvoie True : pas de nouvelle instance créée.

📌 Optimisation Python : ce comportement évite des allocations mémoire inutiles sur des objets immuables.

🔁 Variante 2 : copied_list_of_tuples = [tuple(t) for t in generate_tuples(N)]
Résultat : == → True et is → False

🔁 Interprétation :
generate_tuples(n) produit de nouveaux objets à chaque exécution.

Bien que les tuples soient égaux en contenu (==), chaque tuple est distinct en mémoire (is → False).

Cela montre que l’identité d’un objet est différente de l’égalité de valeur.

📌 Bon usage pour tester des copies profondes ou pour éviter les effets de bord liés au partage d’objets.

🧱 Variante 3 : liste statique définie à la main
Résultat : == → True et is → False

🧱 Interprétation :
Ici, tu définis manuellement une nouvelle séquence de tuples.

Bien que le contenu soit identique à list_of_tuples, les objets sont recréés.

Donc : égalité de valeur, mais identité différente.

📌 Cela reflète le comportement par défaut de Python : chaque affectation explicite d’un tuple (même à contenu égal) produit un objet différent, sauf interning ou cache implicite (voir plus bas).

🔬 Analyse technique : Python et l’immutabilité
Comparaison	== (égalité de contenu)	is (identité mémoire)
Variante 1	✅	✅
Variante 2	✅	❌
Variante 3	✅	❌

🧠 Pourquoi cette différence ?
Les tuples sont immuables : leur contenu ne peut pas être modifié après création.

Python peut optimiser leur gestion via du caching, du memoization, ou de l’interning.

L’appel tuple(existing_tuple) ne crée pas de nouvelle instance si existing_tuple est déjà un tuple.

📌 À retenir
✅ == teste la valeur.

✅ is teste l’adresse mémoire (identité).

✅ tuple(t) n’a aucun effet si t est déjà un tuple.

✅ Générer des tuples identiques ne garantit pas qu’ils partagent le même emplacement mémoire.

⚠️ Ne pas confondre égalité logique et identité physique : crucial pour la gestion mémoire, les performances et les effets de bord en Python.
"""