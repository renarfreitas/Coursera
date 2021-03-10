d = True
i=3
num = int(input("Digite um número inteiro: "))
while (i < num//2) and d:
  if (num % i) == 0:
    d = False
  else:
    i= i+1
if d:
  print("primo")
else:
  print("não primo")