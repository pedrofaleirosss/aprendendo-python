import requests

cep = input("Digite o CEP: ")
link = f'https://viacep.com.br/ws/{cep}/json'

try:
    response = requests.get(link)

    if response.status_code == 200:
        dicionario = response.json()

        print(f"CEP: {dicionario['cep']}")
        print(f"Logradouro: {dicionario['logradouro']}")
        print(f"Complemento: {dicionario['complemento']}")
        print(f"Bairro: {dicionario['bairro']}")
        print(f"Localidade: {dicionario['localidade']}")
        print(f"UF: {dicionario['uf']}")
    elif response.status_code == 404:
        print('Não foi possível encontrar o endereço passado como parâmetro')
    elif response.status_code == 500:
        print('Ocorreu algum erro no servidor')
    else:
        print(response.status_code)
except ConnectionError:
    print('Erro de Conexão')
except Exception:
    print('Erro')