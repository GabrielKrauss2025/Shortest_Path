from parte_6 import *

if __name__ == '__main__':
    M , topo, esq = carregar_labirinto(IMG / "labirinto.png")

    # imagem original
    original = np.array(Image.open(IMG / "labirinto.png"))

    celulas = cria_celulas(20, M)
    hor = verifica_vizinhos_horizontal(celulas, M)
    ver = verifica_vizinhos_vertical(celulas, M)
    grafo, vertices, arestas = criando_grafo(hor, ver, 20)

    s, t = 1, vertices

    distancia, anterior = dijkstra(grafo, s)
    caminho = reconstruir_caminho(anterior, s, t)

    # centros em coordenadas da imagem original
    centros = {v: (celulas[v]["centro"][0] + esq, celulas[v]["centro"][1] + topo) for v in celulas}

    # apenas o caminho mínimo sobre o labirinto
    plt.figure()
    plt.axis('off')
    plt.imshow(original)
    plt.title('Apenas caminho mínimo')

    # plotando as arestas do grafo
    for u in caminho:
        x1, y1 = centros[u]
        for v in grafo[u]:
            if u < v and v in caminho:
                x2, y2 = centros[v]
                plt.plot([x1, x2], [y1, y2], color='blue', linewidth=1.5)

    # desenha os vértices
    x_coords = [centros[v][0] for v in caminho]
    y_coords = [centros[v][1] for v in caminho]

    plt.scatter(x_coords[1:-1], y_coords[1:-1], c='orange', s=15, zorder=2)
    plt.scatter(x_coords[0], y_coords[0], c='green', s=35, zorder=2)
    plt.scatter(x_coords[-1], y_coords[-1], c='red', s=35, zorder=2)

    # salva a imagem em 'img'
    plt.savefig(IMG / 'apenas_caminho_minimo.png', dpi=500, bbox_inches='tight')
    plt.show()


    # grafo completo com caminho mínimo destacado
    plt.figure()
    plt.axis('off')
    plt.imshow(original)
    plt.title('Grafo com caminho mínimo')

    # plotando as arestas do grafo
    for u in celulas:
        x1, y1 = centros[u]
        for v in grafo[u]:
            if u < v:
                x2, y2 = centros[v]
                if u in caminho and v in caminho:
                    plt.plot([x1, x2], [y1, y2], color='red', linewidth=1.5)
                else:
                    plt.plot([x1, x2], [y1, y2], color='blue', linewidth=1.5)

    # desenha os vértices
    x_coords = [centros[v][0] for v in centros]
    y_coords = [centros[v][1] for v in centros]

    plt.scatter(x_coords[1:-1], y_coords[1:-1], c='black', s=15, zorder=2)
    plt.scatter(x_coords[0], y_coords[0], c='green', s=35, zorder=2)
    plt.scatter(x_coords[-1], y_coords[-1], c='red', s=35, zorder=2)

    x_coords = [centros[v][0] for v in celulas if v not in caminho]
    y_coords = [centros[v][1] for v in celulas if v not in caminho]
    plt.scatter(x_coords, y_coords, c='orange', s=15, zorder=2)


    # salva a imagem em 'img'
    plt.savefig(IMG / 'grafo_com_caminho_minimo.png', dpi=500, bbox_inches='tight')
    plt.show()