def fatorial(n):
    f = 1
    while n > 1:
        f = f * n
        n = n-1
    return f
    
n = int(input("Digite um número inteiro possitivo: "))
while n >= 0:
    fatorial(n)
    print(fatorial(n))
    n = int(input("Digite um número inteiro possitivo: "))
