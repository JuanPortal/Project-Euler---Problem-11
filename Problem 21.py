# Project Euler - Problem 21


def sDivisores(n):
    divisors = []
    for j in range(1, n):
        if n % j == 0:
            divisors.append(j)
    return sum(divisors)


conjunto = set([])
for i in range(10000):
    if sDivisores(sDivisores(i)) == i and sDivisores(i) != i:
        conjunto.add(i)
        conjunto.add(sDivisores(i))

print(conjunto)
print(sum(conjunto))
