# Project Euler - Problem 5

for i in range(1, 232792561):  # 232792560 es el m.c.m.
    test = []
    for j in range(1, 21):
        if i % j == 0:
            test.append(1)
    if len(test) == 20:
        print(i)
        break

''' Ejemplo

for i in range(1, 3000):
    test = []
    for j in range(1, 11):
        if i % j == 0:
            test.append(1)
    if len(test) == 10:
        print(i)
        break

'''
