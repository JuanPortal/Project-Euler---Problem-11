# Project Euler - Problem 15


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


result = factorial(40) / (factorial(20) * factorial(20))

print(int(result))
