x = input_points()
n = len(x)

def newton_error(z):
    M = e**z
    omega = 1.0
    for i in range(0, n):
        omega *= z - x[i]
    return abs(omega) / math.factorial(n) * M

print("Pogreška u x=2.1:", newton_error(2.1))
