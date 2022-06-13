# Project Euler - Problem 9

for i in range(1, 998):
    for j in range(1, 998):
        for k in range(1, 998):
            if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2:
                print(i * j * k)
                break
