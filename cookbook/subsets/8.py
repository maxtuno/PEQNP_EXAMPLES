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

import peqnp as pn
import numpy as np


def chunks(lst1, lst2, n):
    for i in range(0, len(lst1), n):
        yield (lst1[i:i + n], lst2[i:i + n], list(range(i + 1, i + n + 1)))


if __name__ == '__main__':

    n = 9
    m = 3

    pn.engine(10)

    xs = np.asarray(pn.vector(size=n))

    pn.apply_single(xs.flatten(), lambda x: 0 < x <= n)
    pn.all_different(xs.flatten())

    z, x = pn.subsets(xs.flatten(), k=m)

    y = [pn.switch(z, i, neg=True) for i in range(n)]

    for u, v, l in chunks(y, x, m):
        assert sum(u) == pn.one_of([0, m])
        assert sum(v) == pn.one_of([0, sum(l)])
        assert np.prod(v) == pn.one_of([0, np.prod(l)])

    while pn.satisfy():
        print(np.vectorize(int)(z.binary))
        print(np.vectorize(int)(xs))
        print()
