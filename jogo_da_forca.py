def jogar():

    palavra_secreta = "malakoi"
    letras_acertadas = ["_","_","_","_","_","_","_"]
    tentativas = 10

    while tentativas > 0 and "_" in letras_acertadas:
        palpite = input("Digite uma letra:").lower()
        
        if palpite in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if palpite == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas -= 1 
            print (f"Você tem {tentativas} tentativas restantes");
        print(" ".join(letras_acertadas))
            
    if "_" not in letras_acertadas:
    print (f"Parabéns! Você acertou.")
    else:
        print (f"Poxa, não foi dessa vez :(")

if(__name__=="__main__")
    jogar()