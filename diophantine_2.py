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

# https://mathoverflow.net/questions/201980/diophantine-equations-and-the-numbers-4-7-8
# http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.36.8786

if __name__ == '__main__':

    for k in range(100):

        pn.engine(16)

        n = pn.integer()
        x = pn.integer()
        y = pn.integer()
        z = pn.integer()

        assert x ** n + y ** n + z ** n == k * x * y * z

        assert n > 1 < x <= y <= z

        if pn.satisfy(turbo=True):
            print('{2} ** {1} + {3} ** {1} + {4} ** {1} == {0} * {2} * {3} * {4}'.format(k, n, x, y, z))
