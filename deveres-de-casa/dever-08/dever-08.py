import heapq

# Grafo representado por lista de adjacência
GRAFO = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (4, 5)],
    3: [(4, 1)],
    4: []
}


def dijkstra(grafo, inicio):
    # Inicialização das distâncias
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0

    # Armazena o predecessor de cada nó
    predecessores = {}

    # Fila de prioridade
    fila = [(0, inicio)]

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)

        # Ignora caminhos maiores
        if distancia_atual > distancias[vertice_atual]:
            continue

        print(f"Visitando nó {vertice_atual}")
        print(f"Distâncias atuais: {distancias}\n")

        # Explora vizinhos
        for vizinho, peso in grafo[vertice_atual]:
            nova_distancia = distancia_atual + peso

            # Atualiza se encontrar caminho menor
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = vertice_atual

                heapq.heappush(fila, (nova_distancia, vizinho))

    return distancias, predecessores


# Executando o algoritmo
inicio = 0
fim = 4


distancias, predecessores = dijkstra(GRAFO, inicio)


# Reconstruindo o caminho
caminho = []
atual = fim

while atual != inicio:
    caminho.append(atual)
    atual = predecessores[atual]

caminho.append(inicio)
caminho.reverse()


# Resultado final
print("Caminho mínimo:", caminho)
print("Custo total:", distancias[fim])