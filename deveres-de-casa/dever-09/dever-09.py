# Algoritmo de Bellman-Ford

# Número de vértices
V = 5

# Lista de arestas: (origem, destino, peso)
arestas = [
    (0, 1, 5),
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 1),
    (4, 3, -1)
]

# Inicialização
distancia = [float('inf')] * V
predecessor = [None] * V

# Vértice inicial
origem = 0
distancia[origem] = 0

print("Estado inicial:")
print("Distâncias:", distancia)
print("Predecessores:", predecessor)
print()

# Relaxamento das arestas
for i in range(V - 1):

    print(f"===== ITERAÇÃO {i+1} =====")

    for u, v, peso in arestas:

        if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:

            distancia[v] = distancia[u] + peso
            predecessor[v] = u

    # Exibição da tabela
    print("Vértice | Distância | Predecessor")

    for vertice in range(V):
        print(f"{vertice:^8} | {distancia[vertice]:^10} | {str(predecessor[vertice]):^12}")

    print()

# Verificação de ciclo negativo
ciclo_negativo = False

for u, v, peso in arestas:

    if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
        ciclo_negativo = True
        break

# Resultado final
if ciclo_negativo:
    print("Existe ciclo negativo no grafo.")
else:
    print("Não existe ciclo negativo no grafo.")