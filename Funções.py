"""Funções 

Bloco de código que executa uma tarefa e pode ser reutilizável. 
"""

def saudacao(nome):
    return f"Olá {nome}!"

print(saudacao("Mundo!"))

"""Funções anônimas (lambda)

Funções sem um nome definido.
"""

soma = lambda x, y: x + y
print(soma(10, 5))