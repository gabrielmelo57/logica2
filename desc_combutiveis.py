# 8. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#    Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro 
#    Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro 

# O programa deverá ler o número de litros vendidos, o tipo de combustível codificado da seguinte forma: 
#    A - Álcool, 
#    G - Gasolina, 
# Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,95 o preço do litro do álcool é R$ 2,89.

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ")
if tipo_combustivel == "A":
    preco_litro = 2.89
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
elif tipo_combustivel == "G":
    preco_litro = 4.95
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
else:
    print("Tipo de combustível inválido!")
    exit()

valor_total = litros * preco_litro
valor_desconto = valor_total * desconto
valor_final = valor_total - valor_desconto

print("O valor a ser pago é: R$ ", valor_final)