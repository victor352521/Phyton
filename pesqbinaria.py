def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) -1
    tentativas = 0

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        tentativas += 1 
        print(tentativas)
        print(f'tamanho lista:(len(lista)')
        if chute == item:
            return meio
        if chute > item:
            alto = meio 
        else:
            baixo = meio +1
        #return None

minha_Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(pesquisa_binaria(minha_Lista, 1))

