numero = int(input("Digite um número entre 0 e 1000: "))

if 0 < numero < 1000:
    centena = (numero) // 100
    print(centena)
    dezena = (numero - (centena * 100)) // 10
    print(dezena)
    unidade = (numero - (centena * 100) - (dezena * 10))
    print(unidade)

    print(f"A soma dos algarismos é: {centena + dezena + unidade}.")
else:
    print("Número inválido.")