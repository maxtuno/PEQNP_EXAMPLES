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

import random

import peqnp as pn


# Permutation Reconstruction fromDifferences
# from https://arxiv.org/pdf/1410.6396.pdf
def gen_instance(n):
    y = list(range(1, n + 1))
    random.shuffle(y)
    # Read paper exist two solutions.
    print('hidden:')
    print(y)
    print(80 * '-')
    return [abs(y[i + 1] - y[i]) for i in range(n - 1)]


if __name__ == '__main__':

    n = 50

    diffs = gen_instance(n)

    pn.engine(n.bit_length() + 1)

    x = pn.vector(size=n)

    pn.all_different(x)
    pn.apply_single(x, lambda a: 1 <= a <= n)

    for i in range(n - 1):
        assert pn.index(i, diffs) == pn.one_of([x[i + 1] - x[i], x[i] - x[i + 1]])

    if pn.satisfy(turbo=True):
        xx = [abs(x[i + 1] - x[i]) for i in range(n - 1)]
        if xx == diffs:
            print(x)
            print(xx)
        else:
            raise Exception('Error!')
    else:
        raise Exception('Error!')
