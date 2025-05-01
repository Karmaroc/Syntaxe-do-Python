"""Try/Except

Trata erros que ocorrem durante a execução de um programa.
"""

try:
    x = 10 / 0
    
except ZeroDivisionError:
    print("Não pode dividir por zero!")

else:
    print("Divisão feita com sucesso.")

finally:
    print("Esse bloco sempre será executado.")
    
# Exemplos de erros

try:
    lista = [1, 2, 3]
    print(lista[5])

except IndexError:
    print("Não exise esse indice.")

try:
    dicionario = {"chave": "valor"}
    print(dicionario["outra_chave"])

except KeyError:
    print("Não existe essa chave.")
    
try:
    x = int("Palavra")

except ValueError:
    print("O valor para a função int está incorreto.")
    
try:
    z = "abc" + 5
    
except TypeError:
    print("Operação tipos inesperados.")

try:
    lista = [1, 2, 3]
    lista.append()

except TypeError:
    print("Precisa de um argumeto.")

try:
    #import modulo
    ...
except ImportError:
    print("Import de módulo inexistente.")

try:
    open("arquivo_inexistente.txt")

except FileNotFoundError:
    print("Não pode abrir, pois não existe.")

try:
    #print(variavel_nao_definida)
    ...
except NameError:
    print("A variável não foi definida.")



