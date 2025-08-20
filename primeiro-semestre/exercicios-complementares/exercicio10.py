operacao = input("Digite a operação desejada (+, -, *, /): ")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

'''
if operacao == "+":
    print(f"{num1} {operacao} {num2} é: {num1 + num2}")
elif operacao == "-":
    print(f"{num1} {operacao} {num2} é: {num1 - num2}")
elif operacao == "*":
    print(f"{num1} {operacao} {num2} é: {num1 * num2}")
elif operacao == "/":
    print(f"{num1} {operacao} {num2} é: {num1 / num2}")
else:
    print("Operação inválida.")
'''

match operacao:
    case "+":
        print(f"{num1} mais {num2} é: {num1 + num2}")
    case "-":
        print(f"{num1} menos {num2} é: {num1 - num2}")
    case "*":
        print(f"{num1} vezes {num2} é: {num1 * num2}")
    case "/":
        if num2 == 0:
            print("O segundo número não pode ser 0.")
        else:
            print(f"{num1} dividido por {num2} é: {(num1 / num2):.2f}")
    case _:
        print("Operação inválida.")
