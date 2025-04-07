# 3. Calcule a soma dos elementos
# Dado um array, calcule a soma de todos os seus elementos.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,11500)

def somarElementos():
  soma = 0

  for n in numeros:
    soma += n

  print(numeros)
  print(f'A soma de todos os elementos no array dado acima e igual a: {soma}')

somarElementos()