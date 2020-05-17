"""
Copyright (c) 2012-2020 PEQNP. all rights reserved. contact@peqnp.science

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import warnings

import numpy as np
import peqnp as pn
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

n, R_m, cls  = np.random.randint(50, 100), 2, np.random.randint(2, 10)

print(n, R_m, cls)

A = np.random.logistic(size=(n, R_m))
d = np.random.randint(25, 50, size=(n))
C = np.random.logistic(size=(cls, R_m))
D = np.zeros(shape=(n, cls))
for i in range(n):
    for j in range(cls):
        D[i][j] = np.linalg.norm(A[i] - C[j])

optimal = n // cls
while True:
  pn.engine()

  X = np.asarray(pn.vector(size=n, is_mip=True))
  Y = np.asarray(pn.matrix(dimensions=(n, cls), is_mip=True))

  pn.all_binaries(Y.flatten())

  for x, y in zip(X, Y):
      assert (y <= x).all()
      assert sum(y) == 1

  assert sum(X) == cls
  assert (Y.sum(axis=0) <= optimal).all()
  assert sum(Y.sum(axis=0)) == n

  result = pn.minimize(sum(D[i][j] * d[j] * Y[i][j] for i in range(n) for j in range(cls)))

  if result > 2 ** 32: # Infeasible
    optimal += 1
    continue

  Y = np.vectorize(int)(Y)
  for i, a in enumerate(C):
      plt.plot(a[0], a[1], 'ko', alpha=0.7)
      plt.scatter(a[0], a[1], c=[plt.cm.RdYlBu(i / cls)], s=250, alpha=0.7)

  for i, (a, b) in enumerate(zip(A, Y)):
      plt.scatter(a[0], a[1], c=[plt.cm.RdYlBu(b.tolist().index(1) / cls)], s=d[i], alpha=0.9)

  plt.show()

  optimal = max(Y.sum(axis=0))
  
  break

print(Y.sum(axis=0))
