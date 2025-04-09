# 12. Soma de cada coluna
# Dada uma matriz, calcule a soma dos elementos de cada coluna e exiba os
# resultados.

import random

## Função que gera um array de 2 dimensões
def generate_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Exemplo de uso
data = generate_2d_array(5, 25,0,11500)

def somarElementosColuna():
    index = 0
    totalColunas = 0
    totalLinhas = 0

    print("Matriz:")
    for d in data:
        print(f'{d}\n')
        totalLinhas += 1  

    for d in data[0]:
        totalColunas += 1 

    while index < totalColunas:
        coluna = 0
        arraySoma = []
        soma = 0

        for d in data:
            colNum = data[coluna][index]
            arraySoma.append(colNum)
            print(f'Coluna {index}, Linha {coluna}: {colNum}')
            coluna += 1

        for a in arraySoma:
            soma += a

        print(f'Soma da coluna {index}: {soma}\n')

        colNum = 0
        coluna = 0
        arraySoma = []
        soma = 0
        index += 1

somarElementosColuna()