while True:
    username = input("Insira seu nome de usuário: ")
    password = input("Insira sua senha: ")
    if username != password:
        print("Nome de usuário: %s \nSenha: %s" %(username, password))
        break
    else:
        print("Erro: nome de usuário e senha devem ser diferentes. Tente novamente.")
