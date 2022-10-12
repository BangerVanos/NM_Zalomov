import math
import copy


def seidel(a: list, b: list, e: float):
    n = len(b)
    x = copy.deepcopy(b)

    coverge = False
    iters = 0
    while not coverge:
        x_new = copy.deepcopy(x)
        iters += 1
        for i in range(n):
            s1 = sum(a[i][j] * x_new[j] for j in range(i))
            s2 = sum(a[i][j] * x[j] for j in range(i+1, n))
            x_new[i] = (b[i] - s1 - s2)/a[i][i]

        coverge = math.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= e
        x = x_new

    return iters, x
