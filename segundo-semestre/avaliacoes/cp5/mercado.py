# RM: 562523 - Pedro Alves Faleiros
# Simples sistema de mercado com cadastro de produtos, usuários, login, compra e histórico de compras.

from datetime import datetime

usuario_logado = None

def mostra_menu() -> None:
    """Mostra o menu de opções para o usuário."""
    print("--------------- Menu ---------------")
    print("[1] Cadastrar produto")
    print("[2] Editar produtos")
    print("[3] Listar produtos")
    print("[4] Cadastrar usuário")
    if not usuario_logado:
        print("[5] Fazer Login")
    else:
        print("[5] Sair da conta")
    if usuario_logado:
        print("[6] Consultar conta")
        print("[7] Adicionar saldo")
        print("[8] Comprar produtos")
        print("[9] Ver histórico de compras")
    print("[0] Sair")

def cadastrar_produto() -> None:
    """Pede ao usuário o nome e o preço do produto e salva em um arquivo."""

    nome: str = input("Nome do produto: ")

    try:
        preco: float = float(input("Preço do produto: "))
    except ValueError:
        print("Preço inválido. Tente novamente.")
        return
    
    try:
        quantidade: int = int(input("Quantidade do produto: "))
        if quantidade < 1:
            raise ValueError
    except ValueError:
        print("Quantidade inválida. Tente novamente.")
        return

    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - R${preco} - {quantidade} unidades\n")

    print("Produto cadastrado com sucesso!\n")

def editar_produtos() -> None:
    """Edita um produto cadastrado, pedindo o índice do produto que deseja editar, novo nome e novo preço."""

    try:
        arquivo = open("produtos.txt", "r", encoding="utf-8")
    except FileNotFoundError:
        print("Nenhum produto cadastrado. Cadastre um produto primeiro.\n")
        return

    produtos: list[str] = arquivo.readlines()
    arquivo.close()

    print("\nProdutos cadastrados:")

    for i, produto in enumerate(produtos):
        print(f"[{i}] {produto.strip()}")

    indice: int = int(input("\nDigite o índice do produto que deseja editar: "))
    novo_nome: str = input("Novo nome do produto: ")
    novo_preco: float = float(input("Novo preço do produto: "))
    try:
        nova_quantidade: int = int(input("Nova quantidade do produto: "))
    except ValueError:
        print("Quantidade inválida. Tente novamente.")
        return

    produtos[indice] = f"{novo_nome} - R${novo_preco} - {nova_quantidade} unidades\n"

    with open("produtos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(produtos)

    print("Produto editado com sucesso!\n")

def listar_produtos() -> None:
    """Lista todos os produtos cadastrados, mostrando o total de produtos e o preço total."""

    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            produtos = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhum produto cadastrado. Cadastre um produto primeiro.\n")
        return

    print("\n--------------- Produtos Cadastrados ---------------\n")
    for produto in produtos:
        print(produto.strip())
    print()

def cadastrar_usuario() -> None:
    """Pede ao usuário nome completo, data de nascimento,
    agencia, conta, saldo e senha de acesso e salva em um arquivo."""

    nome: str = input("Nome completo: ")

    data_nascimento: str = input("Data de nascimento (DD/MM/AAAA): ")
    try:
        dia, mes, ano = map(int, data_nascimento.split("/"))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 1900:
            pass
    except (ValueError, AssertionError):
        print("Data de nascimento inválida. Tente novamente.\n")
        return

    agencia: str = input("Agência: ")
    conta: str = input("Conta: ")

    try:
        saldo: float = float(input("Saldo: "))
    except ValueError:
        print("Saldo inválido. Tente novamente.\n")
        return
    
    try:
        senha: str = input("Senha de acesso: ")
        if len(senha) < 6:
            raise ValueError
    except ValueError:
        print("Senha inválida. Tente novamente. A senha deve ter pelo menos 6 caracteres.\n")
        return

    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} | {data_nascimento} | {agencia} | {conta} | R${saldo} | {senha}\n")

    print("Usuário cadastrado com sucesso!\n")

def fazer_login() -> None:
    """Realiza o login de um usuário cadastrado, verificando nome e senha."""
    global usuario_logado

    nome: str = input("Nome completo: ")
    senha: str = input("Senha de acesso: ")

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            usuarios: list[str] = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.\n")
        return

    for usuario in usuarios:
        if usuario.startswith(nome) and senha in usuario:
            usuario_logado = nome
            print("Login realizado com sucesso!\n")
            return

    print("Login falhou. Nome ou senha incorretos.\n")

def sair_da_conta() -> None:
    """Desloga o usuário atual."""
    global usuario_logado
    usuario_logado = None
    print("Você saiu da conta com sucesso.\n")

def consultar_conta() -> None:
    """Consulta os dados da conta do usuário logado."""
    global usuario_logado

    if not usuario_logado:
        print("Você precisa estar logado para consultar sua conta.\n")
        return

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            usuarios: list[str] = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.\n")
        return

    for usuario in usuarios:
        if usuario.startswith(usuario_logado):
            print("\n--------------- Dados da Conta ---------------")
            print(usuario.strip())
            print(f"Saldo: R${usuario.split(' | ')[4][2:]}\n")
            return

    print("Usuário não encontrado.\n")

