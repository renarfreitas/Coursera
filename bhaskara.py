import math

a = float(input("Valor a: "))
b = float(input("Valor b: "))
c = float(input("Valor c: "))

delta = b ** 2 - 4 * a * c
if delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é",x1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        if x1 < x2:
            pri = x1
            seg = x2
        else:
            pri = x2
            seg = x1
        print("as raízes da equação são",pri,"e",seg)