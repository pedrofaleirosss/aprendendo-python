def exibir_boas_vindas():
    print("---------------------- Bem-vindo à Vinheria Agnello ----------------------")

exibir_boas_vindas()

nome_vinhos = ["Luara Tempranillo"]
qtd_vinhos = [2]

def cadastra_ou_sai():
    resposta = int(input("Deseja cadastrar mais um vinho? 1 - Cadastrar / 2 - Sair: "))

    while resposta != 1 and resposta != 2:
        print("Resposta inválida!")
        resposta = int(input("Deseja cadastrar mais um vinho? 1 - Cadastrar / 2 - Sair: "))

    if (resposta == 2):
        return True 
    else:
        return False

def cadastra_vinho():
    nome = input("Digite o nome do vinho: ")
    quantidade = int(input("Digite a quantidade desse vinho: "))

    while (quantidade <= 0):
        print("A quantidade deve ser maior que zero!")
        quantidade = int(input("Digite a quantidade desse vinho: "))

    nome_vinhos.append(nome)
    qtd_vinhos.append(quantidade)

while True:
    cadastra_vinho()
    if (cadastra_ou_sai()):
        break

def mostra_menu():
    print("---------------- Menu de Vinhos ----------------")

    for i in range(len(nome_vinhos)):
        print(f"Nome: {nome_vinhos[i]} | Quantidade: {qtd_vinhos[i]}")

mostra_menu()