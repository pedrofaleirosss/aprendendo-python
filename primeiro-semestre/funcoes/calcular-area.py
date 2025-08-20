def calcular_area(base, altura):
    area = (base * altura) / 2
    print(f"A área do triângulo é {area}")

base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

calcular_area(base, altura)