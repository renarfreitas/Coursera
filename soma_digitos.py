num = int(input("igite um número inteiro: "))
i=0
while num:
  i += num % 10
  num //= 10
print(i)