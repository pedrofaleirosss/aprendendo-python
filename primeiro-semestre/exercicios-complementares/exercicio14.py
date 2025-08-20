a = float(input("Digite o valor a: "))
b = float(input("Digite o valor b: "))
c = float(input("Digite o valor c: "))

if a <= b <= c:
    print("Estão em ordem crescente.")
elif  a >= b >= c:
    print("Estão em ordem decrescente.")
else:
    print("Estão desordenados")