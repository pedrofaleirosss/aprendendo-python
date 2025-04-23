lado_a = int(input("Digite o valor do lado A: "))
lado_b = int(input("Digite o valor do lado B: "))
lado_c = int(input("Digite o valor do lado C: "))

if lado_a < (lado_b + lado_c) and lado_b < (lado_a + lado_c) and lado_c < (lado_a + lado_b):
    print("São lados de um triângulo!")
else:
    print("Não são lados de um triângulo.")