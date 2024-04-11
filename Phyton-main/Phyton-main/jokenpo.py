import random
def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    print("bem vindo ao jogo jokenpô")
    print("escolha: pedra, papel, tesoura")

    while True:
        escolha_jogador = input("sua escolha:").lower()
        if escolha_jogador not in opcoes:
            print("escolha invalida, tente novamente")
            continue

        escolha_computador = random.choice(opcoes)
        print(f"computador escolheu: {escolha_computador}")

        if escolha_jogador == escolha_computador:
            print("empate")
        elif (
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "tesoura" and escolha_computador  == "papel")
            ):
            print("voce ganhou")
        else:
            print("voce perdeu")
            
        jogar_novamente = input("voce quer jogar novamnte?").lower()
        if jogar_novamente != "sim":
            break

if __name__ == "__main__":
    jogar_jokenpo()




