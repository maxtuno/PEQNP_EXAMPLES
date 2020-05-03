import numpy as np
import peqnp as pn

b = 4
n = 3

A = np.random.randint(0, 2 ** b, size=n)
print(A)

pn.engine(b)

ids, xs = pn.permutations(A, n)

while pn.satisfy():
    print(ids, xs)
