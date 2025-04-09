# 9. Soma de todos os elementos da matriz
# Dada uma matriz N x M, retorne a soma de todos os seus elementos.

import random

## Função que gera um array de 2 dimensões
def generate_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Exemplo de uso
data = generate_2d_array(5, 25,0,11500)

def somarElementos():
    soma = 0

    for d in data:
        for _ in d:
            soma += _

    print(data)
    print(f'A soma de todos os elementos dados na matriz acima e de: {soma}')

somarElementos()