# Exercício 1

# def mostrar_informacoes(nome: str, idade: int, cidade: str) -> None:
#     """
#     Essa função recebe 3 parâmetros, nome, idade e cidade e imprimi
#     uma mensagem com essas informações
#     """
#     print(f"Olá {nome}. Você tem {idade} anos e mora em {cidade}.")
#
# mostrar_informacoes(cidade = "Atibaia", idade = 18, nome = "Pedro")

# Exercício 2

# def calcular_area_retangulo(base: float = 1, altura: float = 1) -> float:
#     """
#     Essa função recebe a base e a altura de um retângulo em float
#     e retorna a área desse retângulo em float
#     """
#     return base * altura
#
# print(f"A área do retângulo é {calcular_area_retangulo(5, 4)}")
# print(f"A área do retângulo é {calcular_area_retangulo()}")

# Exercício 3

# def soma(a: float, b: float) -> float:
#     """
#     Essa função recebe 2 valores, a e b, do tipo flaot,
#     e retorna a soma deles em float
#     """
#     return a + b
#
# print(soma(3, 7))

# Exercício 4

# def enviar_email(destinatario: str, assunto: str = "Sem assunto", corpo: str = "") -> None:
#     """
#     Essa função recebe 3 parâmetros string: destinatário, assunto e corpo.
#     Assunto e corpo possuem valores padrão.
#     A função imprimi as informações formatadas.
#     """
#     print(f"Destinatário: {destinatario}\nAssunto: {assunto}\nCorpo: {corpo}")
#
# enviar_email("Pedro", "Saudações", "Olá Pedro")
# enviar_email("Pedro")

# Exercício 5

# def concatenar_strings(string1: str, string2: str, separador: str = " ") -> str:
#     """
#     Essa função recebe duas strings e um
#     separador (que tem como valor padrão uma string de espaço " ").
#     Ela retorna as duas strings concatenadas com o separador entre elas.
#     """
#     return string1 + separador + string2
#
# print(concatenar_strings("Bom", "dia"))

# Exercício 6

# def comprar_produto(produto: str = "Produto desconhecido", quantidade: int = 1) -> str:
#     """
#     Essa função recebe um produto em str e uma quantidade em int e retorna
#     uma mensagem indicando a compra do produto na quantidade especificada.
#     Os dois parâmetros têm valores padrão.
#     """
#     return f"Sua compra foi: Produto: {produto} - Quantidade: {quantidade}"
#
# print(comprar_produto(quantidade = 3, produto = "Bolacha"))
# print(comprar_produto())

# Exercício 7

# def imprime_lista(itens: list) -> None:
#     """
#     Essa função recebe um parâmetro itens que é uma lista de strings.
#     Ela imprime cada item da lista em linhas separadas.
#     """
#     for item in itens:
#         print(item)
#
# imprime_lista(["Item 1", "Item 2", "Item 3"])