'''def é_hipotenusa(a):
    cateto1 = 0
    cateto2 = 0
    for i in range(1, a):
        for j in range(1, a):
            if i ** 2 + j ** 2 == a ** 2:
                cateto1 = i
                cateto2 = j
                break
    if cateto1 != 0 and cateto2 != 0:
        return True
    else:
        return False
def soma_hipotenusas(n):
    lista = []
    soma = 0
    for i in range(2, n+1):
        if é_hipotenusa(i) == True:
            lista.append(i)
            soma += i
    print(lista)
    print(soma)

flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam-1
'''
aluno = ["Fulano de Tal", 25, "Rua xyz, 123", "São Paulo", 3, "Matemática", 7.5, "Português", 6.6, "Artes", 10]
