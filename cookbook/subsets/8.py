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

import functools
import operator
import peqnp as pn


def ands(x, pos):
    return functools.reduce(operator.iand, [x[i] for i in pos])


if __name__ == '__main__':

    n = 10

    pn.engine(10)

    xs = pn.vector(size=n)

    pn.all_different(xs)
    pn.apply_single(xs, lambda x: 0 < x <= n)
    sub = pn.subset(xs, k=3, empty=0)

    assert pn.one_of([ands(sub, pos) for x in xs for pos in [[0, 1, 2], [7, 8, 9]]]) != 0

    while pn.satisfy():
        print(xs)
