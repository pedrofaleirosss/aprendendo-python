nota1 = float(input("Digite a nota 1 (peso 1): "))
nota2 = float(input("Digite a nota 2 (peso 1): "))
nota3 = float(input("Digite a nota 3 (peso 2): "))

media = (nota1 + nota2 + (nota3 * 2)) / 4

print(f"A média é: {media:.2f}")

if media >= 6:
    print("Aprovado.")
else:
    print("Reprovado.")