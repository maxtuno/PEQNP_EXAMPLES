import numpy as np
import peqnp as pn
import matplotlib.pyplot as plt

n, R_m, cls  = 200, 2, 8
A = np.random.randint(0, 100, size=(n, R_m))
d = np.random.randint(0, 100, size=(n))
C = np.random.randint(0, 100, size=(cls, R_m))
D = np.zeros(shape=(n, cls))
for i in range(n):
    for j in range(cls):
        D[i][j] = np.linalg.norm(A[i] - C[j])

pn.engine()

X = np.asarray(pn.vector(size=n, is_mip=True))
Y = np.asarray(pn.matrix(dimensions=(n, cls), is_mip=True))

pn.all_binaries(X.flatten())
pn.all_binaries(Y.flatten())

for x, y in zip(X, Y):
    assert (y <= x).all()
    assert sum(y) == 1

assert sum(X) == cls

pn.minimize(sum(D[i][j] * d[j] * Y[i][j] for i in range(n) for j in range(cls)))

Y = np.vectorize(int)(Y)
for i, a in enumerate(C):
    plt.plot(a[0], a[1], 'ro', alpha=0.7)
    plt.scatter(a[0], a[1], c=[plt.cm.RdYlBu(i / cls)], s=250, alpha=0.7)

for i, (a, b) in enumerate(zip(A, Y)):
    plt.scatter(a[0], a[1], c=[plt.cm.RdYlBu(b.tolist().index(1) / cls)], s=d[i], alpha=0.9)

plt.figure(figsize=(20, 20))
plt.show()