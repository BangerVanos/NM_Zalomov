import math


E = 10E-15


def tailor_term(n: int, x: float) -> float:
    return (-1)**n*((x**(2*n+1))/math.factorial(2*n+1))


def sin_tailor(term_num: int, x: float):
    tailor_list = [tailor_term(i, x) for i in range(term_num)]
    print(', '.join(list(map(str, tailor_list))))
    sin = sum(tailor_list)
    return sin


print("-"*(len("Computed sin\tTailor sin")+3))
print("Computed sin\tTailor sin")
print("-"*(len("Computed sin\tTailor sin")+3))
