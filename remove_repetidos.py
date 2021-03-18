def remove_repetidos(lista):
    y = []
    for i in lista:
        if i not in y:
            y.append(i)
    y.sort()
    return y
