from numpy.polynomial import Polynomial as P
from pylab import *

x = [0., 0.4, 0.8, 1.2, 1.6, 2.0]
y = [0.21, 1.25, 2.31, 2.7, 2.65, 3.2]

reg_pravac = P.fit(x, y, 1)
print('Koeficijenti regresijskog pravca su:', reg_pravac.coef)
print('Regresijski polinom stupnja 1 je:', reg_pravac)

reg_parabola = P.fit(x, y, 2)
print('Koeficijenti regresijske parabole su:', reg_parabola.coef)
print('Regresijski polinom stupnja 2 je:', reg_parabola)

xtocke = linspace(min(x)-0.5, max(x)+0.5, 100)

reg_pravac_y = reg_pravac(xtocke)
reg_parabola_y = reg_parabola(xtocke)
rust
print('reg_pravac(1.4)=', reg_pravac(1.4))
print('reg_parabola(1.4)=', reg_parabola(1.4))


plot(x, y, 'o', label='ulazni podaci')
plot(xtocke, reg_pravac_y, 'g-', label='linearna regresija')
plot(xtocke, reg_parabola_y, 'r-', label='kvadratna regresija')
plt.legend(loc='best')
show()
