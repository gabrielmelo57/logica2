# 4. Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa que auxilie os seus eletricistas no cálculo das principais grandezas da Eletricidade
# que são Tensão, Resistência e Corrente. Sabe-se que:
# U = R * I, 
# onde, 
# U é a Tensão      (em V), 
# R é a Resistência (em Ώ) e,
# I é a Corrente    (em A).

# Você foi contratado(a) pela empresa para atender a essa solicitação.
# Construa um programa que apresente o seguinte menu:

# ******************************
# CÁLCULO DE GRANDEZAS ELÉTRICAS
# ******************************
# 1. Tensão (em Volt)
# 2. Resistência (em Ohm)
# 3. Corrente (em Ampére)
# 4. Sair do programa
# ******************************
# Qual grandeza deseja calcular?

# Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas para realizar o cálculo.

# Quando o eletricista escolher:
# 1. Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente.
#    Utilizar a fórmula: U = R * I

# 2. Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente.
#    Utilizar a fórmula: R = U / I

# 3. Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência.
#    Utilizar a fórmula: I = U / R

# Por fim, o programa deve calcular e apresentar o valor encontrado para a grandeza escolhida.
# Obs.: Qualquer opção diferente das apresentadas no menu (1 a 4) deverão ser informadas ao usuário como 'Opção inválida!'

print("******************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("******************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("4. Sair do programa")
print("******************************")
print("Qual grandeza deseja calcular?")
opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    resistencia = float(input("Digite o valor da Resistência (em Ohm): "))
    corrente = float(input("Digite o valor da Corrente (em Ampére): "))
    tensao = resistencia * corrente
    print("O valor da Tensão é: {:.2f} V".format(tensao))
elif opcao == 2:
    tensao = float(input("Digite o valor da Tensão (em Volt): "))
    corrente = float(input("Digite o valor da Corrente (em Ampére): "))
    resistencia = tensao / corrente
    print("O valor da Resistência é: {:.2f} Ώ".format(resistencia))
elif opcao == 3:
    tensao = float(input("Digite o valor da Tensão (em Volt): "))
    resistencia = float(input("Digite o valor da Resistência (em Ohm): "))
    corrente = tensao / resistencia
    print("O valor da Corrente é: {:.2f} A".format(corrente))
elif opcao == 4:
    print("Saindo do programa...")
else:
    print("Opção inválida!")