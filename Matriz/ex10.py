# 10. Encontre o maior elemento de uma matriz
# Dada uma matriz N x M, encontre o maior número presente nela.

import random

## Função que gera um array de 2 dimensões
def generate_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Exemplo de uso
data = generate_2d_array(5, 25,0,11500)

def retornarMaiorNumero():
    maior = 0

    for d in data:
        for _ in d:
            if _ > maior:
                maior = _

    print(data)
    print(f"O maior numero na matriz dada acima e: {maior}")

retornarMaiorNumero()