# Exercício 1

# texto = input("Digite um texto para contagem de palavras: ")
# contagem_palavras = {}
#
# lista_palavras = texto.split(" ")
#
# for palavra in lista_palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] = contagem_palavras[palavra] + 1
#     else:
#         contagem_palavras[palavra] = 1
#
# print(contagem_palavras)

# Exercício 2

# alunos = []
#
# for i in range(3):
#     nome = input("Digite o nome do aluno: ")
#     idade = int(input("Digite a idade do aluno: "))
#     nota = float(input("Digite a nota do aluno: "))
#     alunos.append((nome, idade, nota))
#
# nomes_aprovados = []
#
# def alunos_aprovados(lista_alunos: list) -> list:
#     for aluno in lista_alunos:
#         if aluno[2] >= 7:
#             nomes_aprovados.append(aluno[0])
#
#     return nomes_aprovados
#
# print(alunos_aprovados(alunos))

# Exercício 3

# produtos = {}
#
# for i in range(3):
#     print("---------- Cadastro de Produto ----------------")
#     nome_produto = input("Digite o nome do produto: ")
#     preco = float(input("Digite o preço do produto: "))
#     quantidade = int(input("Digite a quantidade desse produto no estoque: "))
#     produtos[nome_produto] = (preco, quantidade)
#
# def total_valor_estoque():
#     valores_totais = []
#     for produto in produtos:
#         valores_totais.append([produto, f"Valor total do estoque: {produtos[produto][0] * produtos[produto][1]}"])
#     return valores_totais
#
# print(total_valor_estoque())

# Exercício 4

# usuarios = {}
#
# for i in range(3):
#     cpf = input("Digite o seu CPF: ")
#     nome = input("Digite o seu nome: ")
#     usuarios[cpf] = nome
#
# print(usuarios)

# Exercício 5

# pessoas = {}
#
# for i in range(3):
#     cpf = input("Digite o seu CPF: ")
#     nome = input("Digite o seu nome: ")
#     idade = int(input("Digite a sua idade: "))
#     cidade = input("Digite a sua cidade: ")
#     print("-----------------------")
#     pessoas[cpf] = {"nome": nome, "idade": idade, "cidade": cidade}
#
# def pessoas_cidade(cidade_escolhida: str) -> list:
#     pessoas_da_cidade = []
#
#     for pessoa in pessoas:
#         if pessoas[pessoa]["cidade"] == cidade_escolhida:
#             pessoas_da_cidade.append(pessoas[pessoa]["nome"])
#
#     return pessoas_da_cidade
#
# print(pessoas_cidade("Atibaia"))