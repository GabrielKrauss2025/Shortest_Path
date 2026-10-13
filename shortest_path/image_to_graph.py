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

def cria_celulas_paredes(num_celulas, lab):
    n_celulas = num_celulas 
    n_grade = n_celulas * 2 + 1  

    altura, largura = lab.shape

    celulas = np.empty((n_celulas, n_celulas), dtype=object)
    
    for i in range(n_celulas):
        for j in range(n_celulas):
            linha_grade = i * 2 + 1
            col_grade = j * 2 + 1
            
            # Coordenadas em pixels
            y_inicio = round(linha_grade * altura / n_grade)
            y_fim = round((linha_grade + 1) * altura / n_grade)
            y_centro = round((y_inicio + y_fim) / 2)

            x_inicio = round(col_grade * largura / n_grade)
            x_fim = round((col_grade + 1) * largura / n_grade)
            x_centro = round((x_inicio + x_fim) / 2)
            
            celulas[i, j] = {
                "id": i * n_celulas + j + 1, 
                "pixels": lab[x_inicio:x_fim, y_inicio:y_fim], 
                "centro": [x_centro, y_centro]
            }
        
    return celulas

def verifica_vizinhos_horizontal(celulas, lab):
    n = celulas.shape[0] 
    passagens_hor = {}

    # Para horizontal: i (linhas) vai até n, j (colunas) vai até n-1
    for i in range(n):
        for j in range(n - 1): 
            # A linha Y é a mesma, tiramos a média do X (coluna) entre a célula e seu vizinho à direita
            y_centro = celulas[i, j]["centro"][0]
            x_centro = round((celulas[i, j]["centro"][1] + celulas[i, j+1]["centro"][1]) / 2)

            # Verifica o pixel intermediário na matriz (índices: linha, coluna)
            if lab[y_centro, x_centro] == 1: # 1 significa região livre[cite: 2]
                id1 = celulas[i, j]["id"]
                id2 = celulas[i, j+1]["id"]
                
                # Adiciona as conexões (grafo não-direcionado)
                passagens_hor.setdefault(id1, []).append(id2)
                passagens_hor.setdefault(id2, []).append(id1)

    return passagens_hor


'''
M = carregar_labirinto("labirinto.png")

celulas = cria_celulas(20, M) 

# Cria a pasta 'img' um nível acima do diretório atual
os.makedirs('../img', exist_ok=True)

plt.figure()
plt.axis('off')
plt.imshow(M, cmap='gray')
plt.title('Imagem binária do labirinto')

x_coords = [celulas[i, j]["centro"][1] for i in range(20) for j in range(20)]
y_coords = [celulas[i, j]["centro"][0] for i in range(20) for j in range(20)]

# Plotando os centros
plt.scatter(x_coords, y_coords, c='red', s=35)

plt.savefig('../img/labirinto_binario_celulas.png', dpi=150, bbox_inches='tight')
plt.show()