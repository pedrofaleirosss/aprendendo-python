# Exercício 1

# def somar(num1: float, num2: float) -> float:
#     """
#     Essa função recebe dois números float e retorna a soma deles
#     """
#     return num1 + num2
#
# num1: float = float(input("Digite o número 1: "))
# num2: float = float(input("Digite o número 2: "))
#
# print(f"A soma dos números é {somar(num1, num2)}")

# Exercício 2

# def quadrado(numero: int) -> int:
#     """
#     Essa função recebe um número inteiro e retorna o resultado desse número ao quadrado
#     """
#     return numero**2
#
# numero: int = int(input("Digite um número: "))
#
# print(f"O número {numero}² é igual a {quadrado(numero)}")

# Exercício 3

# def soma_dos_quadrados(num1: int, num2: int) -> int:
#     """
#     Essa função recebe dois números inteiros e retorna a soma dos seus quadrados
#     """
#     return quadrado(num1) + quadrado(num2)
#
# num1: int = int(input("Digite o número 1: "))
# num2: int = int(input("Digite o número 2: "))
#
# print(f"A soma de {num1}² e {num2}² é {soma_dos_quadrados(num1, num2)}")

# Exercício 4

# def media(num1: float, num2: float, num3: float) -> float:
#     """
#     Essa função recebe 3 números float e retorna a média aritmética deles.
#     """
#     return (num1 + num2 + num3) / 3
#
# num1: float = float(input("Digite o número 1: "))
# num2: float = float(input("Digite o número 2: "))
# num3: float = float(input("Digite o número 3: "))
#
# print(f"A média aritmética dos números é {media(num1, num2, num3)}")

# Exercício 5

# def calcular_salario(salario_atual: float) -> float:
#     """
#     Essa função recebe o salário atual de um funcionário em float e retorna
#     o salário em float com um reajuste de aumento sendo que caso o salário
#     seja maior que R$2000,00 o funcionário recebe 7% de aumento, senão recebe 15%
#     """
#     if salario_atual > 2000:
#         return salario_atual * 1.07
#     else:
#         return salario_atual * 1.15
#
# salario_atual: float = float(input("Digite o seu salário atual: "))
#
# print(f"Seu novo salário é R${calcular_salario(salario_atual):.2f}")

# Exercício 6

# def soma_divisores(numero: int) -> int:
#     """
#     Essa função recebe um número positivo int e retorna a soma de todos os seus divisores em int
#     """
#     soma: int = 0
#     for num in range(1, numero + 1):
#         if numero % num == 0:
#             soma = soma + num
#
#     return soma
#
# numero: int = int(input("Digite um número: "))
#
# print(f"A soma de todos os divisores de {numero} é {soma_divisores(numero)}")