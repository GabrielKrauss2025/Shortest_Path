from parte_2 import carregar_labirinto, cria_celulas, verifica_vizinhos_horizontal, verifica_vizinhos_vertical, criando_grafo
import matplotlib.pyplot as plt
import os

M = carregar_labirinto("../img/labirinto.png")

celulas = cria_celulas(20, M)
hor = verifica_vizinhos_horizontal(celulas, M)
ver = verifica_vizinhos_vertical(celulas, M)
grafo, vertices, arestas = criando_grafo(hor, ver)

plt.figure(figsize=(8, 8))
plt.axis('off')
plt.imshow(M, cmap='gray')
plt.title('Grafo do Labirinto (Vértices e Arestas)')

# Plotando as arestas do grafo
for u in grafo:
    x1, y1 = celulas[u]["centro"]
    for v in grafo[u]:
        if u < v:
            x2, y2 = celulas[v]["centro"]
            plt.plot([x1, x2], [y1, y2], color='blue', linewidth=1.5)

# Desenha os vértices
x_coords = [celulas[v]["centro"][0] for v in celulas]
y_coords = [celulas[v]["centro"][1] for v in celulas]

plt.scatter(x_coords[1:-1], y_coords[1:-1], c='orange', s=25, zorder=2)
plt.scatter(x_coords[0], y_coords[0], c='green', s=30, zorder=2)
plt.scatter(x_coords[-1], y_coords[-1], c='red', s=30, zorder=2)

# Salva a imagem em 'img'
os.makedirs('../img', exist_ok=True)
plt.savefig('../img/labirinto_grafo_completo.png', dpi=150, bbox_inches='tight')
plt.show()