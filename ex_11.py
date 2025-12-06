import heapq, itertools, math

grafo = {
 'blum': [('cerf',22),('dahi',16)],
 'cerf': [('blum',22),('dahi',29),('gray',34),('kay',26),('naur',65)],
 'dahi': [('blum',16),('cerf',29),('gray',28),('kay',24)],
 'kay' : [('dahi',24),('cerf',26),('gray',25),('naur',36)],
 'gray': [('cerf',34),('dahi',28),('kay',25),('naur',30)],
 'naur': [('gray',30),('cerf',65),('kay',36)]
}

def dijkstra(g, start):
    dist={v:math.inf for v in g}
    prev={v:None for v in g}
    dist[start]=0
    pq=[(0,start)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in g[u]:
            nd=d+w
            if nd<dist[v]:
                dist[v]=nd; prev[v]=u
                heapq.heappush(pq,(nd,v))
    return dist,prev

dist, prev = dijkstra(grafo, 'dahi')
# reconstruir caminho dahi áte naur
path=[]
cur='naur'
while cur:
    path.append(cur)
    cur = prev[cur]
path = list(reversed(path))
print("\n Resultado com Dijkstra dahi até naur: \n", dist['naur'], path)

# permutations
start = 'cerf'
cities = list(grafo.keys())
others = [c for c in cities if c != start]

best = None
best_path = None
for perm in itertools.permutations(others):
    path = [start] + list(perm) + [start]
    total = 0
    ok = True
    for i in range(len(path)-1):
        u,v = path[i], path[i+1]
        found = False
        for x,w in grafo[u]:
            if x == v:
                total += w; found = True; break
        if not found:
            ok = False; break
    if not ok: continue
    if best is None or total < best:
        best = total; best_path = path

print("\n TSP (start=end cerf):", best, best_path)

#arvore geradora minima com prim
def prim(g, start=None):
    import heapq
    nodes=set(g.keys())
    if not start: start=next(iter(nodes))
    visited=set([start])
    pq=[]
    for v,w in g[start]:
        heapq.heappush(pq,(w,start,v))
    edges=[]
    total=0
    while pq and len(visited)<len(nodes):
        w,u,v=heapq.heappop(pq)
        if v in visited: continue
        visited.add(v)
        edges.append((u,v,w))
        total+=w
        for x,wx in g[v]:
            if x not in visited:
                heapq.heappush(pq,(wx,v,x))
    return edges,total

edges_mst, total_mst = prim(grafo,'blum')
print("\nPrim MST edges:", edges_mst)
print("\nPrim MST total:", total_mst)

# ciar a lista de arestas sem duplicar os valores
seen = set()
edges = []
for u in grafo:
    for v,w in grafo[u]:
        a = tuple(sorted((u,v)))
        if a not in seen:
            seen.add(a); edges.append(a)

def greedy_vertex_cover(edges):
    uncovered = set(edges)
    cover = set()
    while uncovered:
        deg={}
        for u,v in uncovered:
            deg[u]=deg.get(u,0)+1
            deg[v]=deg.get(v,0)+1
        pick = max(deg.items(), key=lambda x:x[1])[0]
        cover.add(pick)
        uncovered = {e for e in uncovered if pick not in e}
    return cover

cover = greedy_vertex_cover(edges)
print("\n Cobertura:", cover)
