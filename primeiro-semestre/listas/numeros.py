numeros = [2, 0, 4, 18, 13]

soma = 0
num_maior = ""
num_menor = ""

for i in range(len(numeros)):
    # Calcula soma
    soma += numeros[i]

    # Calcula maior número
    if num_maior != "":
        if numeros[i] > num_maior:
            num_maior = numeros[i]
    else:
        num_maior = numeros[i]

    # Calcula menor número
    if num_menor != "":
        if numeros[i] < num_menor:
            num_menor = numeros[i]
    else:
        num_menor = numeros[i]

print(f"O somatório é {soma}")

if soma > 0:
    # Calcula média
    media = soma / len(numeros)
    print(f"A média é {media}")

print(f"O maior número é {num_maior}")
print(f"O menor número é {num_menor}")