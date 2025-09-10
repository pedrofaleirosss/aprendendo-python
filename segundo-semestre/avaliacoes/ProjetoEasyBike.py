# RM 566254 - GEOVANA MARIA DA SILVA CARDOSO
# RM 562544 - MARIANA SILVA DO EGITO MOREIRA
# RM 562523 - PEDRO ALVES FALEIROS
import random
import re

usuarios: list = []
bikes: list = []
protocolos: list = []

usuario_logado = None

def mostra_menu() -> None:
    """
    Essa função exibe um menu com as funcionalidades do sistema
    """
    print("----------- Menu ------------")
    print("[1] Cadastrar Usuário")
    print("[2] Fazer Login")
    print("[3] Cadastrar bike")
    print("[4] Acionar Sinistro")
    print("[5] Cancelar Vistoria")
    print("[6] Sair da Conta")
    print("[7] Ver Perfil")
    print("[8] Verificar status da vistoria")
    print("[9] Exibir relatório de vistorias")

def digita_email() -> str:
    """
    Essa função solicita que o usuário digite um e-mail,
    valida esse e-mail e retorna ele em string
    """
    email: str = input("Digite o seu e-mail: ")

    while not email.find("@") or not email.endswith(".com"):
        email: str = input("E-mail inválido. Digite o e-mail novamente: ")

    return email

def digita_senha() -> str:
    """
    Essa função solicita que o usuário digite uma senha,
    valida ela, e retorna ela em string
    """
    senha: str = input("Digite a sua senha: ")

    while not (len(senha) >= 8 and
           re.search(r"[A-Z]", senha) and
           re.search(r"[a-z]", senha) and
           re.search(r"[0-9]", senha) and
           re.search(r"[\W_]", senha)):

        senha: str = input("A senha deve ter pelo menos 8 caracteres, um número, uma letra maiúscula e minúscula, e um simbolo. Digite a senha novamente: ")


    return senha

def cadastra_usuario() -> None:
    """
    Essa função solicita o nome do usuário,
    valida esse nome, chama as funções email e senha,
    e adiciona o usuário à lista de usuários.
    """
    nome: str = input("Digite o seu nome: ")
    nome: str = nome.strip()

    while len(nome.split(" ")) < 2:
        nome: str = input("O nome deve ter pelo menos duas palavras. Digite o nome novamente: ")
        nome = nome.strip()

    email: str = digita_email()

    for usuario in usuarios:
        while usuario[1] == email:
            email = input("E-mail já cadastrado. Digite o e-mail novamente: ")

    senha: str = digita_senha()

    termos_uso: str = input("Você aceita os termos de uso? (s/n) ")

    while termos_uso.lower() != "s":
        termos_uso: str = input("Você precisa aceitar os termos de uso para continuar (s): ")

    idade: int = int(input("Digite sua idade: "))

    if idade < 18:
        print("Cadastro permitido apenas para maiores de 18 anos.")
    else:
        usuarios.append([nome, email, senha])
        print("Usuário cadastrado com sucesso!")

def fazer_login() -> None:
    """
    Essa função solicita o e-mail e senha do usuário e,
    caso corresponderem com algum usuário na lista,
    armazena esse usuário na variável do usuario_logado
    """
    global usuario_logado

    if not usuario_logado:
        email = digita_email()
        senha = digita_senha()

        for usuario in usuarios:
            if usuario[1] == email and usuario[2] == senha:
                usuario_logado = usuario
                print(f"Login realizado com sucesso! Bem-vindo, {usuario[0]}.\n")
                return

        print("E-mail ou senha incorretos.\n")
        return

    print("Você já está logado.\n")

