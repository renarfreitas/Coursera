l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

while a > 0:
    for i in range(l):
        print('#', end = '')
    print()
    a -= 1
