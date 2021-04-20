# Project Euler - Problem 14

cantidades = []
for j in range(1000000):
    lista = [j + 1]
    for i in range(1000000):
        if lista[i] % 2 == 0:
            lista.append(int(lista[i] / 2))
        else:
            lista.append(int(3 * lista[i] + 1))

        if lista[len(lista) - 1] == 1:
            break

    # print(f"{len(lista)} - {lista}")
    cantidades.append(len(lista))

print(max(cantidades))
