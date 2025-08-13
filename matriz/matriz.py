import random

# Exercício 1

# matriz = []
# for m in range(3):
#     linha = []
#     for n in range(5):
#         numero = int(input("Digite um número inteiro: "))
#         linha.append(numero)
#     matriz.append(linha)
#
# print(matriz)

# Exercício 2

# matriz = []
# for m in range(3):
#     linha = []
#     for n in range(4):
#         numero = int(input("Digite um número: "))
#         linha.append(numero)
#     matriz.append(linha)
#
# print("Matriz normal: ")
# print(matriz)
#
# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[0])):
#         if matriz[linha][coluna] > 100:
#             matriz[linha][coluna] = 0
#
# print("Matriz com os valores maiores que 100 alterados para 0: ")
# print(matriz)

# Exercício 3

# matriz = []
# soma = 0
#
# for m in range(5):
#     linha = []
#     for n in range(5):
#         numero = random.randint(1, 10)
#         linha.append(numero)
#     matriz.append(linha)
#
# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         if linha == coluna:
#             soma += matriz[linha][coluna]
#
# print(matriz)
# print("Somatório dos elementos da diagonal principal: ", soma)

# Exercício 4

# matriz = []
# menor_elemento = 100
#
# for m in range(5):
#     linha = []
#     for n in range(5):
#         numero = random.randint(1, 100)
#         linha.append(numero)
#     matriz.append(linha)
#
# print(matriz)
#
# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         if coluna != len(matriz[linha]) - 1:
#             if matriz[linha][coluna] < menor_elemento:
#                 menor_elemento = matriz[linha][coluna]
#
# print("O menor elemento da matriz é: ", menor_elemento)

# Exercício 5

# matriz = []
# 
# for m in range(5):
#     linha = []
#     for n in range(4):
#         numero = int(input("Digite um número inteiro: "))
#         linha.append(numero)
#     matriz.append(linha)
# 
# print(matriz)
# 
# numero = int(input("Digite um número para buscar na matriz: "))
# posicoes = []
# 
# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         if numero == matriz[linha][coluna]:
#             posicoes.append([linha, coluna])
# 
# if len(posicoes) == 0:
#     print("Número não encontrado na matriz.")
# else:
#     print(f"O número digitado se encontra nas seguintes posições: {posicoes}")