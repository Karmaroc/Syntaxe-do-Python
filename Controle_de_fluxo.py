"""Estrutura Condicional

Com base em condições toma-se decisões.
"""

if False:
    pass
elif False:
    pass
else:
    print("Certo")
    

"""Estruturas de repetição

Com base em condições executa um bloco de código várias vezes.
"""
sequencia = [10, 2, 3]

for item in sequencia:
    print(item)

x = 1

while x < 10:
    x += 1
    #print(x)

"""break, continue, pass 

sai do laço, passa para próxima iteração, operação nula.
"""

for i in range(10):
    if i == 5:
        print(i)
        break
    elif i == 2:
        print(i)
        continue
    pass
    
