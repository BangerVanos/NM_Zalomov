import seidel_func

a = [[6.2, 2.3, 0.2], [4.1, 5.7, 1.2], [0.3, 0.6, -1.6]]
b = [0.4, 5.8, -0.9]
e = 1E-6

print("Amount of iterations: {}, x = {}".format(*seidel_func.seidel(a, b, e)))
