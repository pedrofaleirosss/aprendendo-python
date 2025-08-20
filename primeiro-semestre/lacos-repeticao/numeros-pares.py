numeros_pares = 0

for i in range (1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))

    if numero % 2 == 0:
        numeros_pares += 1

print(f"Você digitou {numeros_pares} números pares.")