def adicionar_saldo() -> None:
    """Adiciona saldo à conta do usuário logado."""
    global usuario_logado

    if not usuario_logado:
        print("Você precisa estar logado para adicionar saldo à sua conta.\n")
        return

    try:
        valor: float = float(input("Digite o valor a ser adicionado: R$"))
        if valor <= 0:
            raise ValueError
    except ValueError:
        print("Valor inválido. Tente novamente.\n")
        return

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            usuarios: list[str] = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.\n")
        return

    for i, usuario in enumerate(usuarios):
        if usuario.startswith(usuario_logado):
            dados: list[str] = usuario.strip().split(" | ")
            saldo_atual: float = float(dados[4][2:])
            novo_saldo: float = saldo_atual + valor
            usuarios[i] = f"{dados[0]} | {dados[1]} | {dados[2]} | {dados[3]} | R${novo_saldo:.2f} | {dados[5]}\n"
            break

    with open("usuarios.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(usuarios)

    print(f"Saldo adicionado com sucesso! Novo saldo: R${novo_saldo:.2f}\n")

def comprar_produtos() -> None:
    """Permite que o usuário logado compre produtos."""
    global usuario_logado

    if not usuario_logado:
        print("Você precisa estar logado para comprar produtos.\n")
        return

    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            produtos: list[str] = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhum produto cadastrado. Cadastre um produto primeiro.\n")
        return

    print("\n--------------- Produtos Disponíveis ---------------")
    for i, produto in enumerate(produtos):
        print(f"[{i}] {produto.strip()}")
    print("----------------------------------------------------")

    try:
        produto_id: int = int(input("Digite o ID do produto que deseja comprar: "))
        quantidade: int = int(input("Digite a quantidade que deseja comprar: "))
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")
        return
    
    if produto_id < 0 or produto_id >= len(produtos):
        print("ID do produto inválido. Tente novamente.\n")
        return
    
    if quantidade < 1:
        print("Quantidade inválida. Tente novamente.\n")
        return

    preco_total: float = float(produtos[produto_id].split(" - R$")[1].split(" - ")[0]) * quantidade

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            usuarios: list[str] = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.\n")
        return

    for usuario in usuarios:
        if usuario.startswith(usuario_logado):
            dados: list[str] = usuario.strip().split(" | ")
            saldo_atual: float = float(dados[4][2:])
            break
    else:
        print("Usuário não encontrado.\n")
        return

    if saldo_atual < preco_total:
        print("Saldo insuficiente para realizar a compra.\n")
        return
    
    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        nome_produto, preco_produto, quantidade_produto = produtos[produto_id].strip().split(" - ")
        quantidade_disponivel: int = int(quantidade_produto.split(" ")[0])
        nova_quantidade: int = quantidade_disponivel - quantidade
        try:
            if nova_quantidade < 0:
                raise ValueError
        except ValueError:
            print("Quantidade indisponível em estoque. Tente novamente.\n")
            return

    
    with open("produtos.txt", "w", encoding="utf-8") as arquivo:
        nome_produto, preco_produto, quantidade_produto = produtos[produto_id].strip().split(" - ")
        quantidade_disponivel: int = int(quantidade_produto.split(" ")[0])
        nova_quantidade: int = quantidade_disponivel - quantidade
        produtos[produto_id] = f"{nome_produto} - {preco_produto} - {nova_quantidade} unidades\n"
        arquivo.writelines(produtos)

    novo_saldo: float = saldo_atual - preco_total
    for i, usuario in enumerate(usuarios):
        if usuario.startswith(usuario_logado):
            usuarios[i] = f"{dados[0]} | {dados[1]} | {dados[2]} | {dados[3]} | R${novo_saldo:.2f} | {dados[5]}\n"
            break

    with open("usuarios.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(usuarios)

    with open("vendas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{usuario_logado} comprou {quantidade} unidades de {nome_produto} por R${preco_total:.2f} na data {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print(f"Compra realizada com sucesso! Você comprou {quantidade} unidades do produto {nome_produto} por R${preco_total:.2f}.\n")

def ver_historico_compras() -> None:
    """Mostra o histórico de compras do usuário logado."""
    global usuario_logado

    if not usuario_logado:
        print("Você precisa estar logado para ver seu histórico de compras.\n")
        return

    try:
        with open("vendas.txt", "r", encoding="utf-8") as arquivo:
            vendas: list[str] = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhuma compra realizada ainda.\n")
        return

    print("\n--------------- Histórico de Compras ---------------")
    # se o usuário nao tiver compras, mostrar mensagem
    tem_compras: bool = False
    for venda in vendas:
        if venda.startswith(usuario_logado):
            print(venda.strip())
            tem_compras = True
    if not tem_compras:
        print("Nenhuma compra realizada até o momento.")
    print()

while True:
    mostra_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        editar_produtos()
    elif opcao == "3":
        listar_produtos()
    elif opcao == "4":
        cadastrar_usuario()
    elif opcao == "5" and not usuario_logado:
        fazer_login()
    elif opcao == "5" and usuario_logado:
        sair_da_conta()
    elif opcao == "6" and usuario_logado:
        consultar_conta()
    elif opcao == "7" and usuario_logado:
        adicionar_saldo()
    elif opcao == "8" and usuario_logado:
        comprar_produtos()
    elif opcao == "9" and usuario_logado:
        ver_historico_compras()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
