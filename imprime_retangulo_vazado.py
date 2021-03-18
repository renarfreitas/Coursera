l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

li = 1

while li <= a:
    print("#", end = "")
    c = 2
    while c < l: 
        if li == 1 or li == a:
            print("#", end = "")
        else:
            print(end = " ")
        c += 1
    print("#")
    li += 1
