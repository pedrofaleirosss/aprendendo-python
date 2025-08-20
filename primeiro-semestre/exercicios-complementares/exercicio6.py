salario = float(input("Digite o salário: "))
prestacao = float(input("Digite o valor da prestação: "))

if prestacao > salario * 0.2:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")