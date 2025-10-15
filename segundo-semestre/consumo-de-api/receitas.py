import requests

ingrediente = input("Digite um ingrediente: ")
url = "http://dummyjson.com/recipes?limit=50"

try:
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        for receita in dados["recipes"]:
            if ingrediente.capitalize() in receita["ingredients"]:
                print(receita)
    else:
        print(f'ERRO: {response.status_code}')
except requests.exceptions.ConnectionError as erro:
    print('Erro. Erro de Conexão com API')
except Exception as erro:
    print(f'Erro: {erro}')