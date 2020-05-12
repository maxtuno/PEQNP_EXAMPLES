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

import numpy as np
import peqnp as pn
import matplotlib.pyplot as plt


def plot(tour, title):
    x, y = zip(*[data[tour[i]] for i in range(n)] + [data[tour[0]]])
    plt.title(title + ' : {}'.format(oracle(tour)))
    plt.plot(x, y, 'r-')
    plt.plot(x, y, 'ko')
    plt.savefig('tsp_{}.png'.format(title.lower().replace(' ', '_')))
    plt.close()


def oracle(seq):
    return sum(D[seq[i - 1]][seq[i]] for i in range(n))


if __name__ == '__main__':

    n = 9
    data = np.random.logistic(size=(n, 2))
    D = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            D[i][j] = np.linalg.norm(data[i] - data[j])

    seq = pn.hess_sequence(n, oracle=oracle, fast=False)
    print(oracle(seq))
    plot(seq, 'HESS')

    pn.engine()

    M = np.asarray(pn.matrix(dimensions=(n, n), is_mip=True))
    u = pn.vector(size=n, is_mip=True)

    for k in range(n):
        assert M[k][k] == 0

    assert sum(M.flatten()) == n

    for i in range(n):
        for j in range(n):
            assert M[i][j] <= 1

    for a, b in zip(M, M.T):
        assert sum(a) == 1
        assert sum(b) == 1

    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                assert u[i] - u[j] + (n - 1) * M[i][j] <= n - 2

    optimal = pn.minimize(sum(D[i][j] * M[i][j] for i in range(n) for j in range(n)), lp_path='data.lp')
    print(optimal)

    path = {}
    for i in range(n):
        for j in range(n):
            if M[i][j].value:
                path[j] = i

    tour = [0, path[0]]
    while len(tour) < n:
        tour.append(path[tour[-1]])
    plot(tour, 'MIP')

    print('ratio HESS / MIP = {}'.format(oracle(seq) / optimal))
