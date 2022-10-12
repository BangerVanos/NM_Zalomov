import seidel_func


n = 10
a = [[1 if i != j else 2*n for j in range(n)] for i in range(n)]
b = [int((2*n - 1)*i + n*(n + 1)/2 + 9*n - 3) for i in range(1, n+1)]
e = 1E-4

print("Amount of iterations: {}, x = {}".format(*seidel_func.seidel(a, b, e)))
