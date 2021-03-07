import math

x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))
x1 = int(input("Informe o terceiro número: "))
y1 = int(input("Informe o quarto número: "))

distancia = math.sqrt(((x - x1)**2) + ((y - y1)**2))

if distancia >= 10:
  print("longe")
else:
  print("perto")