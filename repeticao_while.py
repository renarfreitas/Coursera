'''
print("Digite uma sequência de valores terminada por zero.")
soma = 0
valor = 1
while valor != 0:
  valor = int(input("Digite um valor a ser somado: "))
  soma = soma+valor
print("A soma dos valores digitados é: ", soma)
'''
print("Digite uma sequência de valores terminada por zero.")
produto = 1
valor = 1
while valor != "*":
  valor = int(input("Digite um valor a ser multiplicado: "))
  produto = produto * valor
print("A multiplicação dos valores digitados é: ", produto)

'''
valor = 1
i = 0
tamanho = int(input("Favor informar a o tamanho da sequência de números: "))
while i <= tamanho:
  print(2**i)
  i = i + 1
'''