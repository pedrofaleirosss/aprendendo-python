# Checkpoint 2 - Computional Thinking Using Python - 1ESPF - 30/04/2025
# Pedro Alves Faleiros - 562523
# Luan Shiba Felix - 565541
# João Pedro Morra Lopes - 565737

print("--------- Vinheria Agnello ---------")
print("Seja bem-vindo!")

endereco = input("Digite o seu endereço: ")
estado = input("Digite a sigla do seu estado (XX): ")

ano_nascimento = int(input("Digite seu ano de nascimento (yyyy): "))

if 2025 - ano_nascimento < 18:
    print("A venda de bebidas alcólicas é proibida para menores de 18 anos!")
    exit()

vinho1_qnt = 7
vinho2_qnt = 4
vinho3_qnt = 2
vinho4_qnt = 9
vinho5_qnt = 5
vinho6_qnt = 10
vinho7_qnt = 1
vinho8_qnt = 12
vinho9_qnt = 8
vinho10_qnt = 7

print("------------------- Menu -------------------")

executa = "sim"
valor_total = 0
historico_pedidos = "Pedidos:\n"

while executa == "sim":
    if vinho1_qnt > 0:
        print(f"Vinho Rosê | Quantidade: {vinho1_qnt} | Preço: R$150,00 | Código: 01")
    if vinho2_qnt > 0:
        print(f"Vinho Tinto | Quantidade: {vinho2_qnt} | Preço: R$100,00 | Código: 02")
    if vinho3_qnt > 0:
        print(f"Vinho Branco | Quantidade: {vinho3_qnt} | Preço: R$120,00 | Código: 03")
    if vinho4_qnt > 0:
        print(f"Vinho Suave | Quantidade: {vinho4_qnt} | Preço: R$85,00 | Código: 04")
    if vinho5_qnt > 0:
        print(f"Vinho Shiba | Quantidade: {vinho5_qnt} | Preço: R$170,00 | Código: 05")
    if vinho6_qnt > 0:
        print(f"Vinho Lopes | Quantidade: {vinho6_qnt} | Preço: R$200,00 | Código: 06")
    if vinho7_qnt > 0:
        print(f"Vinho Faleiros | Quantidade: {vinho7_qnt} | Preço: R$130,00 | Código: 07")
    if vinho8_qnt > 0:
        print(f"Vinho Felix | Quantidade: {vinho8_qnt} | Preço: R$50,00 | Código: 08")
    if vinho9_qnt > 0:
        print(f"Vinho Alves | Quantidade: {vinho9_qnt} | Preço: R$175,00 | Código: 09")
    if vinho10_qnt > 0:
        print(f"Vinho Seco | Quantidade: {vinho10_qnt} | Preço: R$115,00 | Código: 10")

    codigo = int(input("Escolha seu vinho digitando o código (xx): "))

    while codigo < 1 or codigo > 10:
        codigo = int(input("O código digitado não existe. Por favor, digite um código válido: "))

    quantidade = int(input("Digite a quantidade de garrafas que deseja comprar: "))

    while quantidade < 0:
        quantidade = int(input("Quantidade inválida! Digite a quantidade novamente: "))

    match codigo:
        case 1:
            while quantidade > vinho1_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 150
            vinho1_qnt -= quantidade
            historico_pedidos += f"Vinho Rosê | Quantidade: {quantidade} | Preço unitário: R${150:.2f} | Total: R${(quantidade * 150):.2f}\n"
        case 2:
            while quantidade > vinho2_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 100
            vinho2_qnt -= quantidade
            historico_pedidos += f"Vinho Tinto | Quantidade: {quantidade} | Preço unitário: R${100:.2f} | Total: R${(quantidade * 100):.2f}\n"
        case 3:
            while quantidade > vinho3_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 120
            vinho3_qnt -= quantidade
            historico_pedidos += f"Vinho Branco | Quantidade: {quantidade} | Preço unitário: R${120:.2f} | Total: R${(quantidade * 120):.2f}\n"
        case 4:
            while quantidade > vinho4_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 85
            vinho4_qnt -= quantidade
            historico_pedidos += f"Vinho Suave | Quantidade: {quantidade} | Preço unitário: {85:.2f} | Total: R${(quantidade * 85):.2f}\n"
        case 5:
            while quantidade > vinho5_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 170
            vinho5_qnt -= quantidade
            historico_pedidos += f"Vinho Shiba | Quantidade: {quantidade} | Preço unitário: {170:.2f} | Total: R${(quantidade * 170):.2f}\n"
        case 6:
            while quantidade > vinho6_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 200
            vinho6_qnt -= quantidade
            historico_pedidos += f"Vinho Lopes | Quantidade: {quantidade} | Preço unitário: {200:.2f} | Total: R${(quantidade * 200):.2f}\n"
        case 7:
            while quantidade > vinho7_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 130
            vinho7_qnt -= quantidade
            historico_pedidos += f"Vinho Faleiros | Quantidade: {quantidade} | Preço unitário: {130:.2f} | Total: R${(quantidade * 130):.2f}\n"
        case 8:
            while quantidade > vinho8_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 50
            vinho8_qnt -= quantidade
            historico_pedidos += f"Vinho Felix | Quantidade: {quantidade} | Preço unitário: {50:.2f} | Total: R${(quantidade * 50):.2f}\n"
        case 9:
            while quantidade > vinho9_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 175
            vinho9_qnt -= quantidade
            historico_pedidos += f"Vinho Alves | Quantidade {quantidade} | Preço unitário: {175:.2f} | Total: R${(quantidade * 175):.2f}\n"
        case 10:
            while quantidade > vinho10_qnt:
                quantidade = int(input("Quantidade insuficiente no estoque. Digite uma quantidade válida: "))
            valor_total += quantidade * 115
            vinho10_qnt -= quantidade
            historico_pedidos += f"Vinho Seco | Quantidade: {quantidade} | Preço unitário: {115:.2f} | Total: R${(quantidade * 115):.2f}\n"
        case _:
            print("Código inválido.")

    executa = input("Deseja escolher outras opções de vinho? (sim/nao): ")

    while executa != "sim" and executa != "nao":
        executa = input("Opção inválida. Deseja escolher outras opções de vinho? (sim/nao): ")



print(historico_pedidos)

if valor_total >= 500:
    print(f"Valor total da compra: R${valor_total:.2f}")
    print("Você ganhou frete grátis!")
else:
    if estado == "SP" or estado == "sp":
        valor_total = valor_total + (valor_total * 0.05)
        print(f"Valor total da compra mais 5% de frete: R${valor_total:.2f}")
    else:
        valor_total = valor_total + (valor_total * 0.10)
        print(f"Valor total da compra mais 10% de frete: R${valor_total:.2f}")

print(f"Endereço de entrega: {endereco} - {estado}")
print("Obrigado por comprar na Vinheria Agnello! Volte sempre!")
