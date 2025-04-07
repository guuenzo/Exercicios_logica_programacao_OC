# 2. Encontre o menor número
# Dado um array, retorne o menor número presente nele.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,11500)

def retornarMenorNumero():
  menor = numeros[0]

  for n in numeros:
    if n < menor:
      menor = n

  print(numeros)
  print(f'O menor numero do array dado acima e o: {menor}')

retornarMenorNumero()