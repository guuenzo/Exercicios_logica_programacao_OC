# 12. Soma de cada coluna
# Dada uma matriz, calcule a soma dos elementos de cada coluna e exiba os
# resultados.

import random

## Função que gera um array de 2 dimensões
def generate_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Exemplo de uso
data = generate_2d_array(5, 25,0,11500)

#A FAZER
def somarElementosColuna():
    index = 0
    colNum = 0
    arraySoma = []
    soma = 0

    print(data)
    print('Coluna da matriz dada: ')
    for d in data:
        colNum = data[index][0]
        index += 1
        arraySoma.append(colNum)
        print(colNum)

    for a in arraySoma:
        soma += a

    print(f'Soma da coluna acima: {soma}')

somarElementosColuna()