import jogo_da_forca
import adivinhacao

def escolha_jogo():
    print("******************")
    print("**Escolha o jogo**")
    print("******************")
    print("(1)Forca,(2)Advinhação")

    jogo = int(input("Qual jogo você quer jogar hoje?"))

    if (jogo == 1):
        print("Jogo da forca")
        jogo_da_forca.jogar()
    elif (jogo == 2):
        print("Jogo da advinhação")
        adivinhacao.jogar_advinhacao()

if(__name__=="__main__"):
    escolha_jogo()