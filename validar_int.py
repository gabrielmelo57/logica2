# 7. Desenvolva um programa que receba um inteiro e exiba o mesmo na tela. Se o valor digitado for em branco exibir 'Dado inválido'

inteiro = int(input("Digite um número inteiro: "))
if inteiro == "":
    print("Dado inválido")