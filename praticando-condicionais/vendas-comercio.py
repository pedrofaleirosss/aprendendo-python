qtdMacas = int(input("Digite a quantidade de maçãs vendidas: "))
qtdBananas = int(input("Digite a quantidade de bananas vendidas: "))

if qtdMacas > qtdBananas:
    print("As maçãs tiveram mais vendas.")
elif qtdMacas == qtdBananas:
    print("As maçãs e bananas tiveram a mesma quantidade de vendas.")
else:
    print("As bananas tiveram mais vendas.")