# Project Euler - Problem 17

import inflect

p = inflect.engine()


def fix(cadenita):
    cadenita = cadenita.replace("-", "")
    cadenita = cadenita.replace(" ", "")
    return cadenita


suma = 0
for i in range(1, 1001):
    suma += len(fix(p.number_to_words(i)))

print(suma)
