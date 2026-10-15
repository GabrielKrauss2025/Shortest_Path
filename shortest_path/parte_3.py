from parte_2 import *

if __name__ == '__main__':
    M, topo, esq = carregar_labirinto("../img/labirinto.png")

    # imagem original
    original = np.array(Image.open("../img/labirinto.png"))

    celulas = cria_celulas(20, M)
    hor = verifica_vizinhos_horizontal(celulas, M)
    ver = verifica_vizinhos_vertical(celulas, M)
    grafo, vertices, arestas = criando_grafo(hor, ver, 20)

    # centros em coordenadas da imagem original
    centros = {v: (celulas[v]["centro"][0] + esq, celulas[v]["centro"][1] + topo) for v in celulas}

    plt.figure()
    plt.axis('off')
    plt.imshow(original)
    plt.title('Grafo sobreposto ao labirinto')

    # plotando as arestas do grafo
    for u in grafo:
        x1, y1 = centros[u]
        for v in grafo[u]:
            if u < v:
                x2, y2 = centros[v]
                plt.plot([x1, x2], [y1, y2], color='blue', linewidth=1.5)

    # desenha os vértices
    x_coords = [centros[v][0] for v in centros]
    y_coords = [centros[v][1] for v in centros]

    plt.scatter(x_coords[1:-1], y_coords[1:-1], c='orange', s=15, zorder=2)
    plt.scatter(x_coords[0], y_coords[0], c='green', s=35, zorder=2)
    plt.scatter(x_coords[-1], y_coords[-1], c='red', s=35, zorder=2)

    # salva a imagem em 'img'
    plt.savefig('../img/labirinto_grafo_completo.png', dpi=500, bbox_inches='tight')
    plt.show()