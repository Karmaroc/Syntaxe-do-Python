"""Estruturas de dados 

Listas - Elementos entre colchetes, são mutáveis, ordenados, indexados e separados por vírgula. 
Tuplas - Elementos entre parênteses, imutáveis, ordenadas, indexados e seperados por vírgula. 
Dicionários - Utiliza-se chaves e inserir pares de chave-valor, chaves únicas, pode ser alterado - mutável, separados por vírgula.
Conjuntos - Coleção desordenada de elementos únicos, imutáveis, não indexados e separados por vírgula.
"""

listas = [1, 2, 3]
listas.append(4) # Mutável
listas[0] # Indexado
x = tuple(listas) # Ordenado, métodos**

tuplas = (1, 2, 3)
#soma = tuplas.count(1) 
indice = tuplas.index(2) # imutável e retorna o índice
y = list(tuplas) # Ordenada
tuplas[2] # Indexados

dicionarios = {"nome": "Ana", "idade": 25}
dicionarios["nome"] # Indexado por chave
dicionarios["nome"] = "Vitor" # Mutável
dicionarios["idade"] = 25 # Par chave-valor única 

conjunto = {1, 2, 6, 10, 3, 4, 5}
list(conjunto) # Desordenada
conjunto.add(5) # Elementos únicos
#conjunto[0] # Não indexado
a = set([1, 2, 3, 4, 5]) # Mutável 
b = frozenset([2, 3, 4, 5]) # Imutável 

