# Recursividade - Exercícios

# Exercício 1

# def soma(n: int) -> int:
#     if n == 1:
#         return 1
#     else:
#         return n + soma(n - 1)
#
# numero = int(input("Digite um número inteiro maior que zero: "))
# print(f"A soma dos números de 1 a {numero} é {soma(numero)}")

# Exercício 2

# def mdc(x: int, y: int) -> int:
#     if x >= y and x % y == 0:
#         return y
#     elif x < y:
#         return mdc(y, x)
#     else:
#         return mdc(x, x % y)
#
# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# print(f"O mdc (máximo divisor comum) dos números {numero1} e {numero2} é {mdc(numero1, numero2)}")

# Exercício 3

# def potenciacao(a: int, b: int) -> int:
#     if b == 0:
#         return 1
#     else:
#         return a * potenciacao(a, b - 1)
#
# base = int(input("Digite a base: "))
# expoente = int(input("Digite o expoente: "))
# print(f"O resultado de {base} elevado a {expoente} é {potenciacao(base, expoente)}")

# Exercício 4

# numeros = [1, 4, 5, 8, 11]
#
# def busca(lista: list, item: int) -> bool:
#     if len(lista) == 0:
#         return False
#     elif lista[0] == item:
#         return True
#     else:
#         return busca(lista[1:], item)
#
# numero = int(input("Digite um número para buscar na lista: "))
# print(f"Número encontrado? -> {busca(numeros, numero)}")

# Exercício 5

# numeros = [1, 3, 3, 3, 4, 7, 9, 9, 12]
#
# def busca(lista: list, num: int) -> int:
#     if len(lista) == 0:
#         return 0
#     elif lista[0] == num:
#         return 1 + busca(lista[1:], num)
#     else:
#         return busca(lista[1:], num)
#
# numero = int(input("Digite o número inteiro que deseja buscar na lista: "))
# print(f"O número {numero} apareceu {busca(numeros, numero)} vezes na lista.")

# Exercício 6
#
# def multiplica(num1: int, num2: int) -> int:
#     if num1 == 0:
#         return 0
#     else:
#         return num2 + multiplica(num1 - 1, num2)
#
# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
#
# print(f"O resultado da multiplicação entre {numero1} e {numero2} é {multiplica(numero1, numero2)}")

# Exercício 7

# numeros = [1, 4, 5, 10, 13]
#
# def somatorio(lista: list) -> int:
#     if len(lista) == 0:
#         return 0
#     else:
#         return lista[0] + somatorio(lista[1:])
#
# print(f"O somatório da lista: {numeros} é {somatorio(numeros)}")

# Exercício 8

# numeros = [1, 4, 5, 10, 13]

# def soma(lista: list) -> int:
#     if len(lista) == 0:
#         return 0
#     elif lista[0] % 2 == 0:
#         return lista[0] + soma(lista[1:])
#     else:
#         return soma(lista[1:])

# print(f"A soma dos números pares da lista: {numeros} é {soma(numeros)}")