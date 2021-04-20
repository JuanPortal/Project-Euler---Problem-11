# Project Euler - Problem 15


def factorial(n):
    producto = 1
    for i in range(1, n + 1):
        producto *= i
    return producto


resultado = factorial(40)/(factorial(20)*factorial(20))

print(int(resultado))
