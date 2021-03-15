n = int(input("Digite um número inteiro maior que 1: "))
fator = 2
multi = 0

while n > 1:
    while n % fator == 0:
        multi = multi + 1
        n = n / fator
    if multi > 0:
        print("Fator", fator, "multiplicidade", multi)
    fator = fator + 1
    multi = 0
