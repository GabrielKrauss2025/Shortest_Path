from parte_5 import dijkstra

def reconstruir_caminho(anterior, s, t):
    caminho = [t]
    v = t
    while v != s:
        v = anterior[v]
        caminho.append(v)
    return caminho[::-1]

