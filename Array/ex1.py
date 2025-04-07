# 1. Encontre o maior número
# Dado um array, retorne o maior número presente nele.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,11500)

def retornarMaiorNumero():
  maior = 0

  for n in numeros:
    if n > maior:
      maior = n
  
  print(numeros)
  print(f'O maior numero do array dado acima e o: {maior}')

retornarMaiorNumero()