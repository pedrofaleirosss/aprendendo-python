numeros = [2, 8, 3, 6, 9, 4]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"O mínimo número par é {min(pares)}")
print(f"O máximo número ímpar é {max(impares)}")