renda = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))

if parcela <= renda * 0.3 and renda >= 2000:
    print("Empréstimo concedido.")
elif renda < 2000:
    print("Empréstimo negado: renda precisa ser maior que R$2000,00")
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")