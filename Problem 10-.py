# Project Euler - Problem 10


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


suma = 0
for i in range(2000000):
    if Primo(i):
        suma += i

print(suma)
