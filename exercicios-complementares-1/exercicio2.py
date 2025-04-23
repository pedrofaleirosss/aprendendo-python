numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2} e a diferença entre eles é: {numero1 - numero2}.")
elif numero1 == numero2:
    print("Os números são iguais e a diferença entre eles é 0.")
else:
    print(f"O número {numero2} é maior que o número {numero1} e a diferença entre eles é: {numero2 - numero1}.")