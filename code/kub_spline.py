import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 0.5, 0.333, 0.25, 0.2])

xr = np.linspace(0, 6, num=1000)
spline = CubicSpline(x, y)

# crtanje interpoliranih vrijednosti
import matplotlib.pyplot as plt
plt.plot(xr, spline(xr), '-', label='interpolacija')
plt.plot(x, y, 'o', label='ulazni podaci')
plt.legend(loc='best')
plt.show()
