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


def generate_data(bits, size):
    data = [random.randint(1, 2 ** bits) for _ in range(size)]
    print(data)
    print()
    return data


if __name__ == '__main__':

    bits, size = 5, 20

    data = generate_data(bits, size)

    pn.engine(sum(data).bit_length())

    T, sub, com = pn.subsets(data, complement=True)

    assert sum(sub) == sum(com)

    while pn.satisfy():
        print()
        sub_ = [data[i] for i in range(size) if T.binary[i]]
        com_ = [data[i] for i in range(size) if not T.binary[i]]
        print(sum(sub_), sub_)
        print(sum(com_), com_)
