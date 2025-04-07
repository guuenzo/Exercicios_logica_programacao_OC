# 6. Inverta um array
# Dado um array, retorne um novo array com os elementos invertidos.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,11500)

def retornarArrayInverso():
    arrayInverso = []
    tamanho = 0
    index = 0

    for n in numeros:
        tamanho += 1

    index = tamanho - 1

    while index >= 0:
        arrayInverso.append(numeros[index])
        index -= 1

    print(f'Array original: {numeros}')
    print(f'Novo array com os elementos invertidos: {arrayInverso}')

retornarArrayInverso()