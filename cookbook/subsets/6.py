import peqnp as pn

pn.engine(10)
xs = pn.vector(size=3)
pn.all_out(xs, [1, 2, 3])
pn.all_different(xs)
pn.apply_single(xs, lambda x: x < 10)
while pn.satisfy():
    print(xs)
