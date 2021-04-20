# Project Euler - Problem 4

palindromos = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if str(i * j) == str(i * j)[::-1]:
            palindromos.append(i * j)

print(max(palindromos))
