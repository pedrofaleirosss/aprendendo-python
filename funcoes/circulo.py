def area(r):
    return 3.14 * r**2

def perimetro(r):
    return 3.14 * 2 * r

raio = float(input("Digite o raio do círculo (cm): "))

print(f"A área do círculo é {area(raio):.2f} cm²")
print(f"O perímetro do círculo é {perimetro(raio):.2f} cm²")