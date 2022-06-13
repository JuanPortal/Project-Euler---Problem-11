# Project Euler - Problem 17

import inflect  # inflect helps us to get the name of the numbers

p = inflect.engine()


def fix(string):
    return string.replace("-", "").replace(" ", "")


sum = 0
for i in range(1, 1001):
    sum += len(fix(p.number_to_words(i)))

print(sum)
