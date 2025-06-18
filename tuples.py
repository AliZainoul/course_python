t1 : tuple = (1, 1, 1, 2, 33, 3, 4, 1, 2)
t2 : tuple = (1, 1, 1, 2, 33, 3, 4, 1, 2)

print(f"My tuple t1 with id = {id(t1)}, hash = {hash(t1)}, value = {t1} and type = {type(t1)} \n")
print(f"My tuple t2 with id = {id(t2)}, hash = {hash(t2)}, value = {t2} and type = {type(t2)} \n")

print(f"t1 == t2: {t1 == t2}")
print(f"t1 is t2: {t1 is t2}")