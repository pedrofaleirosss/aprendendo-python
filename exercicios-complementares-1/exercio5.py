numero = input("Digite um número: ")

numero_reverso = numero[::-1]

print(numero)
print(numero_reverso)

if numero == numero_reverso:
    print("O número é capicua.")
else:
    print("O número não é capicua.")