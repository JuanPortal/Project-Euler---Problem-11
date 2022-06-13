# Project Euler - Problem 4

palindromes = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if str(i * j) == str(i * j)[::-1]:
            palindromes.append(i * j)

print(max(palindromes))
