from typing import Iterator


# === Exercise 4 ===
def generate_powers(base: int, limit: int) -> Iterator[int]:
    """Yield successive powers of `base` less than `limit`."""
    power = 1
    while power < limit:
        yield power
        power *= base
    else:
        raise StopIteration("Limit exceeded")


# print("-"*32 + " [EX4] generate_powers " + "-"*32+ '\n')
# print("[EX4] generate_powers:", list(generate_powers(base=2, limit=50)))


gen : Iterator[int] = generate_powers(base=2, limit=50)
print(next(gen)) # Output : 2 := 2^1
print(next(gen)) # Output : 4 := 2^2
print(next(gen)) # Output : 8 := 2^3
print(next(gen)) # Output : 16 := 2^4
print(next(gen)) # Output : 32 := 2^5
# Error : 
print(next(gen)) # Output : 64 := 2^4
# The line above generates the error, 64 > LIMIT = 50 //

# THE GENERATOR HAS BEEN CONSUMED


gen_1 : Iterator[int] = generate_powers(base=2, limit=50)

for element in gen_1:
    print(element)