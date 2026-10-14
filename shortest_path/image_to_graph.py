from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def carregar_labirinto(title):
    # Ler a imagem
    img = Image.open(title)
    
    # Converter para cinza
    cinza = img.convert('L')

    # Transforma em matriz
    M = np.array(cinza)

    # Usa um valor de corte para transformar a matriz em binária
    # 0's representam paredes e 1's representam corredores
    M = (M > 128).astype(int)

    # Recorta a matriz
    linha = np.where((M == 0).any(axis=1))[0]
    coluna = np.where((M == 0).any(axis=0))[0]
    M = M[linha.min():(linha.max() + 1), coluna.min():(coluna.max()+1)]

    return M

import numpy as np

def cria_celulas(num_celulas, lab):
    n_celulas = num_celulas 
    n_grade = n_celulas * 2 + 1  
    altura, largura = lab.shape

    # Dicionário indexado pelo ID (1 a 400)
    celulas = {} 
    
    for i in range(n_celulas):
        for j in range(n_celulas):
            linha_grade = i * 2 + 1
            col_grade = j * 2 + 1
            
            y_inicio = round(linha_grade * altura / n_grade)
            y_fim = round((linha_grade + 1) * altura / n_grade)
            y_centro = round((y_inicio + y_fim) / 2)

            x_inicio = round(col_grade * largura / n_grade)
            x_fim = round((col_grade + 1) * largura / n_grade)
            x_centro = round((x_inicio + x_fim) / 2)
            
            # ID no padrão 1 a 400
            id_celula = i * n_celulas + j + 1
            
            celulas[id_celula] = {
                "i": i,
                "j": j,
                "pixels": lab[y_inicio:y_fim, x_inicio:x_fim], 
                "centro": [x_centro, y_centro]
            }
        
    return celulas

def verifica_vizinhos_horizontal(celulas, lab):
    n = max(c["i"] for c in celulas.values()) + 1
    passagens_hor = {}

    for i in range(n):
        for j in range(n - 1): 
            id1 = i * n + j + 1
            id2 = i * n + (j + 1) + 1 # Célula à direita
            
            # Pega o centro diretamente pelo ID
            y_centro = celulas[id1]["centro"][1]
            x_centro = round((celulas[id1]["centro"][0] + celulas[id2]["centro"][0]) / 2)

            if lab[y_centro, x_centro] == 1: 
                passagens_hor.setdefault(id1, []).append(id2)
                passagens_hor.setdefault(id2, []).append(id1)

    return passagens_hor

def verifica_vizinhos_vertical(celulas, lab):
    n = max(c["i"] for c in celulas.values()) + 1
    passagens_ver = {}

    for i in range(n-1):
        for j in range(n): 
            id1 = i * n + j + 1
            id2 = (i + 1) * n + j + 1 # Célula à direita
            
            # Pega o centro diretamente pelo ID
            x_centro = celulas[id1]["centro"][0]
            y_centro = round((celulas[id1]["centro"][1] + celulas[id2]["centro"][1]) / 2)

            if lab[y_centro, x_centro] == 1: 
                passagens_ver.setdefault(id1, []).append(id2)
                passagens_ver.setdefault(id2, []).append(id1)

    return passagens_ver

def criando_grafo(hor, ver):
    grafo = {}
    for id_no in range(1, 401):
        viz_hor = hor.get(id_no, [])
        viz_ver = ver.get(id_no, [])
        
        grafo[id_no] = list(set(viz_hor).union(set(viz_ver))) 
        
    vertices = len(grafo)
    arestas = 0

    for v in grafo:
        for viz in grafo[v]:
            if v < viz:
                arestas += 1

    return grafo, vertices, arestas  

M = carregar_labirinto("labirinto.png")

celulas = cria_celulas(20, M) 
hor = verifica_vizinhos_horizontal(celulas, M)

ver = verifica_vizinhos_vertical(celulas, M)
grafo, vertices, arestas = criando_grafo(hor, ver)
print(vertices, arestas)

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

plt.scatter(x_coords, y_coords, c='red', s=25, zorder=2)

# Salva a imagem em 'img' 
os.makedirs('../img', exist_ok=True)
plt.savefig('../img/labirinto_grafo_completo.png', dpi=150, bbox_inches='tight')
plt.show()




