#Parte 2 da atividade 
import time
import random

def gerar_matriz(n):
    return [[random.randint(0, 10) for _ in range(n)] for _ in range(n)]

def multiplicar(A, B):
    n = len(A)
    resultado = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado


for n in [50, 100, 150]:
    A = gerar_matriz(n)
    B = gerar_matriz(n)

    inicio = time.time()
    multiplicar(A, B)
    fim = time.time()

    print(f"N={n} | Tempo={fim - inicio:.6f}s")