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
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(10, 10)) 

pn.engine(12)

x = pn.integer()
y = pn.integer()

assert f(x, y) == 0

xs, ys = [], []
while pn.satisfy():
    xs.append(x.value)
    ys.append(y.value)

x = np.linspace(-1, max(xs)) 
y = np.linspace(-1, max(ys)) 
  
[X, Y] = np.meshgrid(x, y) 

Z = f(X, Y)
  
plt.title('$(x^2 + y^2) \% (x + y)=0$')
ax.contour(X, Y, Z, alpha=0.7) 
ax.scatter(xs, ys, c='r')
ax.set_xlabel('x') 
ax.set_ylabel('y') 
  
plt.show() 
