from numpy import *
from numpy.polynomial import polynomial as p
from numpy import linalg
import pylab

M1=array([[1,0,0], [1,2,4], [1,4,16]])
M2=array([3,4,2])

a=linalg.solve(M1, M2)
print(a)

print('p(0)=',p.polyval(0., a))
print('p(2)=',p.polyval(2., a))
print('p(4)=',p.polyval(4., a))

x=linspace(0-0.5, 5, 100)
y=p.polyval(x, a)
pylab.plot(x, y)
pylab.show()
