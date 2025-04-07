# 8. Rotacione um array para a direita
# Dado um array e um número k, rotacione os elementos k vezes para a direita.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,11500)

def rotacionarElementosArrayDireita(k):
  tamanho = 0
  ultimoElemento = 0
  
  print(f"Array original: {numeros}")

  for n in numeros:
    tamanho += 1

  while k > 0:
        ultimoElemento = numeros.pop()
        numeros.insert(0, ultimoElemento)
        k -= 1

  print(f'Array rotacionado: {numeros}')

rotacionarElementosArrayDireita(3)