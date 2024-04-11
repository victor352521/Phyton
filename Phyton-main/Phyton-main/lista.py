def mostrar_lista(lista):
    print("Lista:")
    for item in lista:
        print(item)
    print()

def adicionar_item(lista):
    novo_item = input("Digite uma fruta: ")
    lista.append(novo_item)
    print("Fruta adicionada com sucesso!")
    mostrar_lista(lista)

def excluir_item(lista):
    item_excluir = input("Digite a fruta você que deseja excluir: ")
    if item_excluir in lista:
        lista.remove(item_excluir)
        print("Fruta excluída com sucesso!")
    else:
        print("O item não está na lista.")
    mostrar_lista(lista)

def main():
    lista = []
    continuar = True

    while continuar:
        print("Escolha uma opção:")
        print("1. Adicionar uma fruta à lista")
        print("2. Excluir uma fruta da lista")
        print("3. Mostrar lista atual")
        print("4. Sair do programa")

        opcao = input("Opção: ")

        if opcao == '1':
            adicionar_item(lista)
        elif opcao == '2':
            excluir_item(lista)
        elif opcao == '3':
            mostrar_lista(lista)
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()