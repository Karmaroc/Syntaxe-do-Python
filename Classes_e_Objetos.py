"""Classes e Objetos 

Define atributos(caracteristicas) e métodos(ações) que os objetos da classe terão.
É modular e reutilizável, é um molde que gera novas instâncias - objetos.
"""

class Dog:
    def __init__(self, nome, raca): # Método inicializador
        self.nome = nome
        self.raca = raca

d1 = Dog("Asper", "Milinois")
#d1.nome = "Asper"
#d1.raca = "Milinois"

d2 = Dog("Luminuss", "Dogo Argentino")
#d2.nome = "Luminuss" # Atributos
#d2.raca = "Dogo Argentino"

# print(d1.nome)
# print(d1.raca)

#print(d2.nome)
#print(d2.raca) # Acessar um atributo.

class Carro:
    def __init__(self, nome):
        self.nome = nome
        
    def acelerar(self): # Método é uma função dentro da classe.
        print(f'{self.nome} está acelerando...')
        
carro1 = Carro("Ferrari")
#carro1.acelerar()
#Carro.acelerar(carro1)

"""Herança em Classes
 
Herda todos os métodos e atributos de outra classe. 
A classe original é chamada de classe base e a nova classe é chamada de classe derivada.
"""         

# Classe Original/base

class Animal:
    def __init__(self): # Self é a referência atual dentro de uma classe para referenciar o objeto.
        print("Essa mensagem substitui o super().")
    
    def mensagem(self): # Métodos de instância.
        print("Animal do Vitor")
    
    def comer(self):
        print("Comendo")
        
# Classe derivada

class Cachorro(Animal):
    def __init__(self, nome):
        
        super().__init__() # O Python executa o __init__
        self.nome = nome
        print(f"Meu cachorro chama {self.nome}.")
        
    def quem_sou_eu(self):
        print("Eu sou o cão do Vitor.")
        
    def latir(self):
        print("Au Au!")

meu_cao = Cachorro("Loki")

meu_cao.mensagem() # Chamada do método 
meu_cao.quem_sou_eu()
meu_cao.latir()
meu_cao.comer() 
