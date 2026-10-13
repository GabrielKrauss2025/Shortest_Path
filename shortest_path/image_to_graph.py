from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

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

M = carregar_labirinto("labirinto.png")
n = 20
altura, largura = M.shape
celulas = np.empty((n,n), dtype=object)

for i in range(n):
    for j in range(n):
        y_inicio = round(i * altura / n)
        y_fim = round((i+1) * altura / n)

        x_inicio = round(j * altura / n)
        x_fim = round((j+1) * altura / n)

        celulas[i, j] = {"id" : i*n + j + 1, "pixels" : M[y_inicio:y_fim, x_inicio:x_fim]}

print(celulas.shape)
print(celulas[0, 0]["id"])
print(np.unique(celulas[0, 0]["pixels"], return_counts=True))
