# Project Euler - Problem 2

sequence = [1, 2]
c = 2
while True:
    new = sequence[c - 1] + sequence[c - 2]
    if new > 4000000:
        break
    sequence.append(new)
    c += 1

print(sum([i for i in sequence if i % 2 == 0]))
