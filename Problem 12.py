# Project Euler - Problem 12


def ndivisores(n):
    divisors = []
    for k in range(1, n + 1):
        if n % k == 0:
            divisors.append(k)
    return len(divisors)


for i in range(1, 100000000):
    numero = int(i * (i + 1) / 2)
    if ndivisores(numero) > 500:
        print(numero)
        break
