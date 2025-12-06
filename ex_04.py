import matplotlib.pyplot as plt
import networkx as nx


class Vertice(object):
  """Implementa um vértice de grafo"""

  def __init__(self, valor):
    self.valor = valor
    self.vizinhos = []

  def __repr__(self):
    return str(self.valor)

class Grafo(object):
  """Implementa um grafo que pode ser direcionado ou não-direcionado"""
  def __init__(self, direcionado=False):
    self.vertices = []
    self.direcionado = direcionado

  def cria_vertice(self, valor):
    """Cria vértice com o valor definido"""
    vertice = Vertice(valor)
    self.vertices.append(vertice)
    return vertice

  def adiciona_aresta(self, v1, v2):
    """Adiciona aresta entre v1 e v2 (direcionado ou não)"""
    v1.vizinhos.append(v2)

    if not self.direcionado:
      # grafo não-direcionado
      v2.vizinhos.append(v1)

  def desenha(self):
    """Desenha o grafo, direcionado ou não-direcionado"""
    # alterar o tipo de grafo do NetworkX
    g = nx.DiGraph() if self.direcionado else nx.Graph()

    for vertice in self.vertices:
      g.add_node(vertice)
      for vizinho in vertice.vizinhos:
        g.add_edge(vertice, vizinho)

    pos = nx.planar_layout(g)
    tamanho = [300 * len(str(v)) for v in g.nodes]

    nx.draw(
      g, pos, with_labels=True, arrows=True,
      connectionstyle='arc3, rad = 0.1',
      node_color="#cccccc", node_size=tamanho
    )
    plt.show()

class GrafoDirecionado(Grafo):
  """Implementa um grafo direcionado"""

  def adiciona_aresta(self, v1, v2):
    """Adiciona aresta entre v1 e v2"""
    v1.vizinhos.append(v2)

  def desenha(self):
    """Desenha o grafo"""
    g = nx.DiGraph()
    for vertice in self.vertices:
      g.add_node(vertice)
      for vizinho in vertice.vizinhos:
        g.add_edge(vertice, vizinho)
    pos = nx.planar_layout(g)
    tamanho = [300 * len(str(v)) for v in g.nodes]
    nx.draw(g, pos, with_labels=True, arrows=True,
            connectionstyle='arc3, rad = 0.1',
            node_color="#cccccc", node_size=tamanho)
    plt.show()

amigos = Grafo()

alice = amigos.cria_vertice("Alice")
bob = amigos.cria_vertice("Bob")
cynthia = amigos.cria_vertice("Cynthia")
diana = amigos.cria_vertice("Diana")
elise = amigos.cria_vertice("Elise")
fred = amigos.cria_vertice("Fred")
jamal = amigos.cria_vertice("Jamal")
melvyn = amigos.cria_vertice("Melvyn")
rodrigo = amigos.cria_vertice("Rodrigo")
stella = amigos.cria_vertice("Stella")
vicky = amigos.cria_vertice("Vicky")

amigos.adiciona_aresta(alice, bob)
amigos.adiciona_aresta(bob, cynthia)
amigos.adiciona_aresta(alice, diana)
amigos.adiciona_aresta(bob, diana)
amigos.adiciona_aresta(elise, fred)
amigos.adiciona_aresta(diana, fred)
amigos.adiciona_aresta(fred, alice)
amigos.adiciona_aresta(rodrigo, melvyn)
amigos.adiciona_aresta(stella, jamal)

# for v in amigos.vertices:
#   print(f"{v.valor}: {v.vizinhos}")

amigos.desenha()

# amigos.desenha()

# print("Amigos de Alice:", alice.vizinhos)

seguidos = Grafo(direcionado=True)

alice = seguidos.cria_vertice("Alice")
bob = seguidos.cria_vertice("Bob")
cynthia = seguidos.cria_vertice("Cynthia")
seguidos.adiciona_aresta(alice, bob)
seguidos.adiciona_aresta(bob, cynthia)
seguidos.adiciona_aresta(cynthia, bob)

seguidos.desenha()

# print("Seguidos por Alice:", alice.vizinhos)
# print("Seguidos por Bob:", bob.vizinhos)