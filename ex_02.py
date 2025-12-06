import math
from datetime import datetime

def ind_filho_esq(ind):
  """Retorna o índice do filho esquerdo de ind"""
  return ind * 2 + 1

def ind_filho_dir(ind):
  """Retorna o índice do filho direito de ind"""
  return ind * 2 + 2

def ind_pai(ind):
  """Retorna o índice do pai de ind"""
  return (ind - 1) // 2

def to_ts(dthr):
    """ converter dthr em timestamp """
    return datetime.strptime(dthr, "%Y-%m-%d %H:%M:%S").timestamp()

def chave_paciente(p):
    """ Chave de prioridade: maior gravidade primeiro e se empatar o menor dthr primeiro """
    return (p["grav"], -to_ts(p["dthr"]))

class Heap(object):
  """Implementa um heap baseado em array"""
  def __init__(self, chave=lambda x:x, max_heap=True):
    self.__dados = []
    self.__chave = chave
    self.__max_heap = max_heap

  def __repr(self, no=0, tipo="", indent=""):
    """Produz representação de subárvore como str"""
    s = ""
    if no < len(self.__dados):
      indent += " " * 3
      s += self.__repr(ind_filho_dir(no), "┌➝",
                       indent + ("│" if tipo == "└➝" else " "))
      s += f"{indent[6:]}{tipo} {self.__dados[no]}\n"
      s += self.__repr(ind_filho_esq(no), "└➝",
                       indent + ("│" if tipo == "┌➝" else " "))
    return s

  def __str__(self):
    return self.__repr() + "\n" + str(self.__dados)

  def __maior(self, ind1, ind2):
    """Retorna True de ind1 > ind2 e False caso contrário"""
    chave1 = self.__chave(self.__dados[ind1])
    chave2 = self.__chave(self.__dados[ind2])
    if self.__max_heap:
      return chave1 > chave2
    return chave2 > chave1

  def __tem_filho_maior(self, ind):
    """Verifica se ind tem filho com valor maior"""
    esq = ind_filho_esq(ind)
    dir = ind_filho_dir(ind)
    return ((esq < len(self.__dados) and self.__maior(esq, ind))
            or
            (dir < len(self.__dados) and self.__maior(dir, ind)))

  def __maior_filho(self, ind):
    """Retorna o índice do maior filho de ind"""
    esq = ind_filho_esq(ind)
    dir = ind_filho_dir(ind)
    if dir >= len(self.__dados):
      if esq < len(self.__dados):
        return esq
      return -1
    if self.__maior(dir, esq):
      return dir
    return esq

  def insere(self, item):
    """Insere item no heap"""
    self.__dados.append(item)
    novo = len(self.__dados) - 1
    pai = ind_pai(novo)
    while novo > 0 and self.__maior(novo, pai):
      self.__dados[novo], self.__dados[pai] = \
          self.__dados[pai], self.__dados[novo]
      novo = pai
      pai = ind_pai(novo)

  def remove(self):
    """Remove item do heap"""
    if not self.__dados:
      return None
    if len(self.__dados) == 1:
      return self.__dados.pop()
    item = self.max()
    self.__dados[0] = self.__dados.pop()
    no = 0
    while self.__tem_filho_maior(no):
      maior_filho = self.__maior_filho(no)
      self.__dados[no], self.__dados[maior_filho] = \
          self.__dados[maior_filho], self.__dados[no]
      no = maior_filho
    return item

  def max(self):
    """Retorna o valor máximo no heap"""
    if self.__dados:
      return self.__dados[0]

  def vazio(self):
    """Retorna True se o heap está vazio, False caso contrário"""
    return len(self.__dados) == 0
  
  def niveis(self):
    """Retorna a quantidade  de níveis do heap"""
    """
        Para descobrir a quantidade de níveis do heap, vou utilizar a formula: níveis = [log2(tamanho)] + 1
        Esta formula segue O(1) porque, não vamos percorre a lista apenas pegar o seu tamanho e fazer um calculo de soma.
    """
    if len(self.__dados) == 0:
        return 0
    return math.floor(math.log2(len(self.__dados))) + 1
  
  def mescla(self, outro):
    """Mescla outro heap neste heap fazendo o outro heap fica vazio"""
    """
        A função vai conferir se o heap atual e do passado como argumentos são iguais, se não for vamos lançar uma exceção porque heaps diferentes
        não podem ser mesclados. Depois a função deve percorre todos os elementos do segundo heap e inserir no heap atual usando o insere() e
        por fim esvaziar o segundo heap.
    """
    # verifcar se as funções chave são iguais
    if self.__chave != outro.__chave:
        raise Exception("Heaps possuem funções chave diferentes")
    # Inserir todos os elementos do outro heap neste heap
    for item in outro.__dados:
        self.insere(item)
    # esvaziar o segundo heap
    outro.__dados.clear()

# lista = [100, 88, 25, 87, 16, 8, 12, 86, 50, 2, 15, 3]
# h = Heap()
# for v in lista:
#   h.insere(v)
# print("\nHeap original:")
# print(h)

pacientes_1 = [
    {"dthr": "2024-05-30 12:39:01", "nome": "José",   "grav": 2},
    {"dthr": "2024-05-30 12:42:03", "nome": "Márcia", "grav": 3},
    {"dthr": "2024-05-30 12:42:06", "nome": "André",  "grav": 2},
    {"dthr": "2024-05-30 12:43:10", "nome": "Bruna",  "grav": 5}
]
pacientes_2 = [
    {"dthr": "2024-05-30 12:39:15", "nome": "Ana",    "grav": 5},
    {"dthr": "2024-05-30 12:40:21", "nome": "Carlos", "grav": 4},
    {"dthr": "2024-05-30 12:42:28", "nome": "Diego",  "grav": 3},
    {"dthr": "2024-05-30 12:42:36", "nome": "Elaine", "grav": 2},
    {"dthr": "2024-05-30 12:43:45", "nome": "Fábio",  "grav": 1}
]
fila_pacientes_1 = Heap(chave=chave_paciente, max_heap=True)
fila_pacientes_2 = Heap(chave=chave_paciente, max_heap=True)

# adicionando os pacientes
for p in pacientes_1:
    fila_pacientes_1.insere(p)

for p in pacientes_2:
    fila_pacientes_2.insere(p)

# mesclando
fila_pacientes_1.mescla(fila_pacientes_2)

print("\nNiveis do heap mesclado", fila_pacientes_1.niveis())
print("\n\nHeap resultante:\n")
print(fila_pacientes_1)