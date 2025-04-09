# 11. Soma de cada linha
# Dada uma matriz, calcule a soma dos elementos de cada linha e exiba os
# resultados.

import random

## Função que gera um array de 2 dimensões
def generate_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Exemplo de uso
data = generate_2d_array(5, 25,0,11500)

def somarElementosLinha():
    i = 1
    soma = 0

    for d in data:
        print(f"{i}º Linha")
        print(d)
        for _ in d:
            soma += _
            
        print(f'Soma de todos os elementos da {i}º Linha: {soma}')    
        soma = 0
        i += 1

somarElementosLinha()