import re

# Exercício 1 - Ajustando nomes de produtos

# nome_produto = input("Digite o nome do produto: ").strip().lower()

# print(nome_produto)

# Exercício 2 - Formatando uma saudação

# nome = input("Digite o nome do cliente: ")
# cidade = input("Digite a cidade do cliente: ")

# print(f"Olá, {nome}! Bem-vindo(a) ao sistema da cidade de {cidade}.")

# Exercício 3 - Decifrando pistas com palavras-chave

# palavra = input("Digite a palavra-chave: ")

# print(f"Primeiras: {palavra[:3]}")
# print(f"Últimas: {palavra[-3:]}")

# Exercício 4 - Verificando o início e o fim de uma String

# url = input("Digite a URL para validação: ")

# if url.startswith("https://") and url.endswith(".com"):
#     print("URL válida")
# else: 
#     print("URL inválida")

# Exercício 5 - Encontrando números em um texto

# descricao = input("Digite a descrição da receita: ")
# numero = re.findall(r'\d+', descricao)[0]
# print(f"O número da receita é: {numero}")

# Exercício 6 - Substituindo palavras específicas

# texto = input("Digite o texto a ser revisado: ")
# substituir = input("Qual palavra deseja substituir? ")
# nova = input("Qual a nova palavra? ")

# texto_revisado = re.sub(rf'\b{substituir}\b', nova, texto)
# print(texto_revisado)
 
# Exercício 7 - Validando nomes com Regex

# nome = input("Digite o nome do cliente para validação: ")
# if re.fullmatch(r'[A-Z][a-z]*', nome):
#     print("Nome válido")
# else:
#     print("Nome inválido")

# Exercício 8 - Verificando o formato de um CPF

# cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

# if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
#     print("O CPF está no formato correto.")
# else:
#     print("O CPF está no formato incorreto.")

# Exercício 9 - Encontrando palavras que começam com uma letra específica

# titulo = input("Digite o título: ")
# letra = input("Digite a letra inicial para pesquisa: ")

# palavras = re.findall(rf'\b{letra}\w*', titulo, re.IGNORECASE)

# print(palavras)

# Exercício 10 - Agrupando informações dos pacientes

# infos = input("Digite o nome completo e o ano de nascimento do paciente: ")
# padrao = r'(\w+) (\w+) - (\d{4})'

# resultado = re.search(padrao, infos)

# if resultado:
#     nome = resultado.group(1)
#     sobrenome = resultado.group(2)
#     ano_nascimento = resultado.group(3)

#     print(f"Nome: {nome}")
#     print(f"Sobrenome: {sobrenome}")
#     print(f"Ano de Nascimento: {ano_nascimento}")
# else:
#     print("Informações inválidas.")