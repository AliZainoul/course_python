s1 = """En Python, des différences subtiles mais fondamentales peuvent apparaître entre le comportement interactif de l’interpréteur (REPL) et l’exécution d’un scri\
pt source. Ces différences, souvent invisibles pour les débutants, sont cruciales à comprendre pour tout développeur expérimenté. Cet article examine ces comportements \
à travers le prisme de la fonction id() et des objets immuables comme les tuple, en mettant en lumière les mécanismes internes de CPython : l’interning, le constant fol\
ding, et la gestion des objets constants.En Python, des différences subtiles mais fondamentales peuvent apparaître entre le comportement interactif de l’interpréteur (REPL) et l’exécution d’un scri\
pt source. Ces différences, souvent invisibles pour les débutants, sont cruciales à comprendre pour tout développeur expérimenté. Cet article examine ces comportements \
à travers le prisme de la fonction id() et des objets immuables comme les tuple, en mettant en lumière les mécanismes internes de CPython : l’interning, le constant fol\
ding, et la gestion des objets constants."""

s2 = """En Python, des différences subtiles mais fondamentales peuvent apparaître entre le comportement interactif de l’interpréteur (REPL) et l’exécution d’un scri\
pt source. Ces différences, souvent invisibles pour les débutants, sont cruciales à comprendre pour tout développeur expérimenté. Cet article examine ces comportements \
à travers le prisme de la fonction id() et des objets immuables comme les tuple, en mettant en lumière les mécanismes internes de CPython : l’interning, le constant fol\
ding, et la gestion des objets constants.En Python, des différences subtiles mais fondamentales peuvent apparaître entre le comportement interactif de l’interpréteur (REPL) et l’exécution d’un scri\
pt source. Ces différences, souvent invisibles pour les débutants, sont cruciales à comprendre pour tout développeur expérimenté. Cet article examine ces comportements \
à travers le prisme de la fonction id() et des objets immuables comme les tuple, en mettant en lumière les mécanismes internes de CPython : l’interning, le constant fol\
ding, et la gestion des objets constants."""

print(f"s1 == s2 : {s1 == s2}")
print(f"s1 is s2 : {s1 is s2}")