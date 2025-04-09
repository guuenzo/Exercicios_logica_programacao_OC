# 14.Diagonal secundária
# Dada uma matriz quadrada N x N, retorne os elementos da sua diagonal
# secundária.

import random

## Função que gera um array de 2 dimensões
def generate_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Exemplo de uso
data = generate_2d_array(3, 3,0,11500)

def retornarDiagonalSecundaria(): 
    print('Matriz quadrada N x N:')
    for d in data:
        print(d)

    tamanho = 0
    for d in data:
        tamanho += 1

    index = 0
    novoArray = []
    for d in data:
        novoArray.append(data[index][tamanho - 1 - index])
        index += 1

    print('Elementos da diagonal secundaria da matriz gerada acima: ')
    for a in novoArray:
        print(a)

retornarDiagonalSecundaria()