# Project Euler - Problem 21


def d(n):
    divisors = []
    for j in range(1, n):
        if n % j == 0:
            divisors.append(j)
    return sum(divisors)


amicable_numbers = set([])
for i in range(10000):
    if d(d(i)) == i and d(i) != i:
        amicable_numbers.add(i)
        amicable_numbers.add(d(i))

# print(amicable_numbers)
print(sum(amicable_numbers))
