
# grafo
grafo = [
    (1, 2, 15),
    (1, 3, 12),
    (2, 3, 6),
    (2, 5, 5),
    (2, 4, 13),
    (3, 4, 6)
]

#union find
parent = {}
rank = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    raizA = find(a)
    raizB = find(b)

    if raizA == raizB:
        #se já tiver conectado
        return False

    if rank[raizA] < rank[raizB]:
        parent[raizA] = raizB
    elif rank[raizA] > rank[raizB]:
        parent[raizB] = raizA
    else:
        parent[raizB] = raizA
        rank[raizA] += 1

    return True


# inicar
vertices = {1, 2, 3, 4, 5}
for v in vertices:
    parent[v] = v
    rank[v] = 0

# organizar arestas
grafo.sort(key=lambda x: x[2])

mst = []
total_cost = 0

#Kruskal
for u, v, cost in grafo:
    if union(u, v):
        mst.append((u, v, cost))
        total_cost += cost

print("\nreultado:")
for u, v, c in mst:
    print(f"{u} - {v} (custo {c})")

print("\nCusto total:", total_cost)
