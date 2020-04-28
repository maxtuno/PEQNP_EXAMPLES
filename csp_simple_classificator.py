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
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

X, y = make_classification(n_features=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1, n_samples=1000)

X = MinMaxScaler().fit_transform(X)
X *= (max(X.flatten()) - min(X.flatten()))
X_train, X_test, y_train, y_test = train_test_split(X, y)

cm = plt.cm.RdBu
cm_bright = ListedColormap(['#FF0000', '#0000FF'])

plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, edgecolors='k')
plt.savefig('raw.png')
plt.close()

pn.engine(bits=int(sum(X.flatten())).bit_length() + 1)

T = pn.vector(size=X_train[0].size)

a = pn.integer()
b = pn.integer()
c = pn.integer()
d = pn.integer()
o = pn.integer()

assert c + o < b

for x, y in zip(X_train, y_train):
    if y == 0:
        assert a <= np.matmul(T, x) <= b
    elif y == 1:
        assert c <= np.matmul(T, x) <= d

top = 0
while pn.satisfy():
    T_ = np.vectorize(int)(T)
    a_ = int(a)
    b_ = int(b)
    c_ = int(c)
    d_ = int(d)
    o_ = int(o)

    y_pred = np.zeros(shape=(y_test.size,), dtype=int)
    for i, x in enumerate(X_test):
        if a_ <= np.matmul(T_, x) <= b_:
            y_pred[i] = 0
        elif c_ <= np.matmul(T_, x) <= d_:
            y_pred[i] = 1

    score = accuracy_score(y_test, y_pred)

    if score > top:
        top = score

        print('T: {}'.format(T_.tolist()))
        print('a: {}'.format(a_))
        print('b: {}'.format(b_))
        print('c: {}'.format(c_))
        print('d: {}'.format(d_))
        print('o: {}'.format(o_))

        print('Accuracy Score : {}'.format(score))

        plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap=cm_bright, edgecolors='k')
        plt.savefig('cls.png')
        plt.close()

        if score == 1:
            break
