# Exercício 1

# arquivo = open("./segundo-semestre/arquivos-texto/numeros.txt", "a")

# for i in range(10):
#     try:
#         num = int(input("Digite um número inteiro: "))
#         arquivo.write(str(num) + '\n')
#     except TypeError:
#         print("Número inválido.")
#     except ValueError:
#         print("Número inválido.")

# arquivo.close()

# Exercício 2

# try:
#     arquivo = open("./segundo-semestre/arquivos-texto/numeros.txt", "r")
# except FileNotFoundError:
#     print("Arquivo numeros.txt não encontrado.")
# else:
#     soma = 0

#     for numero in arquivo:
#         soma += int(numero)

#     print(f"A soma dos números é {soma}")

#     arquivo.close()

# Exercício 3

# arquivo = open("./segundo-semestre/arquivos-texto/arquivo.txt", "a")

# caractere = ""

# while caractere != "0":
#     try:
#         caractere = input("Digite um caractere: ")
#         if len(caractere) > 1 or len(caractere) < 1:
#             raise TypeError
#         arquivo.write(caractere + "\n")
#     except TypeError:
#         print("Caractere inválido.")

# arquivo.close()

# Exercício 4

# pares = open("./segundo-semestre/arquivos-texto/pares.txt", "a")
# impares = open("./segundo-semestre/arquivos-texto/impares.txt", "a")

# numero = ""

# while numero != 0:
#     try:
#         numero = int(input("Digite um número: "))
#         if numero % 2 == 0:
#             pares.write(str(numero) + "\n")
#         else:
#             impares.write(str(numero) + "\n")
#     except ValueError:
#         print("Número inválido.")
#     except TypeError:
#         print("Número inválido")

# pares.close()
# impares.close()

# Exercício 5

# try:
#     pares = open("./segundo-semestre/arquivos-texto/pares.txt", "r")
#     impares = open("./segundo-semestre/arquivos-texto/impares.txt", "r")
#     numeros_ordem = open("./segundo-semestre/arquivos-texto/numeros-em-ordem.txt", "w")
# except FileNotFoundError:
#     print("Algum dois arquivos não foi encontrado.")
# else:
#     lista_numeros = []

#     for num in pares:
#         lista_numeros.append(int(num))

#     for num in impares:
#         lista_numeros.append(int(num))

#     lista_numeros.sort()
#     print(lista_numeros)

#     for num in lista_numeros:
#         numeros_ordem.write(str(num) + "\n")

#     pares.close()
#     impares.close()
#     numeros_ordem.close()
