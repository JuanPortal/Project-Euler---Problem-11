# Project Euler - Problem 6


def difference(n):
    return (n * (n + 1) / 2) ** 2 - n * (n + 1) * (2 * n + 1) / 6


print(int(difference(100)))
