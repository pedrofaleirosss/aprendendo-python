nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    print(f"A média das notas é: {(nota1 + nota2) / 2}")
else:
    print("Uma das notas não é válida.")