from numpy import *
from scipy import interpolate
import pylab

def f(x):
    return x*cos(x)

xcvorovi=genfromtxt('tocke.txt', delimiter=',')
print(xcvorovi)
ycvorovi=f(xcvorovi)
print(ycvorovi)

lspline=interpolate.interp1d(xcvorovi, ycvorovi, kind='slinear')
kspline=interpolate.interp1d(xcvorovi, ycvorovi, kind='cubic')

print('Aps greska za lspline u x=1 je: ', abs(f(1)-lspline(1)))
print('Aps greska za kspline u x=1 je: ', abs(f(1)-kspline(1)))

xtocke=linspace(min(xcvorovi), max(xcvorovi), 100)
ylspline=lspline(xtocke)
ykspline=kspline(xtocke)
yfunkcija=f(xtocke)

pl.figure()
pl.plot(xcvorovi, ycvorovi, 'o', xtocke, ylspline, '-r',
        xtocke, ykspline, '-g', xtocke, yfunkcija, '--')
pl.legend(['cvorovi', 'lspline', 'kspline', 'funckija'])
pl.grid()
pl.show()