def acionar_sinistro() -> None:
    """
    Essa função recebe os dados da bike,
    gera um número de protocolo e inicia
    a vistoria da bike.
    """
    numero_serie: str = input("Qual o número de série da bike? ")
    bike_encontrada = None

    for bike in bikes:
        if bike[0] == numero_serie:
            bike_encontrada = bike

    if not bike_encontrada:
        print("Bike não encontrada.")
    else:
        gravacao: str = input("Digite 'sim' para realizar a gravação da bike: ")

        while gravacao.lower() != "sim":
            gravacao: str = input("Resposta inválida. Digite 'sim' para realizar a gravação da bike: ")

        foto: str = input("Digite 'sim' para enviar a foto da bike: ")

        while foto.lower() != "sim":
            foto = input("Resposta inválida. Digite 'sim' para enviar a foto da bike: ")

        protocolo: int = random.randint(1000, 9999)

        protocolos.append([protocolo, numero_serie])

        print(f"A vistoria da bike foi iniciada. Número do protocolo: {protocolo}")

def cadastrar_bike() -> None:
    """
    Essa função recebe os dados da bike, valida eles,
    e inclui a bike na lista de bikes
    """
    numero_serie: str = input("Digite o número de série: ")

    while len(numero_serie) < 7:
        numero_serie: str = input("O número de série deve ter no mínimo 7 caracteres. Digite novamente: ")

    modelo: str = input("Digite o modelo: ")

    while modelo == "":
        modelo: str = input("Modelo inválido. Digite o modelo novamente: ")

    nota_fiscal: str = input("Digite o código da nota fiscal: ")

    preco: float = float(input("Digite o preço: "))

    bikes.append([numero_serie, modelo, nota_fiscal, preco])

    print(f"Bike cadastrada com sucesso!")

def cancelar_vistoria() -> None:
    """
    Essa função recebe um número de protocolo,
    procura ele na lista de protocolos, e se encontrá-lo,
    cancela a vistoria.
    """
    protocolo: int =  int(input("Informe o número do protocolo: "))
    motivo = input("Qual foi o motivo do cancelamento? ")



    for i in range(len(protocolos)):
        if protocolos[i][0] == protocolo:
            protocolos.remove(protocolos[i])
            print("Vistoria cancelada com sucesso.")
            return

    print("Número do protocolo não encontrado.")

def sair_da_conta() -> None:
    """
    Essa função muda a variável do usuário logado,
    fazendo um logout
    """
    global usuario_logado
    if usuario_logado:
        usuario_logado = None
        print("Você saiu da conta.\n")
    else:
        print("Você não está logado.\n")

def ver_perfil() -> None:
    """
    Essa função exibe os dados do usuário logado
    """
    if usuario_logado:
        print("\n------ Perfil ------")
        print(f"Nome: {usuario_logado[0]}")
        print(f"E-mail: {usuario_logado[1]}")
        print(f"Senha: {usuario_logado[2]}")
    else:
        print("Você precisa estar logado para ver o perfil.\n")

def status_vistoria():
    """
    Essa função recebe o número de protocolo
    e verifica o status da vistoria
    """
    protocolo: int = int(input("Informe o número do protocolo: "))

    for i in range(len(protocolos)):
        if protocolos[i][0] == protocolo:
            print("Vistoria concluída.")
            return

    print("Número do protocolo não encontrado.")

def relatorio_vistorias() -> None:
    """
    Essa função exibe a lista de vistorias com o
    número do protocolo e número de série da bike
    """
    print("Vistorias: ")
    for p in protocolos:
        print(f"Protocolo: {p[0]} - Número de Série: {p[1]}")

while True:
    mostra_menu()
    numero_menu = int(input("Digite a ação que deseja realizar: "))

    if numero_menu == 1:
        cadastra_usuario()
    elif numero_menu == 2:
        fazer_login()
    elif numero_menu == 3:
        cadastrar_bike()
    elif numero_menu == 4:
        acionar_sinistro()
    elif numero_menu == 5:
        cancelar_vistoria()
    elif numero_menu == 6:
        sair_da_conta()
    elif numero_menu == 7:
        ver_perfil()
    elif numero_menu == 8:
        status_vistoria()
    elif numero_menu == 9:
        relatorio_vistorias()