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
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__ == '__main__':

    n, epsilon = 100, 0.9

    iris = datasets.load_iris()

    X_train, X_test, Y_train, Y_test = train_test_split((iris.data[:n] * 10), iris.target[:n], shuffle=True)

    bt = 0
    while True:

        bt += 1

        print('bits : {}'.format(bt))

        pn.engine(bits=bt)

        T = pn.vector(size=X_train[0].size)

        a = pn.integer()
        b = pn.integer()

        for x, y in zip(X_train, Y_train):
            if y == 0:
                assert np.matmul(T, x) <= a
            elif y == 1:
                assert a < np.matmul(T, x) <= b
            elif y == 2:
                assert b < np.matmul(T, x)

        if pn.satisfy():
            T = np.vectorize(int)(T)
            a = int(a)
            b = int(b)

            Y_pred = np.zeros(shape=(Y_test.size,), dtype=int)
            for i, x in enumerate(X_test):
                if np.matmul(T, x) <= a:
                    Y_pred[i] = 0
                elif a < np.matmul(T, x) <= b:
                    Y_pred[i] = 1
                elif b < np.matmul(T, x):
                    Y_pred[i] = 2

            print('T: {}'.format(T.tolist()))
            print('a: {}'.format(a))
            print('b: {}'.format(b))

            score = accuracy_score(Y_test, Y_pred)

            print('Accuracy Score : {}'.format(score))

            if score >= epsilon:
                break
