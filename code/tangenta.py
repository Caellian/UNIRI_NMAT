
if f(x) * fdd(x) < 0:
    print("Newtonova metoda ne konvergira.")

def newton(x, eps, f, fd, n):
    for i in range(n):
        if abs(fd(x)) < eps:
            break
        
        dx = f(x) / fd(x)
        x = x - dx
        
        if abs(dx) < eps:
            print(f"Rješenje nađeno u {i} iteracija")
            return x
    
    print(f"Rješenje nije nađeno u {n} iteracija.")
    return None
