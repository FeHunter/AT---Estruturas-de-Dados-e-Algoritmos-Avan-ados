import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Vertice(object):
  def __init__(self, valor):
    self.valor = valor
    self.vizinhos = []

  def __repr__(self):
    return str(self.valor)

class Grafo(object):
  """Implementa um grafo direcionado ou não-direcionado"""
  def __init__(self, direcionado=False):
    self.vertices = []
    self.direcionado = direcionado

  def cria_vertice(self, valor):
    v = Vertice(valor)
    self.vertices.append(v)
    return v

  def adiciona_aresta(self, v1, v2):
    v1.vizinhos.append(v2)
    if not self.direcionado:
      v2.vizinhos.append(v1)

  def desenha(self):
    g = nx.DiGraph() if self.direcionado else nx.Graph()
    for v in self.vertices:
      g.add_node(v)
      for w in v.vizinhos:
        g.add_edge(v, w)
    pos = nx.planar_layout(g)
    tamanho = [400 for _ in g.nodes]
    nx.draw(g, pos, with_labels=True, arrows=True,
            connectionstyle='arc3, rad = 0.1',
            node_color="#cccccc", node_size=tamanho)
    plt.show()

  # DFS
  def dfs(self, inicio):
    visitados = []
    pilha = [inicio]
    while pilha:
      atual = pilha.pop()
      if atual not in visitados:
        visitados.append(atual)
        # ter uma consistente
        pilha.extend(reversed(atual.vizinhos))
    return visitados

  # BFS
  def bfs(self, inicio):
    visitados = []
    fila = deque([inicio])
    while fila:
      atual = fila.popleft()
      if atual not in visitados:
        visitados.append(atual)
        fila.extend(atual.vizinhos)
    return visitados

  # DFS caminho A para C
  def dfs_caminho(self, atual, destino, visitados=None):
    if visitados is None:
      visitados = []

    visitados.append(atual)

    if atual == destino:
      return visitados

    for viz in atual.vizinhos:
      if viz not in visitados:
        caminho = self.dfs_caminho(viz, destino, visitados.copy())
        if caminho:
          return caminho

    return None


g1 = Grafo()

# Criar vertices
A = g1.cria_vertice("A")
B = g1.cria_vertice("B")
C = g1.cria_vertice("C")
D = g1.cria_vertice("D")
E = g1.cria_vertice("E")
F = g1.cria_vertice("F")
G = g1.cria_vertice("G")
H = g1.cria_vertice("H")
I = g1.cria_vertice("I")
J = g1.cria_vertice("J")
K = g1.cria_vertice("K")

# Arestas
g1.adiciona_aresta(A, B)
g1.adiciona_aresta(A, I)
g1.adiciona_aresta(C, F)
g1.adiciona_aresta(D, A)
g1.adiciona_aresta(D, I)
g1.adiciona_aresta(H, D)
g1.adiciona_aresta(H, E)
g1.adiciona_aresta(H, F)
g1.adiciona_aresta(H, G)
g1.adiciona_aresta(I, H)
g1.adiciona_aresta(J, C)
g1.adiciona_aresta(J, H)

# Desenhar
g1.desenha()

print("DFS saindo de A:", g1.dfs(A))
print("BFS saindo de I:", g1.bfs(I))
print("Caminho A a C:", g1.dfs_caminho(A, C))


g2 = Grafo(direcionado=True)

# vertices
A2 = g2.cria_vertice("A")
B2 = g2.cria_vertice("B")
C2 = g2.cria_vertice("C")
D2 = g2.cria_vertice("D")
E2 = g2.cria_vertice("E")
F2 = g2.cria_vertice("F")
G2 = g2.cria_vertice("G")
H2 = g2.cria_vertice("H")
I2 = g2.cria_vertice("I")
J2 = g2.cria_vertice("J")
K2 = g2.cria_vertice("K")

# arestas com direcionamento
g2.adiciona_aresta(A2, B2)
g2.adiciona_aresta(A2, I2)
g2.adiciona_aresta(C2, F2)
g2.adiciona_aresta(D2, A2)
g2.adiciona_aresta(D2, I2)
g2.adiciona_aresta(H2, D2)
g2.adiciona_aresta(H2, E2)
g2.adiciona_aresta(H2, F2)
g2.adiciona_aresta(H2, G2)
g2.adiciona_aresta(I2, H2)
g2.adiciona_aresta(J2, C2)
g2.adiciona_aresta(J2, H2)

g2.desenha()

print("DFS saindo de A:", g2.dfs(A2))
print("BFS saind de I:", g2.bfs(I2))
print("Caminho A até C:", g2.dfs_caminho(A2, C2))

