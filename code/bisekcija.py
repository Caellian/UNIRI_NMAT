def bisekcija(f, a, b, eps):
    c = (a + b) / 2
    
    if abs(b - a) < eps:
        return c
    if f(a) * f(c) <= 0:
        return bisekcija(f, a, c, eps)
    else:
        return bisekcija(f, c, b, eps)
