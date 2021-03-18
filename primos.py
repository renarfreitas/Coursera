
def éPrimo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

n = int(input("Digite um número inteiro (zero para sair): "))

while n > 0:
    if éPrimo(n):
        print(n, 'é primo!')
    else:
        print(n, 'não é primo =/')
    n = int(input('Digite um número inteiro (zero para sair): '))

valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)
