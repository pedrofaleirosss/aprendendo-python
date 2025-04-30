estoque = 5

while estoque > 0:
    print(f"Venda realizada! Estoque restante: {estoque}")
    estoque -= 1
print("Estoque esgotado")

for estoque in range(5, 0, -1):
    print(f"Venda realizada! Estoque restante: {estoque}")
print("Estoque esgotado")