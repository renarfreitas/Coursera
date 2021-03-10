num = input("Digite um número inteiro: ")

tamanho = len(num)
verifica = False
i = 0

while i < tamanho - 1:
    if num[i] == num[i + 1]:
        verifica = True
    i += 1
    
if verifica:
    print("sim")
else:
    print("não")