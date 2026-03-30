# 1. Desenvolva um programa que pergunte a velocidade do carro de um usuário. 
# Se a velocidade ultrapassar 80km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 50,00 por cada km acima de 80 km/h.
# Exemplo: Digite a velocidade em Km/h: 85
# Limite = 80Km/h
# Excedeu 5Km/h
# multa = 5Km/h * R$ 50,00
# Valor da multa: R$ 250,00

velocidade = float(input("Digite a velocidade do carro em Km/h: "))
limite = 80.0
if velocidade > limite:
    excedente = velocidade - limite
    multa = excedente * 50.0
    print("Limite =", limite, "Km/h")
    print("Excedeu", excedente, "Km/h")
    print("Valor da multa: R$", multa)
else:
    print("Velocidade dentro do limite permitido.")