def rk4(x, y, h, f, n):
    xs = [x]
    ys = [y]
    for i in range(n):
        k1 = f(xs[i], y[i])
        k2 = f(xs[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(xs[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(xs[i], y[i] + h * k3)
        xs.append(xs[i] + h)
        y = ys[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        ys.append(y)
    return xs, ys
