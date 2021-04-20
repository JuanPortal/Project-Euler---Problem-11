# Project Euler - Problem 6


def diferencia(n):
    result = (n * (n + 1) / 2) ** 2 - n * (n + 1) * (2 * n + 1) / 6
    return result


print(int(diferencia(100)))
