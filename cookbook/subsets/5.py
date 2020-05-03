import numpy as np
import peqnp as pn

b = 5
n = 5

A = np.random.randint(0, 2 ** b, size=n)
print(A)

pn.engine(b)

ids, xs = pn.permutations(A, n)

assert ids[len(ids) // 2] == len(ids) // 2

while pn.satisfy():
    print(ids, xs)
