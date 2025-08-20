# Pedro Faleiros - RM: 562523
# Luan Felix - RM: 565541
# João Lopes - RM: 565737

# Globla Solution - Computional Thinking Using Python - FIAP - 2025

import time # Importa o módulo de tempo para registrar data/hora das ocorrências


# Lista que armazenará todos os usuários [nome, email, senha, pontos]
lista_usuarios = []

# Variável que armazena o usuário atualmente logado
usuario_logado = None

# Lista que armazenará as ocorrências registradas
ocorrencias = []

# Exibe o menu principal e retorna a opção escolhida
def mostra_menu():
    print("---------------------- Menu ----------------------")
    print("[1] - Fazer Login")
    print("[2] - Criar Conta")
    print("[3] - Registrar Ocorrência de Enchente")
    print("[4] - Ver Ocorrências")
    print("[5] - Exibir Liderança")
    print("[6] - Ver Perfil")
    print("[7] - Editar Perfil")
    print("[8] - Sair da Conta")
    print("[9] - Sair do App")
    numero_acao =  int(input("Digite o número da ação que deseja realizar: "))
    return numero_acao


# Solicita o nome e valida se foi digitado algo
def digita_nome():
    nome = input("Digite o seu nome: ")

    while len(nome) < 1:
        nome = input("Por favor, digite o nome: ")

    return nome

# Solicita o email e valida se foi digitado algo
def digita_email():
    email = input("Digite o seu e-mail: ")

    while len(email) < 1:
        email = input("Por favor, digite o e-mail: ")

    return email

# Solicita a senha e exige no mínimo 8 caracteres
def digita_senha():
    senha = input("Digite a sua senha: ")

    while len(senha) < 8:
        senha = input("A senha deve ter no mínimo 8 caracteres. Digite a senha novamente: ")

    return senha

# Cria um novo usuário e adiciona na lista
def criar_conta():
    nome = digita_nome()

    email = digita_email()

    senha = digita_senha()

    lista_usuarios.append([nome, email, senha, 0]) # pontos começam em 0
    print("Usuário cadastrado com sucesso!\n")

# Realiza login do usuário se e-mail e senha forem válidos
def fazer_login():
    global usuario_logado # Permite alterar a variável global

    if not usuario_logado:
        email = digita_email()
        senha = digita_senha()

        for usuario in lista_usuarios:
            if usuario[1] == email and usuario[2] == senha:
                usuario_logado = usuario
                print(f"Login realizado com sucesso! Bem-vindo, {usuario[0]}.\n")
                return

        print("E-mail ou senha incorretos.\n")
        return 
    
    print("Você já está logado.\n")

# Exibe os dados do usuário logado
def ver_perfil():
    if usuario_logado:
        print("\n------ Perfil ------")
        print(f"Nome: {usuario_logado[0]}")
        print(f"E-mail: {usuario_logado[1]}")
        print(f"Senha: {usuario_logado[2]}")
        print(f"Pontos: {usuario_logado[3]} pontos\n")
    else:
        print("Você precisa estar logado para ver o perfil.\n")

# Encerra a sessão do usuário atual
def sair_da_conta():
    global usuario_logado
    if usuario_logado:
        usuario_logado = None 
        print("Você saiu da conta.\n")
    else:
        print("Você não está logado.\n")


# Permite o usuário registrar uma ocorrência de enchente
def registrar_ocorrencia():
    if not usuario_logado:
        print("Você precisa estar logado.\n")
        return

    # Coleta dados da ocorrência
    local = input("Digite o local do alagamento (bairro/rua): ")

    while len(local) < 1:
        local = input("Por favor, digite o local do alagamento (bairro/rua): ")

    nivel = input("Digite o nível da água (ex: até o joelho, cintura, etc): ")

    while len(nivel) < 1:
        nivel = input("Por favor, digite o nível da água (ex: até o joelho, cintura, etc): ")

    imagem = input("Nome da imagem (simulado): ")

    while len(imagem) < 1:
        imagem = input("Por favor, digite o nome da imagem (simulado): ")

    horario = time.strftime("%d/%m/%Y %H:%M:%S") # Data e hora atual formatada

    # Adiciona a ocorrência na lista e recompensa o usuário com pontos
    ocorrencias.append([usuario_logado[0], local, nivel, imagem, horario])
    usuario_logado[3] += 10  # adiciona pontos
    print("Ocorrência registrada com sucesso! +10 pontos.\n")

