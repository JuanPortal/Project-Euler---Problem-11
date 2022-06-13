# Project Euler - Problem 16


def digits_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum


print(digits_sum(2 ** 1000))
