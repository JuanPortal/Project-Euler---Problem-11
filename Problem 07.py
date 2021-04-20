# Project Euler - Problem 7


def Primo(n):
    if n <= 1:
        return False

    divisores = []
    for p in range(2, n):
        residuo = n % p
        divisores.append(residuo)

    if 0 in divisores:
        return False
    else:
        return True


primes = []
for i in range(1, 2147483648):
    if Primo(i):
        primes.append(i)

print(primes[10000])
