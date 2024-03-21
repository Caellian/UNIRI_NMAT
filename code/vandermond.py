import numpy as np
from numpy.polynomial import polynomial as poly
import pylab

A = np.array([
    [1, 0,  0],
    [1, 2,  4],
    [1, 4, 16]
])
B = np.array([3, 4, 2])

# Rješenje sustava A * X = B
X = np.linalg.solve(A, B)
print("Rješenje sustava:", X)

print('p(0) =', poly.polyval(0., X))
print('p(2) =', poly.polyval(2., X))
print('p(4) =', poly.polyval(4., X))

x = np.linspace(-1, 5, 100)
y = poly.polyval(x, X)

pylab.plot(x, y)
pylab.show()
