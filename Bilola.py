#Calculo Área do Circulo
def calculo():
    raio = float(input("Digite o valor do raio"))
    pi = 3.14
    area =  pi * (raio*raio)
    return f'O valor da area é igual a {area}'

print(calculo())

#Calculo Área do Quadrado
def calculo2():
    lado = float(input("Digite o valor do lado"))
    area = (lado * lado)
    return f'O valor da area é igual a {area}'

print(calculo2())

#Calculo Área do Triângulo
def calculo3():
    base = float(input("Digite o valor da base"))
    altura = float(input("Digite o valor da altura"))
    area = (base * altura)/2
    return f'O valor da area é igual a {area}'

print(calculo3())
