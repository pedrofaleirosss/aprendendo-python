nota1 = float(input("Digite a nota do trabalho de laboratório (peso 2): "))
nota2 = float(input("Digite a nota da avaliação semestral (peso 3): "))
nota3 = float(input("Digite a nota do exame final (peso 5): "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

print(f"A média é: {media:.2f}")

if media < 4:
    print("Reprovado.")
elif 4 <= media < 6:
    print("Recuperação.")
else:
    print("Aprovado.")