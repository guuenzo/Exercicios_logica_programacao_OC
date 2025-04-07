# 5. Conte os números pares e ímpares
# Dado um array de números inteiros, conte quantos são pares e quantos são
# ímpares.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,11500)

def contarParesImpares():
  pares = 0
  impares = 0

  for n in numeros:
    if n % 2 == 0:
      pares += 1
    else:
      impares += 1
  
  print(numeros)
  print(f'No array dado acima o total de numeros pares encontrados foi de: {pares}, ja de numeros impares foi de: {impares}')


contarParesImpares()