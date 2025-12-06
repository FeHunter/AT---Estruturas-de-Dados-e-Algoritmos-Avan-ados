def iguais(array1, array2):
  # se não forem do mesmo tamanho não são iguais
  if len(array1) != len(array2):
    return False

  cont1 = {}
  cont2 = {}

  # conta elementos do array1
  for num in array1:
    cont1[num] = cont1.get(num, 0) + 1

  # conta elementos do array2
  for num in array2:
    cont2[num] = cont2.get(num, 0) + 1

  # compara as duas tabelas de frequência
  return cont1 == cont2

array_1 = [2, 4, 9, 3, 10]
array_2 = [3, 4, 10, 2, 9]

print(f"São iguais: {iguais(array_1, array_2)}")
