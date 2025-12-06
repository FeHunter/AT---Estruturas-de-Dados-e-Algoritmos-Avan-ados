from collections import deque

def bfs(start_i, start_j, grid, visitado, altura, largura):
    fila = deque([(start_i, start_j)])
    visitado[start_i][start_j] = True

    # array com os movimentos  cima, baixo, esquerda, direita
    movs = [(1,0), (-1,0), (0,1), (0,-1)]

    while fila:
        i, j = fila.popleft()

        for di, dj in movs:
            ni, nj = i + di, j + dj

            if 0 <= ni < altura and 0 <= nj < largura:
                if grid[ni][nj] == '.' and not visitado[ni][nj]:
                    visitado[ni][nj] = True
                    fila.append((ni, nj))

def contar_cliques(altura, largura, grid):
    visitado = [[False] * largura for _ in range(altura)]
    cliques = 0

    for i in range(altura):
        for j in range(largura):
            if grid[i][j] == '.' and not visitado[i][j]:
                cliques += 1
                bfs(i, j, grid, visitado, altura, largura)

    return cliques

altura, largura = 6, 9
grid = [
    list(".ooo.ooo."),
    list("o...o...o"),
    list(".o.....o."),
    list("..o...o.."),
    list("...o.o..."),
    list("....o....")
]

print(f"Quantidade de cliques: {contar_cliques(altura, largura, grid)}")