import random
import jogos

def jogar_advinhacao():
    nivel = int(input("Escolha o nível de dificuldade (1- fácil, 2- médio, 3- difícil):"))
    max_numero = 25 if nivel == 1 else 50 if nivel == 2 else 100
    numero_secreto = random.randint(1, max_numero)
    tentativas = 10 if nivel == 1 else 5 if nivel == 2 else 3
    pontos = 1000
    
    print(f"jogo de advinhação - Nível {nivel}")
    print(f"tente advinhar o número que estou pensando, entre 1 e {max_numero}.")
    
    for tentativa in range (1, tentativas + 1):
        print(f"Tentativa {tentativa} de {tentativas}")
        palpite = int(input("Digite seu palpite: "))
    
        if palpite < 1 or palpite > max_numero:
            print(f"Digite um número entre 1 e {max_numero}.")
            continue
        
        acertou = palpite == numero_secreto
        maior =  palpite > numero_secreto
        menor = palpite < numero_secreto
        
        if acertou:
            print(f"Você acertou e fez {pontos} pontos")
            break
        
        else:
            pontos_perdidos = abs(numero_secreto - palpite)
            pontos -= pontos_perdidos
            if maior:
                print("Seu palpite foi maior do que o número secreto.")
            elif menor:
                print("seu palpite foi menor do que o número secreto.")
                
    if not acertou: 
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
    print("Fim do jogo! HAHAHAHAHHAHAHHAAH!!!")

    jogos.escolha_jogo()
    
jogar_advinhacao()
            