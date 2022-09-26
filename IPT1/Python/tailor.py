import math


E = 10E-10


def tailor_term(n: int, x: float) -> float:
    return (-1)**n*((x**(2*n+1))/math.factorial(2*n+1))


def sin_tailor(term_num: int, x: float):
    tailor_list = [tailor_term(i, x) for i in range(term_num)]
    print("Tailor terms", ', '.join(list(map(str, tailor_list))))
    sin = sum(tailor_list)
    return sin


def scores() -> str:
    return "-"*(len("Computed sin\tTailor sin")+3)


print(scores())
print("Computed sin\tTailor sin")
for x in range(26):
    print(scores())
    print(f"Counting sin({x})")
    n = 1
    while abs(math.sin(x) - sin_tailor(n, x)) >= E:
        print(f"Computed sin({x}): {math.sin(x)}\tTailor sin({x}): {sin_tailor(n, x)}")
        n += 1
    print(f"{n} tailor terms needed to count sin with {E} accuracy")
