# Cadastro de Aluno

nome = input("Digite o nome: ")
rm = input("Digite o RM: ")
senha = input("Digite a senha: ")

# Cadastro de Notas
tentativas = 1

while tentativas <= 3:
    print(f"Tentativa {tentativas} de 3 ")
    senha2 = input("Digite a senha para cadastrar as notas: ")
    if senha == senha2:
        break
    print("Senha incorreta.")
    tentativas += 1

if tentativas == 4:
    print("Tentativas esgotadas. Acesso bloqueado.")
    exit()

cp1 = -1
cp2 = -1
cp3 = -1

while cp1 < 0 or cp1 > 10:
    cp1 = float(input("Informe a nota da CP1: "))
    if cp1 < 0 or cp1 > 10:
        print("O valor da nota deve ser de 1 a 10.")
while cp2 < 0 or cp2 > 10:
    cp2 = float(input("Informe a nota da CP2: "))
    if cp2 < 0 or cp2 > 10:
        print("O valor da nota deve ser de 1 a 10.")
while cp3 < 0 or cp3 > 10:
    cp3 = float(input("Informe a nota da CP3: "))
    if cp3 < 0 or cp3 > 10:
        print("O valor da nota deve ser de 1 a 10.")

sprint1 = -1
sprint2 = -2

while sprint1 < 0 or sprint1 > 10:
    sprint1 = float(input("Informe a nota do sprint 1: "))
    if sprint1 < 0 or sprint1 > 10:
        print("O valor da nota deve ser de 0 a 10.")
while sprint2 < 0 or sprint2 > 10:
    sprint2 = float(input("Informe a nota do sprint 2: "))
    if sprint2 < 0 or sprint2 > 10:
        print("O valor da nota deve ser de 0 a 10.")

if cp1 < cp2 and cp1 < cp3:
    cp1 = 0
elif cp2 < cp1 and cp2 < cp3:
    cp2 = 0
else:
    cp3 = 0

media_cps = (cp1 + cp2 + cp3 + sprint1 + sprint2) / 4
print(f"A média das notas de cp e sprint é {media_cps:.2f}")

media_cps = media_cps * 0.4
nota_minima_gs = (6 - media_cps ) / 0.6

print(f"{nome}, você precisa tirar no mínimo {nota_minima_gs:.2f} na GS para ficar com a média geral mínima de 6.0")