import os
os.system('clear')

n = int(input("Digite o valor de n: "))
soma = 0

i = 1
while i <= n:
    soma = soma + i
    i = i + 1
print("A soma dos", n, "primeiros inteiros positivos é", soma)