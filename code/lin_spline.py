import numpy as np

x = np.array([0, 1, 2, 3 ,4])
y = np.array([0, 0, 1, 1, 0])

xr = np.linspace(-1, 5, num=1000)
yr = np.interp(xr, x, y)

# crtanje interpoliranih vrijednosti
import matplotlib.pyplot as plt
plt.plot(xr, yr, '-', label='interpolacija')
plt.plot(x, y, 'o', label='ulazni podaci')
plt.legend(loc='best')
plt.show()
