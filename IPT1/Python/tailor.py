import math


DELTA = 1E-8
PI = math.pi


def tailor_term(n: int, x: float) -> float:
    return (-1)**n*((x**(2*n+1))/math.factorial(2*n+1))


def sin_tailor(term_num: int, x: float):
    x -= 2*PI*(x // (2*PI))
    tailor_list = [tailor_term(i, x) for i in range(term_num)]
    # print("Tailor terms:", ', '.join(list(map(str, tailor_list))))
    sin = sum(tailor_list)
    return sin


def scores() -> str:
    return "-"*200


print(scores())
print("Computed sin\t\tTailor sin")
for x in range(10000):
    print(scores())
    print(f"Computing sin({x})")
    n = 1
    while abs(math.sin(x) - sin_tailor(n, x)) >= DELTA:
        print(f"{n}. Computed sin({x}): {math.sin(x)}\t\tTailor sin({x}): {sin_tailor(n, x)}\t\t"
              f"E={abs((math.sin(x)-sin_tailor(n, x))/sin_tailor(n, x))}"
              f"\t\tdelta={abs(math.sin(x) - sin_tailor(n, x))}")
        n += 1
    try:
        print(f"{n}. Computed sin({x}): {math.sin(x)}\t\tTailor sin({x}): {sin_tailor(n, x)}\t\t"
              f"E={abs((math.sin(x) - sin_tailor(n, x)) / sin_tailor(n, x))}"
              f"\t\tdelta={abs(math.sin(x) - sin_tailor(n, x))}")
    except ZeroDivisionError:
        print(f"{n}. Computed sin({x}): {math.sin(x)}\t\tTailor sin({x}): {sin_tailor(n, x)}\t\t"
              f"E=0\t\tdelta={abs(math.sin(x) - sin_tailor(n, x))}")
    print(f"{n} tailor terms needed to count sin with {DELTA} accuracy")
