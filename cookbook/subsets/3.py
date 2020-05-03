import peqnp as pn

b = 4
n = 3

pn.engine(b)

xs = pn.vector(size=n)

pn.all_different(xs)
pn.apply_single(xs, lambda x: x < n)

while pn.satisfy():
    print(xs)
