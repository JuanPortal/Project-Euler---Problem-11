# Project Euler - Problem 16


def sumaDigitos(n):
    suma = 0
    for i in str(n):
        suma += int(i)
    return suma


'''j = 1
while j < 1001:
    print(f"{2 ** j} --> {sumaDigitos(2 ** j)}")
    j += 1'''

print(sumaDigitos(2 ** 1000))
