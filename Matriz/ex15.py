# 15. Transposta de uma matriz
# Dada uma matriz N x M, gere sua transposta (troque linhas por colunas).

import random

## Função que gera um array de 2 dimensões
def generate_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Exemplo de uso
data = generate_2d_array(3, 2,0,11500)

def transporMatriz():
    totalColunas = 0
    totalLinhas = 0

    print('Matriz N x M:')
    for d in data:
        print(d)
        totalLinhas += 1

    for d in data[0]:
        totalColunas += 1 

    matrizTransposta = []
    colunaIndex = 0
    while colunaIndex < totalColunas:
        novaLinha = []
        linhaIndex = 0
        while linhaIndex < totalLinhas:
            novaLinha.append(data[linhaIndex][colunaIndex])
            linhaIndex += 1
        matrizTransposta.append(novaLinha)
        colunaIndex += 1

    print('\nMatriz transposta:')
    for m in matrizTransposta:
        print(m)

transporMatriz()