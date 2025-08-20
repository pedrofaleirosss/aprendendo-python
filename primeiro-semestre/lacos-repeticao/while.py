# x = 0
# numeros_pares = 0

# while x < 10:
#     numero = int(input("Digite um número: "))

#     if numero % 2 == 0:
#         numeros_pares += 1
#     x += 1

# print(f"Você digitou {numeros_pares} números pares.")

# media = float(input("Digite a média: "))

# while media < 0 or media > 10:
#     print("Média inválida.")
#     media = float(input("Digite novamente: "))

# if media < 6:
#     print("Reprovado.")
# else:
#     print("Aprovado.")

# i = 1
# somador = 0

# while i <= 10:
#     somador += i
#     i += 1
# print(f"A soma dos números é {somador}")

# print("------------ Tabuada --------------")

# numero = int(input("Digite um número: "))
# cont = 1

# while cont <= 10:
#     print(f"{numero} vezes {cont} é {numero * cont}")
#     cont += 1

# print("Cachorro-quente | 100 | R$13,20")
# print("Hambúrguer | 101 | R$19,90")
# print("Chesseburguer | 102 | R$21,90")
# print("Suco Natural | 103 | R$7,00")
# print("Refrigerante | 104 | R$6,50")

# cont = 0

# x = 1

# quantidade_cq = 0
# quantidade_h = 0
# quantidade_c = 0
# quantidade_s = 0
# quantidade_r = 0

# while x == 1:
#     codigo = int(input("Informe o código do produto: "))

#     match codigo:
#         case 100:
#             quantidade_cq = int(input("Informe a quantidade: "))
#         case 101:
#             quantidade_h = int(input("Informe a quantidade: "))
#         case 102:
#             quantidade_c = int(input("Informe a quantidade: "))
#         case 103:
#             quantidade_s = int(input("Informe a quantidade: "))
#         case 104:
#             quantidade_r = int(input("Informe a quantidade: "))
#         case _:
#             print("Código inválido.")
#     x = int(input("Deseja mais alguma coisa? Sim - 1 / Não - 2:  "))

# preco_total = 0

# if quantidade_cq > 0:
#     preco_cq = quantidade_cq * 13.2
#     print(f"\n{quantidade_cq} cachorros quentes por R${preco_cq:.2f}")
#     preco_total += preco_cq

# if quantidade_h > 0:
#     preco_h = quantidade_h * 19.9
#     print(f"\n{quantidade_h} hambúrgueres por R${preco_h:.2f}")
#     preco_total += preco_h

# if quantidade_c > 0:
#     preco_c = quantidade_c * 21.9
#     print(f"\n{quantidade_c} cheeseburgers por R${preco_c:.2f}")
#     preco_total += preco_c

# if quantidade_s > 0:
#     preco_s = quantidade_s * 7
#     print(f"\n{quantidade_s} sucos naturais por R${preco_s:.2f}")
#     preco_total += preco_s

# if quantidade_r > 0:
#     preco_r = quantidade_r * 6.5
#     print(f"\n{quantidade_r} refrigerantes por R${preco_r:.2f}")
#     preco_total += preco_r

# print(f"\nPreço total: R${preco_total:.2f}")

nome = input("Digite o nome: ")

while nome != "Diogo":
    nome = input("Não é seu aniversário. Digite outro nome: ")
print(f"Parabéns {nome}")