# 2. Desenvolva um programa que leia três números e que imprima:
#    2.1. o maior,
#    2.2. o menor,
#    2.3. a soma,
#    2.4. a média.
# Exemplo:
# num1 = 5	num2 = 3	num3 = 10
# **********
# maior = 10
# menor = 3
# soma = 18
# media = 6

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
soma = num1 + num2 + num3
media = soma / 3
print("Maior =", maior)
print("Menor =", menor)
print("Soma =", soma)
print("Média =", media)