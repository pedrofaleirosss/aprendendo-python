idade = int(input("Digite a idade: "))
tempo_servico = int(input("Digite o tempo de serviço: "))

if idade >= 65:
    print("Pode aposentar-se.")
elif tempo_servico >= 30:
    print("Pode aposentar-se.")
elif idade >= 60 and tempo_servico >= 25:
    print("Pode aposentar-se.")
else:
    print("Não pode aposentar-se.")