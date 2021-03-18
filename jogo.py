def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))   
    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()

def usuario_escolhe_jogada(n, m):  
    jogada_usuario = int(input("Informe sua jogada: "))                       
    while jogada_usuario <= 0 or jogada_usuario > n or jogada_usuario > m:
        print("Valor incorreto. O valor deve estar entre 1 e %d, ou ser menor que a quantidade de peças disponíveis (%d)"% (n, m))
        jogada_usuario = int(input("Informe sua jogada: ")) 
    print("\nVocê tirou %d peças." % jogada_usuario)
    print("Agora resta %d peças no tabuleiro.\n" % (n - jogada_usuario))
    return jogada_usuario

def campeonato():   
    rodada = 1  
    partidas_ganhas_cpu = 0
    partidas_ganhas_usuario = 0    
    while rodada <= 3:
        print("**** Rodada %d ****" % rodada)
        vencedor = partida()
        if vencedor == 1:
            partidas_ganhas_cpu += 1
        elif vencedor == 0:
            partidas_ganhas_usuario += 1
        rodada += 1  
    print("**** Final do campeonato! ****\n")
    print("Placar: Você %d x %d Computador" % (partidas_ganhas_usuario, partidas_ganhas_cpu))

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? ")) 
    vencedor = 2   
    peças_restantes = n  
    if n % (m + 1) == 0:
        print("Você começa!\n")
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
        print("Computador começa!\n")
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
        print("Fim de jogo! O computador ganhou!\n")
        return 1
    elif vencedor == 0:
        print("Fim de jogo! Você ganhou!\n")
        return 0

def calcula_jogada(n, m):   
    peças_a_retirar = 0   
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            peças_a_retirar = i
    return peças_a_retirar 
    
def computador_escolhe_jogada(n, m):    
    if n < m:
        print("O computador tirou %d peças." % n)
        print("Agora restam %d peças no tabuleiro.\n" % (n - n))
        proxima_jogada = n
    
    elif calcula_jogada(n, m) != 0:
        proxima_jogada = calcula_jogada(n, m)
        print("O computador tirou %d peças." % proxima_jogada)
        print("Agora restam %d peças no tabuleiro.\n" % (n - proxima_jogada))
    
    else:
        print("O computador tirou %d peças." % m)
        print("Agora restam %d peças no tabuleiro.\n" % (n - m))
        proxima_jogada = m

    return proxima_jogada
