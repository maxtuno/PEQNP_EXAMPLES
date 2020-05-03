import peqnp as pn

pn.engine(10)
xs = pn.vector(size=4)
pn.all_in(xs, [1, 2, 3])
while pn.satisfy():
    print(xs)
