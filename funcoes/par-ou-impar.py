def par_ou_impar (numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

print(par_ou_impar(int(input("Digite um número inteiro: "))))