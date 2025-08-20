import random

print("--------------- Jogo de Dados ---------------")
print("Tente acertar a soma de dois dados.")

matrizSomas = []

for i in range(1, 7):
    for n in range(1, 7):
        matrizSomas.append(n + i)

def pedeNumero():
    numero = int(input("Digite um número de 2 a 12: "))

    while numero < 2 or numero > 12:
        numero = int(input("Número inválido. Digite um número de 2 a 12: "))

    return numero

numero = pedeNumero()

def verificaProbabilidade(numero):
    numeroOcorrencias = matrizSomas.count(numero)
    probabilidade = numeroOcorrencias / 36
    print(f"A probabilidade de acerto é {numeroOcorrencias}/36 ou {(probabilidade * 100):.2f}%")

verificaProbabilidade(numero)

def sorteiaDados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

somaDados = sorteiaDados()

if somaDados == numero:
    print(f"Parabéns. Você ganhou! A soma dos dados é {somaDados}.")
else:
    print(f"Você perdeu. A soma dos dados é {somaDados}.")