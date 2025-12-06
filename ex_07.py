from collections import deque

movs = [
    (1, 2), (2, 1), (2, -1), (1, -2),
    (-1, -2), (-2, -1), (-2, 1), (-1, 2)
]

def converter(pos):
    ''' converte as casas do tabuleiro em coordenadas '''
    return ord(pos[0]) - ord('a'), int(pos[1]) - 1

def menor_movimentos(inicio, fim):
    if inicio == fim:
        return 0

    inicio = converter(inicio)
    fim = converter(fim)

    # o -1 e o não visitado
    dist = [[-1] * 8 for _ in range(8)]

    fila = deque([inicio])
    dist[inicio[1]][inicio[0]] = 0

    while fila:
        x, y = fila.popleft()

        for dx, dy in movs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 8 and 0 <= ny < 8 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                fila.append((nx, ny))

                if (nx, ny) == fim:
                    return dist[ny][nx]

print("a1 - h7 =", menor_movimentos("a1", "h7"))
print("h8 - a1 =", menor_movimentos("h8", "a1"))
print("b1 - c3 =", menor_movimentos("b1", "c3"))
print("f6 - f6 =", menor_movimentos("f6", "f6"))