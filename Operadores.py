"""Operadores

Aritméticos: +, -, *, /, //, %, **
Comparação: ==, !=, >, <, >=, <=
Lógicos: and, or, not 
Atribuição: =, +=, -=, *=, /=, //=, %=, **=
Identidade: "is" e "is not"
Membro: in, not in
Bitwise: &, |, ^, ~, <<, >>
"""

# Aritméticos

soma = 10 + 11
subtracao = 10 - 2
multiplicacao = 10 * 3
divisao = 10 / 3
divisao2 = 10 // 4
divisao3 = 15 % 2
potenciacao = 2 ** 10

# Comparação

igualdade = 10 == 10
diferenca = 11 != 10
maior = 5 > 2
menor = 1 < 15
maior_igual = 10 >= 4
menor_igual = 5 <= 5

# Lógicos 

dois_iguais = True and True # Os dois valores devem ser True para retornar True.
um_dos_dois = True or False # Apenas um valor precisa ser True para retornar True.
nega = not dois_iguais # Inverte o valor.

# Atribuição

incremento = 0
incremento += 10

decremento = 10
decremento -= 5

# Identidade

var1 = "Fogo" 
var2 = "Agua"
ele_eh = var1 is var2
ele_nao_eh = var1 is not var2 # Não está no mesmo endereço de memória

# Membro

tem_dentro = "Oi" in "Oi, Mundo!"
nao_tem_dentro = "Oi" not in "Damasco"

# Bitwise

x = True & True
y = 10 ^ 5 # XOR bit a bit, faz um calculo para encontrar um número binário sob cada valor. 

