# 16. Verifique se uma matriz é simétrica
# Uma matriz quadrada é simétrica se for igual à sua transposta.

import random

## Função que gera um array de 2 dimensões
def generate_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Exemplo de uso
data = generate_2d_array(3, 3,0,1)

def verificarSimetriaMatriz():
    totalLinhas = 0
    totalColunas = 0

    print('Matriz fornecida: ')
    for d in data:
        print(d)
        totalLinhas += 1

    for _ in data[0]:
        totalColunas += 1

    if totalLinhas != totalColunas:
        print("A matriz não é quadrada, então não pode ser simétrica.")
        return

    # Verifica simetria sem usar range
    linhaIndex = 0
    while linhaIndex < totalLinhas:
        colunaIndex = 0
        while colunaIndex < totalColunas:
            if data[linhaIndex][colunaIndex] != data[colunaIndex][linhaIndex]:
                print("A matriz fornecida não é simétrica.")
                return
            colunaIndex += 1
        linhaIndex += 1

    print("A matriz fornecida é simétrica.")

verificarSimetriaMatriz()