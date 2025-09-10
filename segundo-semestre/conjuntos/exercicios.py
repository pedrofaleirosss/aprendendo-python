# Exercício 1

# pares = {0, 2, 4, 6, 8, 10}
# impares = {1, 3, 5, 7, 9}
#
# print(f"A união dos conjuntos é {pares.union(impares)}")
# print(f"A interseção dos conjuntos é {pares.intersection(impares)}")
# print(f"A diferença dos conjuntos é {pares.difference(impares)}")

# Exercício 2

# lista = ["Maçã", "Banana", "Laranja", "Maçã", "Banana", "Limao"]
# conjunto = set(lista)
# lista = list(conjunto)
#
# print(lista)

# Exercício 3

# lista = [1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9, 10]
# conjunto = set(lista)
# numero_elementos = 0
#
# for cont in conjunto:
#     numero_elementos = numero_elementos + 1
#
# print(f"A quantidade de elementos únicos da lista é {numero_elementos}")

# Exercício 4

# conjunto1 = {"Pedro", "Carlos", "Matheus", "João"}
# conjunto2 = {"Maria", "Matheus", "Alice", "Pedro"}
#
# print(f"A diferença dos conjuntos é {conjunto1.difference(conjunto2), conjunto2.difference(conjunto1)}")

# Exercício 5

# java = {'joao', 'ana', 'pedro', 'maria', 'fernando', 'mariana'}
# python = {'ana', 'francisco', 'fernando', 'maria', 'henrique'}
# 
# # Os alunos que frequentam apenas o curso de Python.
# print(python - java)
# 
# # Os alunos que frequentam apenas o curso de Java.
# print(java - python)
# 
# # Os alunos que frequentam ambos os cursos.
# print(java & python)
# 
# # Os alunos que frequentam pelo menos um dos cursos
# print(java | python)
# 
# # os alunos que estão em uma das turmas, mas nao em ambas.
# print(java ^ python)            # diferenca simetrica