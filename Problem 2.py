# Project Euler - Problem 2


def fibonacci(n):
    sucesion = [1, 2]
    i = 0

    while i < n:
        i = sucesion[0] + sucesion[1]
        sucesion[0] = sucesion[1]
        sucesion[1] = i
        sucesion.append(i)

    sucesion[0] = 1
    sucesion[1] = 2

    if sucesion[len(sucesion) - 1] > n:
        sucesion.pop()

    return sucesion


print(fibonacci(4000000))

suma = 0
for j in fibonacci(4000000):
    if j % 2 == 0:
        suma += j

print(suma)
