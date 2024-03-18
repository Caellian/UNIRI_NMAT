import numpy as np

x = np.array([-3,4,3])
y = np.array([-4,2,0])

def lagrange_coef(x, val):
    """Računa lagrangeove koeficijente za dane vrijednosti"""
    n = len(x)
    a = []
    for i in range(n):
        I = 1
        for j in range(n):
            if j == i:
                continue
            I *= (val-x[j])/(x[i]-x[j])
        a.append(I)
    return a

def lagrange_formula(x, y):
    """Vraća formulu lagrangeove interpolacije za dane vrijednosti"""
    # numpy dozvoljava umnožak polja po komponentama:
    return lambda val: sum(y * lagrange_coef(x, val))
    # (sporija) formula bez numpyja:
    return lambda val: sum([y[i]*a for i, a in enumerate(lagrange_coef(x, val))])

L = lagrange_formula(x, y)
print("L(3.5) =", L(3.5)) # ISPIS: L(3.5) = 0.9524
