numero = 0

while numero < 1 or numero > 10:
    numero = int(input("Digite um número inteiro de 1 a 10: "))
    if numero < 1 or numero > 10:
        print("O número deve ser de 1 a 10!")

for i in range (1, 11):
    if numero == i:
        print(f"O número digitado foi: {i}")
        break

for i in range (10):
    if i % 3 == 0:
        continue 
    print(i)