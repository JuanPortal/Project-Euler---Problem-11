# Project Euler - Problem 3


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


# num = 6.00851475143e+011

numero = 13195
# numero = 600851475143

for i in range(numero, 1, -1):
    if Primo(i) and numero % i == 0:
        print(i)
        break

# print(int(num))
