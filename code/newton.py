import numpy as np

x = np.array([0, 0.25, 0.5, 0.75, 1])
y = np.array([0, 0.7071, 1, 0.7071, 0])

def newton_coef(x, y):
    """Računa newtonove koeficijente za dane vrijednosti"""
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])
    return a

def newton_formula(x, y):
    """Vraća formulu newtonove interpolacije za dane vrijednosti"""
    coef = newton_coef(x, y)
    
    def iprod(i, val):
        result = 1
        for i in range(i):
            result *= (val - x[i])
        return result
        
    return lambda val: sum([a * iprod(i, val) for i, a in enumerate(coef)])

# primjer ispisa polinoma 4. stupnja
a = newton_coef(x, y)
print(
    f"P4(x) = {a[0]} + {a[1]}(x-{x[0]})"
    f" + {a[2]}(x-{x[0]})(x-{x[1]})"
    f" + {a[3]}(x-{x[0]})(x-{x[1]})(x-{x[2]})"
    f" + {a[4]}(x-{x[0]})(x-{x[1]})(x-{x[2]})(x-{x[3]})"
)

P = newton_formula(x, y)
print('P4(1.5) =', P(1.5)) # ISPIS: P4(1.5) = -0.2544
