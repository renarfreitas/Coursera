import os
os.system("cls")

num = int(input("Informe um número com mais de 2 digitos: "))
prox = 0
resto = 0
soma = 0
i = 1
while i < num:
  resto = num % 10
  prox = num // 10
  num = prox
  soma = resto + soma
  i = i + 1
  if(i >= num):
    break
print(soma)

'''
prox = 0
resto = 0
soma = 0
i = 0
num  = num
while i <= num:
  resto = num % 10
  prox = num // 10
  num = prox
  soma = resto + soma
  i += 1
print (soma)
'''
'''  
while num:
  i += num % 10 # Soma `s` ao ultimo numeral de `n`
  num //= 10 # Remove o ultimo numero de `n`
print(i)
'''
#num  = num * (num-1) * (num-2) * (num-3) * (num-4) * (num-5)
'''
while i <= 1:
  fator = num * (num - 1)
print (fator)
'''