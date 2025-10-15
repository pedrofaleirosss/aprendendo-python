import requests

url = "http://dummyjson.com/products?limit=100"

try:
    response = requests.get(url)

    if response.status_code == 200:
        valor_total = 0
        dados = response.json()
        quantidade_total = 0

        for produto in dados["products"]:
            valor_total_produto = produto["price"] * (100 - produto["discountPercentage"]) * produto["stock"]
            valor_total += valor_total_produto
            quantidade_total += produto["stock"]

        print(f"O valor total do estoque é R${valor_total:.2f} e a quantidade de produtos é {quantidade_total}")
    else:
        print(f'ERRO: {response.status_code}')
except requests.exceptions.ConnectionError as erro:
    print('Erro. Erro de Conexão com API')
except Exception as erro:
    print(f'Erro: {erro}')