# Exibe todas as ocorrências registradas
def ver_ocorrencias():
    if not ocorrencias:
        print("Nenhuma ocorrência registrada ainda.\n")
        return
    print("\n------------- Ocorrências Registradas -------------")
    for ocorrencia in ocorrencias:
        print(f"Usuário: {ocorrencia[0]} | Local: {ocorrencia[1]} | Nível: {ocorrencia[2]} | Imagem: {ocorrencia[3]} | Data/Hora: {ocorrencia[4]}")

    print("")


# Permite ao usuário alterar nome, e-mail ou senha
def editar_perfil():
    if not usuario_logado:
        print("Você precisa estar logado.\n")
        return
    print("\n-------- Editar Perfil --------")
    print(f"[1] - Nome: {usuario_logado[0]}")
    print(f"[2] - E-mail: {usuario_logado[1]}")
    print(f"[3] - Senha: {usuario_logado[2]}")
    print(f"[4] - Voltar")
    acao = int(input("Digite o campo que deseja editar: "))

    while acao < 1 or acao > 4:
        print("Opção inválida.")
        acao = int(input("Digite o campo que deseja editar: "))

    if acao == 1:
        nome = digita_nome()
        usuario_logado[0] = nome 
        print("Nome alterado com sucesso!\n")
    elif acao == 2:
        email = digita_email()
        usuario_logado[1] = email 
        print("E-mail alterado com sucesso!\n")
    elif acao == 3:
        senha = digita_senha()
        usuario_logado[2] = senha 
        print("Senha alterada com sucesso!")
    elif acao == 4:
        print("")
    else:
        print("Opção inválida.\n")


# Exibe ranking dos usuários com mais pontos
def exibir_lideranca():
    if len(lista_usuarios) > 0:
        print("\n--- Tabela de Liderança ---")

        # Cópia da lista para ordenar sem alterar a original
        usuarios_ordenados = []
        for usuario in lista_usuarios:
            usuarios_ordenados.append(usuario)

        # Ordena manualmente os usuários com mais pontos primeiro (bubble sort simples)
        for i in range(len(usuarios_ordenados)):
            for j in range(i + 1, len(usuarios_ordenados)):
                if usuarios_ordenados[j][3] > usuarios_ordenados[i][3]:
                    usuarios_ordenados[i], usuarios_ordenados[j] = usuarios_ordenados[j], usuarios_ordenados[i]

        # Exibe a tabela
        posicao = 1
        for usuario in usuarios_ordenados:
            nome = usuario[0]
            pontos = usuario[3]
            print(f"{posicao}º - {nome} | Pontos: {pontos}")
            posicao += 1

        print("----------------------------\n")
        return 
    
    print("Nenhum usuário cadastrado.\n")


# Loop principal que exibe o menu e executa ações até o usuário sair
while True:
    numero_acao = mostra_menu()

    if numero_acao == 1:
        fazer_login()
    elif numero_acao == 2:
        criar_conta()
    elif numero_acao == 3:
        registrar_ocorrencia()
    elif numero_acao == 4:
        ver_ocorrencias()
    elif numero_acao == 5:
        exibir_lideranca()
    elif numero_acao == 6:
        ver_perfil()
    elif numero_acao == 7:
        editar_perfil()
    elif numero_acao == 8:
        sair_da_conta()
    elif numero_acao == 9:
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida.\n")