from collections import defaultdict, deque

def verificar_biparticao(vertices, arestas):
    cor = {}
    grafo = defaultdict(list)

    for u, v in arestas:
        grafo[u].append(v)
        grafo[v].append(u)

    for v in vertices:
        if v not in cor:
            fila = deque([v])
            cor[v] = 0
            while fila:
                atual = fila.popleft()
                for viz in grafo[atual]:
                    if viz not in cor:
                        cor[viz] = 1 - cor[atual]
                        fila.append(viz)
                    elif cor[viz] == cor[atual]:
                        return False  # dois vizinhos com mesma cor → não é bipartido
    return True

def verificar_planaridade(numero_vertices, arestas):
    numero_arestas = len(arestas)
    vertices = list(set([v for a in arestas for v in a]))

    # Desigualdade de Euler geral
    if numero_vertices <= 3:
        return True

    if verificar_biparticao(vertices, arestas):
        if numero_arestas > 2 * numero_vertices - 4:
            return False
    else:
        if numero_arestas > 3 * numero_vertices - 6:
            return False

    return True


arestas_k5 = [
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 3), (1, 4),
    (2, 3), (2, 4),
    (3, 4)
]

arestas_k33 = [
    (0, 3), (0, 4), (0, 5),
    (1, 3), (1, 4), (1, 5),
    (2, 3), (2, 4), (2, 5)
]

arestas_k4 = [
    (0, 1), (0, 2), (0, 3),
    (1, 2), (1, 3),
    (2, 3)
]

arestas_cubo = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

arestas_piramide = [
    (0, 1), (1, 2), (2, 3), (3, 0),  
    (4, 0), (4, 1), (4, 2), (4, 3)   
]


print("K5 é planar?", verificar_planaridade(5, arestas_k5))       
print("K3,3 é planar?", verificar_planaridade(6, arestas_k33))    
print("K4 é planar?", verificar_planaridade(4, arestas_k4))       
print("Grafo cúbico é planar?", verificar_planaridade(8, arestas_cubo))  
print("Grafo piramide é planar?", verificar_planaridade(5, arestas_piramide))  
