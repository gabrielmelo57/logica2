# 5. Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:

# Código	Condição de Pagamento	Desconto (%)
# 1 	À vista (em espécie) 	10
# 2	Cartão de débito	5
# 3	Cartão de crédito	3
# 4	PIX			7.5

# Construa um programa que solicite ao operador do caixa o preço total da venda, bem como a forma de pagamento.
# Ao fim, o programa deve informar o valor final a ser pago.

preco_total = float(input("Digite o preço total da venda: "))

forma_pagamento = int(input("Digite o código da forma de pagamento: "))

if forma_pagamento == 1:
    desconto = 0.10
elif forma_pagamento == 2:
    desconto = 0.05
elif forma_pagamento == 3:
    desconto = 0.03
elif forma_pagamento == 4:
    desconto = 0.075
else:
    print("Forma de pagamento inválida!")
    exit()

valor_final = preco_total - (preco_total * desconto)
print("O valor final a ser pago é: R$ ", valor_final)