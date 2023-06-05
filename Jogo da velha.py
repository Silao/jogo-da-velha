#JOGO DA VELHA EM PYTHON 
#OS NUMEROS DA MATRIZ DEFINEM A POSIÇÃO DE CADA JOGADA
matriz = [[1,2,3],[4,5,6],[7,8,9]]
jogador1 = "X"
jogador2 = "Ø"

print('-='*5+" jogo da velha "+'=-'*5)

def estrutura_jogo(jg): #Imprime as jogadas a cada rodada
    
    for l in range(3):
        print(*matriz[l], sep="|")  
    if jg == "" or jg == jogador2: #inicia com o Jogador1 e depois alterna a cada rodada
        print('-='*6+" jogador X "+'=-'*6)
        jogadas(jogador1)
    else:
        print('-='*6+" jogador O "+'=-'*6)
        jogadas(jogador2)    
       
def jogadas(jogador): #colhe e armazena as jogadas a cada rodada

    try: #caso o usuario digite uma letra ira ser solicitado um numero da Matriz
        jogada = int(input("Escolha um numero para a jogada: "))

        if str(jogada) in str(matriz): #condição caso jogador escolha um numero indisponivel
            
            for indice, linha in enumerate(matriz):    
                if str(jogada) in str(linha): #substitui o nº escolhido pelo simbolo do jogador
                    matriz[indice][linha.index(jogada)] = jogador 
            verifica_jogadas(jogador) #chama a função que consulta se é uma jogada vencedora
        else:
            print(f"Numero {jogada} já ocupado! escolha outro")
            jogadas(jogador)                       
    except:
        print("FAVOR ESCOLHER UM NUMERO DA LISTA")
        jogadas(jogador)

def verifica_jogadas(simbolo):    
    #condição que verifica se o jogo terminou empatado, ou se ha nº disponivel
    if len(set(list(matriz[0]+matriz[1]+matriz[2]))) > 2:
        #sequencias vitóriosas para comparação com a matriz atual a cada rodada
        sq1 = matriz[0][0], matriz[1][0], matriz[2][0]
        sq2 = matriz[0][1], matriz[1][1], matriz[2][1]
        sq3 = matriz[0][2], matriz[1][2], matriz[2][2]
        sq4 = matriz[0][2], matriz[1][1], matriz[2][0]
        sq5 = matriz[0][0], matriz[1][1], matriz[2][2]
        
        if matriz.count([simbolo, simbolo, simbolo]) == 1:
            vencedor(simbolo)
        elif sq1.count(simbolo) == 3:
            vencedor(simbolo)
        elif sq2.count(simbolo) == 3:            
            vencedor(simbolo)       
        elif sq3.count(simbolo) == 3:
            vencedor(simbolo) 
        elif sq4.count(simbolo) == 3:
            vencedor(simbolo)  
        elif sq5.count(simbolo) == 3:
            vencedor(simbolo)          
        else: #caso não seja elegivél um vencedor nesta rodada, inicia uma nova.
            if simbolo == jogador1: #começa uma nova rodada alterando para o próximo jogador
                estrutura_jogo(jogador1)                      
            else: 
                estrutura_jogo(jogador2)
    else:
        for l in range(3):
                print(*matriz[l], sep="|")
        print('!-'*5+" JOGO EMPATADO "+'-!'*5)

def vencedor(vencedor):#imprime a jogada e o vencedor
    print(f"-=-=-=-=- {vencedor} VENCEU !!! \O/ =-=-=-=-") 
    for l in range(3):
        print(*matriz[l], sep="|")     
         
estrutura_jogo("")