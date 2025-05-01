"""Outros Recuros

> List Comprehension, forma concisa e eficiente de criar listas em Python. 
Em uma única linha.

> Decorators, sem alterar o código permite adicionar funcionalidades a outras funções.
Executando antes ou depois dela, retornado uma função modificada.

> Context Managers (with), é um objeto que define métodos a serem usados em conjunto com
a instrução with.

> Generators, função especial que permite criar iteradores de forma fácil.
Usando a palavra-chave "yield".  
"""

# List Comprehensions

quadrados = [x**2 for x in range(5)]
print(quadrados)

numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Decorators

def decorator(func):
    def wrapper():
        print("Algo antes...")
        func()
        print("Algo depois...")
        
    return wrapper

def outra_funcao():
    print("Sou um belo argumento!")
    
funcao_decorada = decorator(outra_funcao)
funcao_decorada()

# Gerenciador de contexto

with open('file.txt', 'r') as file:
    content = file.read()
    
print(content)

# Generators - Economiza memória, útil para sequências grandes ou infinitas.

def contador():
    for i in range(3):
        yield i
    
for num in contador():
    print(num)