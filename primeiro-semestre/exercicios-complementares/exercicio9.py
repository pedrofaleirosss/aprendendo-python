base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))

if base_maior > 0 and base_menor > 0 and altura > 0:
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {area}")
else:
    print("Um dos valores não é maior que zero.")