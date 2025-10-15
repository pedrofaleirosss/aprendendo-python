import requests

try:
    uf = input('Informe a UF: ')
    resposta = requests.get(f'http://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios')

    if resposta.status_code == 200:
        dados = resposta.json()

        if len(dados) > 0:
            for item in dados:
                print(item['nome'])
        else:
            print('Municipio inexistente')
    else:
        print(f'ERRO: {resposta.status_code}')
except requests.exceptions.ConnectionError as erro:
    print('Erro. Erro de Conexão com API')
except Exception as erro:
    print(f'Erro: {erro}')