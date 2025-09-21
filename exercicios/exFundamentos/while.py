# EXERCICIOS COM O WHILE

# Tentativa de senha

usuario = "gui.andrade"
senha = "guilherme8"
tentativas = 0
max_tentativas = 3

print("Bem vindo ao Gui Corporation!!")
print("-------------------------------")
print("Entre no seu cadastro: ")

while tentativas < max_tentativas:
    entrada_user = input("Digite o nome do usuário: \n")
    entrada_password = input("Digite sua senha: \n")

    if entrada_user == usuario and entrada_password == senha:
        print("Entrando no seu cadastro...")
        print("-------------------------------")
        break
    else:
        print("Usuário ou senha incorretos, tente novamente!")
        print("-------------------------------")
        
    tentativas += 1

    if tentativas == max_tentativas:
        print("Suas tentativas acabaram, entre em contato com o suporte!!")