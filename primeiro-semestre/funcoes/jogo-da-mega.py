import random

dezenas = []
dezenasSorteadas = []

def pedeDezena():
    numero = int(input("Digite uma dezena de 1 a 60: "))

    while numero < 1 or numero > 60:
        numero = int(input("Número inválido. Digite uma dezena de 1 a 60: "))

    while dezenas.count(numero) > 0:
        numero = int(input("Você já digitou esse número. Escolha outro: "))

    dezenas.append(numero)

def sorteiaDezenas():
    dezenaSorteada = random.randint(1, 60)

    while dezenasSorteadas.count(dezenaSorteada) > 0:
        dezenaSorteada = random.randint(1, 60)

    dezenasSorteadas.append(dezenaSorteada)

def ordenaListas(dezenas, dezenasSorteadas):
    dezenas = dezenas.sort()
    dezenasSorteadas = dezenasSorteadas.sort()

for i in range(6):
    pedeDezena()
    sorteiaDezenas()

ordenaListas(dezenas, dezenasSorteadas)

print(dezenas, dezenasSorteadas)

def comparaDezenas():
    iguais = [dezena for dezena in dezenas if dezena in dezenasSorteadas]
    print(f"Você acertou {len(iguais)} números!")

comparaDezenas()