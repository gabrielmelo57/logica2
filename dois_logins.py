# 4. Suponha que o professor Atila possua dois logins na rede do SENAI-SP. 
# Construa um programa que valide o acesso do professor à rede. 
# Caso o par usuário/senha informado esteja correto, o programa deve imprimir a mensagem “Seja bem vindo!”.
# Caso contrário, “Usuário e senha não conferem”.
# Dados dos dois logins:
# login 1			login 2
# usuário: atila		usuário: olivi
# senha: 12345		senha: 54321

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if (usuario == "atila" and senha == "12345") or (usuario == "olivi" and senha == "54321"):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem")