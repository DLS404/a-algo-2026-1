# Parte 1 da atividade
import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


# Teste de tempo
for n in [1000, 2000, 4000, 8000]:
    arr = [random.randint(0, 10000) for _ in range(n)]

    inicio = time.time()
    merge_sort(arr)
    fim = time.time()

    print(f"N={n} | Tempo={fim - inicio:.6f}s")