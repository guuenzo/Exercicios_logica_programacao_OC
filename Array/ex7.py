# 7. Remova duplicatas
# Dado um array com números repetidos, retorne um novo array apenas com
# valores únicos.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,5)

def retornarArrayUnico():
    arrayUnico = []
    duplicado = False

    for n in numeros:
        duplicado = False
        for u in arrayUnico:
            if n == u:
                duplicado = True
                break
        if duplicado == False:
            arrayUnico.append(n)

    print(numeros)
    print(arrayUnico)

retornarArrayUnico()