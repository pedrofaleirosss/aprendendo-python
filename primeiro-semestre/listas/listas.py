# Imprimir a lista de trás para frente usando índices negativos

nomes = ["Paulo", "Ana", "Pedro", "Maria"]

for i in range(-1, (len(nomes) * -1) - 1, -1):
    print(nomes[i])
