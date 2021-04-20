# Project Euler - Problem 1

divisores = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        divisores.append(i)

print()
print(divisores)
print(sum(divisores))
