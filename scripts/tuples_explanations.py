"""
tuples_explanations.py

Ce script illustre comment Python gère les constantes et le bytecode
lors de la création et du retour d’un tuple dans une fonction simple.

Fonctionnalités :
- Définit une fonction `generate_tuple()` qui retourne un tuple `(1, 2, 3)`.
- Affiche les constantes (`co_consts`) utilisées dans cette fonction.
- Affiche le bytecode généré par Python à l’aide du module `dis`.

Objectif pédagogique :
Ce script est utile pour explorer la compilation en bytecode dans CPython,
et comprendre comment Python stocke les objets constants tels que les tuples.

Exemple de sortie :
    (None, (1, 2, 3))
      3           0 RESUME                   0
      4           2 LOAD_CONST               1 ((1, 2, 3))
                  4 STORE_FAST               0 (t)
      5           6 LOAD_FAST                0 (t)
                  8 RETURN_VALUE

Compatibilité :
- Python 3.11 ou supérieur (instruction `RESUME` spécifique à ces versions)

Auteur : ali.zainoul.az@gmail.com
"""


import dis

def generate_tuple() -> tuple:
    """
    Crée et retourne un tuple contenant trois entiers.
    
    Cette fonction sert d'exemple pour analyser le bytecode Python associé
    à la création et au retour d'un tuple simple. Elle permet d'observer 
    comment Python compile et exécute une fonction simple.

    Returns:
        tuple: Un tuple contenant les valeurs (1, 2, 3).
    """
    t = (1, 2, 3)
    return t

# Affiche les constantes utilisées dans le bytecode de la fonction
print(generate_tuple.__code__.co_consts)

# Désassemble le bytecode de la fonction pour voir les instructions internes
dis.dis(generate_tuple)

# → Résultat : (None, (1, 2, 3))
# Cela signifie que la fonction utilise deux constantes :
# - `None` (valeur de retour par défaut si aucun `return`)
# - le tuple `(1, 2, 3)` utilisé dans la fonction

"""
(base) 💻 ~/_COURSE_PYTHON_IB/scripts % python tuples_explanations.py
(None, (1, 2, 3))
  3           0 RESUME                   0

  4           2 LOAD_CONST               1 ((1, 2, 3))
              4 STORE_FAST               0 (t)

  5           6 LOAD_FAST                0 (t)
              8 RETURN_VALUE
"""


"""

Décryptage ligne par ligne :

Ligne	Instruction	        Description
0       RESUME      0	    Point de reprise, utilisé dans la gestion des frames (Python 3.11+).	
2       LOAD_CONST  1	    Charge la constante (1, 2, 3) dans la pile.	
4       STORE_FAST  0 (t)	Stocke cette valeur dans la variable locale t.	
6       LOAD_FAST   0 (t)	Recharge t dans la pile (préparation pour le retour).	
8       RETURN_VALUE	    Retourne la valeur au sommet de la pile, ici (1, 2, 3).	

💡 Remarques pédagogiques :

- Le __code__.co_consts révèle toutes les constantes utilisées dans la fonction compilée.
- Le bytecode est une représentation intermédiaire de haut niveau compilée par CPython.

Ce genre d’analyse est utile pour :

- Optimisation de performance
- Compréhension du fonctionnement interne de Python
- Debugging avancé

L’instruction RESUME est spécifique à Python 3.11+. 
Elle est utilisée dans la nouvelle implémentation de l’évaluateur d’instructions.
"""