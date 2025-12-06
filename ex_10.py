def componentes_conexas(grafo, limite=float('inf')):
    # pegar as cidades os vertices
    cidade = {v: v for v in grafo}

    trocou = True
    while trocou:
        trocou = False
        for v in grafo:
            for vizinho, peso in grafo[v]:
                if peso <= limite:
                    # quando a  cidade for diferente pegamos a menor
                    if cidade[v] != cidade[vizinho]:
                        r1 = cidade[v]
                        r2 = cidade[vizinho]
                        menor = min(r1, r2)
                        maior = max(r1, r2)
                        # tocar a cidade maior pelo menor
                        for k in cidade:
                            if cidade[k] == maior:
                                cidade[k] = menor
                                trocou = True
    return cidade


def vertices_componente(cidade):
    comp = {}
    for v, rot in cidade.items():
        if rot not in comp:
            comp[rot] = []
        comp[rot].append(v)
    return comp


grafo = {
    'blum': [('cerf', 18), ('dahi', 19)],
    'cerf': [('blum', 18), ('dahi', 17), ('gray', 28), ('kay', 29), ('naur', 51)],
    'dahi': [('blum', 19), ('cerf', 17), ('gray', 26), ('kay', 31)],
    'kay' : [('dahi', 31), ('cerf', 29), ('gray', 11), ('naur', 20)],
    'gray': [('cerf', 28), ('dahi', 26), ('kay', 11), ('naur', 24)],
    'naur': [('gray', 24), ('cerf', 51), ('kay', 20)]
}

for limite in [50, 21, 15]:
    rot = componentes_conexas(grafo, limite)
    comp = vertices_componente(rot)
    print("\nCidades:", rot)
    print("Componentes:", comp)
