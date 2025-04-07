# 4. Calcule a média dos elementos
# Dado um array de números, retorne a média dos valores.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,11500)

def calcularMediaValores():
  soma = 0
  quantidade = 0
  media = 0

  for n in numeros:
    quantidade += 1
    soma += n

  media = soma / quantidade

  print(numeros)
  print(f'A media dos valores dados no array acima e de: {media}')

calcularMediaValores()