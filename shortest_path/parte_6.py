from parte_5 import *
import time

def reconstruir_caminho(anterior, s, t):
    caminho = [t]
    v = t
    while v != s:
        v = anterior[v]
        caminho.append(v)
    return caminho[::-1]

if __name__ == '__main__':
    M, topo, esq = carregar_labirinto(IMG / "labirinto.png")

    celulas = cria_celulas(20, M)
    hor = verifica_vizinhos_horizontal(celulas, M)
    ver = verifica_vizinhos_vertical(celulas, M)
    grafo, vertices, arestas = criando_grafo(hor, ver, 20)
    s, t = 1, vertices

    inicio = time.perf_counter()
    distancia, anterior = dijkstra(grafo, s)
    fim = time.perf_counter()
    caminho = reconstruir_caminho(anterior, s, t)
    print(f'Custo do caminho mínimo: {distancia[t]}')
    print(f'Número de movimentos realizados: {len(caminho) - 1}')
    print(f'Número de vértices pertencentes ao caminho mínimo: {len(caminho)}')
    print(f'Tempo total: {fim - inicio} s')
