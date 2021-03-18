def main():
    print("Welcome to the game!")
    print("Choice: 1 - to play an isolated game")
    print("Choice: 2 - to play a championship")
    choice = int(input())
    if choice == 1:
        print("You chose an isolated match!")
        partida()
    elif choice == 2:
        print("You chose a championship!")
        campeonato()

def usuario_escolhe_jogada(n, m):    
    jog_usuario = int(input("Diga qual a sua jogada: "))                         
    while jog_usuario <= 0 or jog_usuario > n or jog_usuario > m:
        print("Valor incorreto. O valor deve ser entre 1 e {}, ou menor que a quantidade de peças disponíveis {}".format(n, m))
        jog_usuario = int(input("Informe sua jogada: "))   
    print("Você retirou {} peças.".format(jog_usuario))
    print("Agora resta {} peças no tabuleiro.".format(n - jog_usuario))
    return jog_usuario

def campeonato():   
    rodada = 1  
    part_ganhas_pc = 0
    part_ganhas_user = 0  
    while rodada <= 3:
        print("**** Rodada {}".format(rodada))
        vencedor = partida()
        if vencedor == 1:
            part_ganhas_pc += 1
        elif vencedor == 0:
            part_ganhas_user += 1
        rodada += 1   
    print("Championship The End")
    print("Placar: Você {} x {} Computador".format(part_ganhas_user, part_ganhas_pc))

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? ")) 
    vencedor = 2
    peças_restantes = n   
    if n % (m + 1) == 0:
        print("Você começa!")
        proxima_jogada = 0   
        while peças_restantes > 0:
            peças_retiradas = usuario_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas
            if peças_restantes == 0:
                vencedor = 0
                break
            peças_retiradas = computador_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas
            if peças_restantes == 0:
                vencedor = 1
                break                
    else:
        print("Computador começa!")
        while peças_restantes > 0:
            peças_retiradas = computador_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas
            if peças_restantes == 0:
                vencedor = 1
                break
            peças_retiradas = usuario_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas
            if peças_restantes == 0:
                vencedor = 0
                break  
    if vencedor == 1:
        print("Game Over!! PC wins!")
        return 1
    elif vencedor == 0:
        print("Game Over!! You wins!")
        return 0

def calcula_jogada(n, m):    
    p_retirar = 0   
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            p_retirar = i
    return p_retirar 
    
def computador_escolhe_jogada(n, m):    
    if n < m:
        print("O computador retirou {} peças." .format(n))
        print("Agora sobraram {} peças no tabuleiro." .format((n - n)))
        next_play = n
    elif calcula_jogada(n, m) != 0:
        next_play = calcula_jogada(n, m)
        print("O computador retirou {} peças." .format(next_play))
        print("Agora sobraram {} peças no tabuleiro." .format((n - next_play)))   
    else: 
        print("O computador retirou {} peças.".format(m))
        print("Agora sobraram {} peças no tabuleiro.".format((n - m)))
        next_play = m
    return next_play
