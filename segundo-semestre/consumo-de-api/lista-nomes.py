import requests

n = input("Digite a quantidade de nomes que deseja: ")
url = f"http://randomuser.me/api/?results={n}"

try:
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        lista = []
        for dado in dados["results"]:
            lista.append(dado["name"]["first"])

        lista.sort()
        print(lista)
    else:
        print(f'ERRO: {response.status_code}')
except requests.exceptions.ConnectionError as erro:
    print('Erro. Erro de Conexão com API')
except Exception as erro:
    print(f'Erro: {erro}')