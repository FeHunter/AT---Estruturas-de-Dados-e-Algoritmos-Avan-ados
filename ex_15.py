def maior_produto(array):
  #pegar os maiores numeros
  maior_n1 = float('-inf')
  maior_n2 = float('-inf')

  # pegar os menores
  menor_n1 = float('inf')
  menor_n2 = float('inf')

  for n in array:
    # atualiza os maiores
    if n > maior_n1:
      maior_n2 = maior_n1
      maior_n1 = n
    elif n > maior_n2:
      maior_n2 = n

    # atualiza os menores
    if n < menor_n1:
      menor_n2 = menor_n1
      menor_n1 = n
    elif n < menor_n2:
      menor_n2 = n

  # compara melhor produto
  produto_positivos = maior_n1 * maior_n2
  produto_negativos = menor_n1 * menor_n2

  return max(produto_positivos, produto_negativos)

array_1 = [5, -10, -6, 9, 4]
print(f"Maior produto é {maior_produto(array_1)}")