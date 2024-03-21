def sekanta(a, b, eps, f, n):
    i = 0
    while abs(b - a) > eps:
        i += 1
        x = b - (f(b) * f(b-a))/(f(b) - f(a))
        
        if f(x) == 0:
            print(f"Rješenje nađeno u {i} iteracija.")
            return x
        
        a = b
        b = x
        
        if i >= n:
            print(f"Rješenje nije nađeno u {n} iteracija.")
            return None
    return b