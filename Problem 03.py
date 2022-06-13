# Project Euler - Problem 3


def is_prime(n):
    if n <= 1:
        return False

    divisors = []
    for p in range(2, n):
        residue = n % p
        divisors.append(residue)

    if 0 in divisors:
        return False

    else:
        return True


number = 13195

for i in range(number, 1, -1):
    if is_prime(i) and number % i == 0:
        print(i)
        break
