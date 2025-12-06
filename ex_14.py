def numero_faltante(array):
    N = len(array)
    soma_total = N * (N + 1) // 2
    soma_array = sum(array)
    return soma_total - soma_array

array_1 =  [2, 3, 0, 6, 1, 5]
array_2 = [8, 2, 3, 9, 4, 7, 5, 0, 6]

print(f"Numero faltando: {numero_faltante(array_1)}")
print(f"Numero faltando: {numero_faltante(array_2)}")
