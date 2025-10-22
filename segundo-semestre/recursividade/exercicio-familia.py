import json

def listar(dicionario):
    if 'filhos' not in dicionario:
        print(dicionario['nome'])
    else:
        print(dicionario['nome'])
        for filho in dicionario['filhos']:
            listar(filho)

with open('./segundo-semestre/recursividade/familia1.json', 'r', encoding='utf-8') as f:
    dicionario = json.load(f)
    print(dicionario)
    listar(dicionario)

with open('./segundo-semestre/recursividade/familia2.json', 'r', encoding='utf-8') as f:
    dicionario = json.load(f)
    print(dicionario)
    listar(dicionario)