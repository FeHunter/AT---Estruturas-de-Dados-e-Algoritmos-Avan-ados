INF = float('inf')
# grafo em sequencia o ultimo e a forja M
dist = [
    [0, 4, INF, INF, 5, INF, INF, INF, INF, INF, INF, INF],
    [4, 0, INF, INF, 4, INF, INF, INF, INF, INF, INF, 3],
    [INF, INF, 0, 5, INF, INF, INF, 5, INF, 3, INF, 4],
    [INF, INF, 5, 0, INF, INF, INF, INF, INF, 4, INF, INF],
    [5, 4, INF, INF, 0, 2, INF, 5, INF, INF, INF, 6],
    [INF, INF, INF, INF, 2, 0, 4, 4, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, 4, 0, 3, 4, INF, INF, INF],
    [INF, INF, 5, INF, 5, 4, 3, 0, INF, 3, INF, INF],
    [INF, INF, INF, INF, INF, INF, 4, INF, 0, INF, 3, INF],
    [INF, INF, 3, 4, INF, INF, INF, 3, INF, 0, 3, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, 3, 3, 0, INF],
    [INF, 3, 4, INF, 6, INF, INF, INF, INF, INF, INF, 0]
]

# algoritmo de FloydWarshall
V = len(dist)
for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# colcando a heuristica TSP
def tsp(dist):
    V = len(dist)
    melhor_rota = None
    menor_custo = INF

    for start in range(V):
        visitados = [False]*V   
        rota = [start]
        custo = 0
        visitados[start] = True
        atual = start

        for _ in range(V-1):
            proximo = None
            min_dist = INF
            for j in range(V):
                if not visitados[j] and dist[atual][j] < min_dist:
                    min_dist = dist[atual][j]
                    proximo = j
            rota.append(proximo)
            visitados[proximo] = True
            custo += min_dist
            atual = proximo

        # volta pro incio
        custo += dist[atual][start]
        rota.append(start)

        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = rota

    return melhor_rota, menor_custo

rota, tempo_total = tsp(dist)
print("\nMelhor rota com a  heuristica TSP:", rota)
print("Tempo total:", tempo_total)
