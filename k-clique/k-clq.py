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

import sys

import peqnp as pn


def load_file(file_name):
    mat = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            if line.startswith('p edge '):
                n_ = int(line[len('p edge '):].split(' ')[0])
            elif line.startswith('e '):
                x, y = map(int, line[len('e '):].split(' '))
                mat.append((x, y))
    return n_, mat


if __name__ == '__main__':

    n, graph = load_file(sys.argv[1])
    k = int(sys.argv[2])

    print('Wait for it...')

    pn.engine(bits=k.bit_length())
    pn.version()

    bits = pn.tensor(dimensions=(n, ))
    assert sum(bits[[i]](0, 1) for i in range(n)) == k
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (i, j) not in graph and (j, i) not in graph:
                assert bits[[i]](0, 1) & bits[[j]](0, 1) == 0

    if pn.satisfy(turbo=True, log=True):
        print(k)
        print(' '.join([str(i) for i in range(n) if bits.binary[i]]))
    else:
        print('Infeasible ...')

