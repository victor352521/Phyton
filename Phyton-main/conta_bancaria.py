class ContaBancaria:
    def __init__(self,numero,titular,saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Número da Conta", self.numero)
        print("Titular", self.titular)
        print("Saldo", self.saldo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Você é pobre, tenha mais dinheiro depois volte para sacar")

#Aqui estou criando uma instância do objeto ContaBancaria
#Com o nome conta_do_victor
numero_conta = input("Digite o número da conta")
titular_conta = input("Digite o titular da conta")
saldo_inicial = float(input("Digite o saldo inicial da conta"))
conta_do_victor = ContaBancaria(numero_conta, titular_conta, saldo_inicial)

#usando os metodos do objeto Conta Bancaria
valor_deposito = float(input("Digite o valor que deseja depositar").replace(",","."))
valor_saque = float(input("Digite o valor que deseja sacar").replace(",","."))

conta_do_victor.depositar(valor_deposito)
conta_do_victor.sacar(valor_saque)
conta_do_victor.exibir_detalhes()
