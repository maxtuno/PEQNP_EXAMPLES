import peqnp as pn

b = 4
n = 3

pn.engine(b)

xs = pn.vector(size=n)

while pn.satisfy():
    print(xs)
