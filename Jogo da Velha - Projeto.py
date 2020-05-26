jogadores = {
    'jogador1':
    {
        'nome': 'player1',
        'simbolo': 'X'
    },
    'jogador2':
    {
        'nome': 'player2',
        'simbolo': 'O'
    }
}


def avalia_possiveis(tabuleiro):
    possivel_1 = tabuleiro['pos1'] == tabuleiro['pos4'] == tabuleiro['pos7']
    possivel_2 = tabuleiro['pos1'] == tabuleiro['pos2'] == tabuleiro['pos3']
    possivel_3 = tabuleiro['pos1'] == tabuleiro['pos5'] == tabuleiro['pos9']
    possivel_4 = tabuleiro['pos2'] == tabuleiro['pos5'] == tabuleiro['pos8']
    possivel_5 = tabuleiro['pos3'] == tabuleiro['pos6'] == tabuleiro['pos9']
    possivel_6 = tabuleiro['pos4'] == tabuleiro['pos5'] == tabuleiro['pos6']
    possivel_7 = tabuleiro['pos7'] == tabuleiro['pos8'] == tabuleiro['pos9']
    possivel_8 = tabuleiro['pos3'] == tabuleiro['pos5'] == tabuleiro['pos7']
    return [possivel_1, possivel_2,
            possivel_3, possivel_4,
            possivel_5, possivel_6,
            possivel_7, possivel_8]


def bem_vindo():    
    print('Bem Vindo ao Jogo da Velha! Vamos começar!')
    imprimir_separador()


def pedir_jogada(lista_total_palpites, contador_jogadas):
    imprimir_separador()
    while True:
        try:
            jogada = int(
                input(jogadores[f"jogador{contador_jogadas%2+1}"]['nome'] +
                      ', digite uma posição no tabuleiro para jogar: ')
            )
            if jogada in lista_total_palpites:
                break
            else: 
                print('Você digitou um número já pedido, tente novamente')
        except ValueError:
            print('Você não digitou um número válido, tente novamente')
    imprimir_separador()
    return jogada


def imprimir_separador():
    print('-=-'*15)


def imprimir_tabuleiro(tabuleiro): 
    print(f"  {tabuleiro['pos1']}  |  {tabuleiro['pos2']}  |  {tabuleiro['pos3']}  ")
    print('------+------+------')
    print(f"  {tabuleiro['pos4']}  |  {tabuleiro['pos5']}  |  {tabuleiro['pos6']}  ")
    print('------+------+------')
    print(f"  {tabuleiro['pos7']}  |  {tabuleiro['pos8']}  |  {tabuleiro['pos9']}  ")


def iniciar_tabuleiro():
    return { 
      'pos1': 1,
      'pos2': 2,
      'pos3': 3,
      'pos4': 4,
      'pos5': 5,
      'pos6': 6,
      'pos7': 7,
      'pos8': 8,
      'pos9': 9
    }


def jogo():
    tabuleiro = iniciar_tabuleiro()
    contador_jogadas = 0
    lista_total_palpites = palpites_vazios()
    
    while True:
        imprimir_tabuleiro(tabuleiro)
        jogada = pedir_jogada(lista_total_palpites, contador_jogadas)
        lista_total_palpites.remove(jogada)
        tabuleiro = verifica_jogada(jogada, contador_jogadas, tabuleiro)
        verificador_fim_jogo = procurar_vencedor(tabuleiro, contador_jogadas)
        
        if verificador_fim_jogo >= 0:
            if verificador_fim_jogo == 0:
                print("Deu velha! Ninguém ganhou.")
            else:
                print(f"Temos um vencedor! Parabéns {jogadores['jogador' + str(contador_jogadas%2+1)]['nome']}!")
            imprimir_tabuleiro(tabuleiro)
            break
        contador_jogadas += 1


def limpar_tela():
    print("Vamos começar de novo!")


def nomear_jogador():
    nome = input("Qual o nome do primeiro jogador? ").strip()
    nome2 = input('Qual o nome do segundo jogador? ').strip()
    if len(nome) > 0:
        jogadores['jogador1']['nome'] = nome
    if len(nome2) > 0:
        jogadores['jogador2']['nome'] = nome2


def novo_jogo():
    while True:
        jogar_de_novo = input("Deseja jogar novamente?\n" +
                              "Digite S para SIM ou N para NÃO: ").strip().upper()

        if jogar_de_novo[0] == 'S':
            return True
        elif jogar_de_novo[0] == 'N':
            return False
        else:
            print('Entre com uma opção válida!')
            imprimir_separador()
            continue


def procurar_vencedor(tabuleiro, contador_jogadas):
    for possivel in avalia_possiveis(tabuleiro):
        if possivel:
            return 1
        elif contador_jogadas == 8:
            return 0
    return -1


def palpites_vazios(): 
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def verifica_jogada(jogada, numero_jogadas, tabuleiro):
    for key, value in tabuleiro.items():  
        if jogada == value:
            if numero_jogadas % 2 == 0:
                tabuleiro[key] = 'X'
            else:
                tabuleiro[key] = 'O'
    return tabuleiro


if __name__ == '__main__':
    bem_vindo()
    nomear_jogador()
    while True:
        jogo()
        if not novo_jogo():
            break
        limpar_tela()
    print('Fim de jogo...\nAté logo!')
