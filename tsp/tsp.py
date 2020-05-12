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
    print(tour)
    x, y = zip(*[data[tour[i]] for i in range(n)] + [data[tour[0]]])
    plt.title(title + ' : {}'.format(oracle(tour)))
    plt.plot(x, y, 'r-')
    plt.plot(x, y, 'ko')
    plt.savefig('tsp_{}.png'.format(title.lower().replace(' ', '_')))
    plt.close()


def oracle(seq):
    return sum(np.linalg.norm(data[seq[i - 1]] - data[seq[i]]) for i in range(n))


if __name__ == '__main__':
    n = 20
    data = np.random.randint(0, 100, size=(n, 2))
    matrix = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = int(np.linalg.norm(data[i] - data[j]))

    seq = pn.hess_sequence(n, oracle=oracle)
    plot(seq, 'Hess Formulation')
    optimal = int(oracle(seq)) + 1
    b = optimal.bit_length()
    while True:
        pn.engine(bits=b)

        X = pn.tensor(dimensions=(n, n))
        y = pn.vector(size=n)

        for i in range(n):
            assert y[i] < n
            assert X[[i, i]](0, 1) == 0
            assert sum(X[[i, j]](0, 1) for j in range(n)) == 1
            assert sum(X[[j, i]](0, 1) for j in range(n)) == 1
            for j in range(1, n):
                if i >= 1 and i != j:
                    assert y[i] + n * X[[i, j]](0, 1) < n + y[j]

        assert sum(matrix[i][j] * X[[i, j]](0, 1) for i in range(n) for j in range(n)) < optimal

        if pn.satisfy(turbo=True):
            optimal = int(sum(matrix[i][j] for i in range(n) for j in range(n) if X.binary[i][j]))
            X = np.vectorize(int)(X.binary)
            print(optimal)
            print(X)
            path = {}
            for i in range(n):
                for j in range(n):
                    if X[i][j]:
                        path[j] = i
            tour = [0, path[0]]
            while len(tour) < n:
                tour.append(path[tour[-1]])
            plot(tour, 'Integer Formulation')
        else:
            break
