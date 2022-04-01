#Aluno: Henrique Vince Rodrigues
#Curso: Inteligência Artificial Aplicada

import random

#Exibe o nome do jogo e mensagem de boas-vindas
print('ZOMBIE DICE')
print('Seja bem-vindo ao Zombie Dice!')

#Armazena a quantidade de jogadores e solicita quantos estão jogando
numJogadores = 0
while numJogadores < 2:
    numJogadores = int(input('Informe o número de jogadores: '))

#se numero de jogadores < 2
    if numJogadores < 2:
        print('Você precisa de pelo menos 2 jogadores!')
#por ser um while, caso o if acima for acionado repetirá a função desde o inicio

#inicia lista vazia (servirá para armazenar os jogadores)
listaJogadores = []
#cria range com quantidade de jogadores , cada valor da range ficará na variavel "i"
for i in range(numJogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ') #permite digitar o nome do jogador 1
    listaJogadores.append(nome) #vai repeir o comando acima de acordo com a quantidade de jogadores

print(listaJogadores, '\n') #mostra a lista de jogadores

dadoVerde = 'CPCTPC' #faces do dado verde; 3 cérebros, 2 passos e 1 tiro
dadoAmarelo = 'TPCTPC' #faces do dado amarelo; 2 cérebros, 2 passos e 2 tiros
dadoVermelho = 'TPCTPT' #faces do dado vermelho; 1 cérebro, 2 passos e 3 tiros

#lista com os dados que ficam dentro do pote
listaDados = [
    dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, #6 dados verdes
    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, #4 dados amarelos
    dadoVermelho, dadoVermelho, dadoVermelho #3 dados verdes
]

print('--------------INÍCIO DO JOGO---------------') #mostra mensagem informando inicio do jogo

jogadorAtual = 0 #armazena o jogador que está jogando
dadosSorteados = [] #lista com os dados que forem sorteados no turno
passos = 0 #armazena dados com lado passos
tiros = 0 #armazena dados com lado tiros
cerebros = 0 #armazena dados com lado cerebros

while True:
    print("TURNO DO JOGADOR:  ", listaJogadores[jogadorAtual]) #mostra o jogador da vez

    for i in (0, 1, 2): #faça para os 3 dados:
        numSorteado = random.randint(0, len(listaDados)) #sorteia um numero de 0 a 12 (ou quantidade de dados na lista listaDados) e armazena em numSorteado
        dadoSorteado = listaDados[numSorteado] #puxa a lista de dados, numSorteado vai determinar a cor do dado

        if dadoSorteado == 'CPCTPC': #se o dado sorteado for CPCTPC, cor do dado é verde
            corDado = "VERDE"
        elif dadoSorteado == 'TPCTPC': #se o dado sorteado for TPCTPC, cor do dado é amarelo
            corDado = "AMARELO"
        else:
            corDado = "VERMELHO" #se o dado sorteado for TPCTPT, cor do dado é vermelho

        print('Dado sorteado: ', corDado) #mostra qual dado foi sorteado
        dadosSorteados.append(dadoSorteado) #appenda na lista de dados sorteados qual o dadoSorteado

    #Inicia lançamento dos dados sorteados
    input('\nPressione ENTER para jogar os dados sorteados.')
    print('\nAs faces sorteadas foram: ') #

    for dadoSorteado in dadosSorteados: #vai percorrer dentro da lista dadosSorteados, cada item que encontrar vai para a variavel dadoSorteado
        numFaceDado = random.randint(0, 5) #sorteia uma das 6 faces do dado

        #Se a face sorteada é CEREBRO
        if dadoSorteado[numFaceDado] == "C":
            print('- CÉREBRO (você comeu um cérebro)')
            cerebros = cerebros + 1 #adiciona variavel contadora dos cérebros no turno atual

        #Se a face sorteada é TIRO
        elif dadoSorteado[numFaceDado] == "T":
            print("- TIRO (você levou um tiro)")
            tiros = tiros + 1 #adiciona variavel contadora dos tiros no turno atual

        #Se a face sorteada é PASSOS
        else:
            print("- PASSOS (uma vítima escapou)")
            passos = passos + 1 #adiciona variavel contadora dos passos no turno atual

    print('SCORE ATUAL: ')
    print('CÉREBROS: ', cerebros)
    print('TIROS: ', tiros)
    
    #Pergunta se jogador quer continuar ou anotar seus pontos
    continuarTurno = input("\nATENÇÃO: Deseja continuar jogando dados? Digite 's' para sim, 'n' para não, depois pressione ENTER:  \n")

    #Fim do turno
    if continuarTurno.lower() == 'n':

        #Altera o jogador da rodada
        jogadorAtual = jogadorAtual + 1
        #Zera os dados sorteados
        dadosSorteados = []

        #Zera os contadores
        tiros = 0
        cerebros = 0
        passos = 0

        #Se ja há um turno por jogador
        if jogadorAtual == len(listaJogadores):
            print("\n ----------Finalizando Zombie Dice... Obrigado por jogar!-----------")
            break

    else:
        print("\n----------Iniciando +1 rodada no turno atual------------\n")

        #reinicia os dados sorteados
        dadosSorteados = []