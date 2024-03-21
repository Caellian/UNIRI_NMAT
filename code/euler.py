def euler(x, y, h, f, n):
    xs = [x]
    ys = [y]
    for i in range(n):
        slope = f(xs[i], ys[i])
        xs.append(xs[i] + h)
        ys.append(ys[i] + h * slope)
    return xs, ys
