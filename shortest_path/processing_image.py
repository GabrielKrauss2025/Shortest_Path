from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# carrega a imagem
img = Image.open('../img/labirinto.png')

# apresenta a imagem original
plt.figure()
plt.axis('off')
plt.imshow(img)
plt.title('Imagem original do labirinto')

os.makedirs('../img', exist_ok=True)
plt.savefig('../img/labirinto_original.png', dpi=150, bbox_inches='tight')
plt.show()

# converte a imagem para a escala de cinza
cinza = img.convert('L')

# transforma a imagem em uma matriz
M = np.array(cinza)

# utiliza um valor de corte para transformar a matriz em binária
# 0's representam paredes e 1's representam corredores
M = (M > 128).astype(int)

# recorta a matriz
linha = np.where((M == 0).any(axis=1))[0]
coluna = np.where((M == 0).any(axis=0))[0]
M = M[linha.min():(linha.max() + 1), coluna.min():(coluna.max()+1)]


# apresenta a imagem binária
plt.figure()
plt.axis('off')
plt.imshow(M, cmap='gray')
plt.title('Imagem binária do labirinto')

plt.savefig('../img/labirinto_binario.png', dpi=150, bbox_inches='tight')
linhas, colunas = M.shape
tol = 5

# entrada
linha_entrada = np.where(M[:, 0] == 1)[0]
if linha_entrada.size == 0:
    raise ValueError('Labirinto inválido')
plt.scatter(0 + tol, (linha_entrada.min() + linha_entrada.max()) / 2, c='green', s = 35)

# saída
linha_saida = np.where(M[:, -1] == 1)[0]
if linha_saida.size == 0:
    raise ValueError('Labirinto inválido')
plt.scatter(colunas - tol, (linha_saida.min() + linha_saida.max()) / 2, c='red', s = 35)

# Salva a imagem em 'img' 
plt.savefig('../img/labirinto_binario_pontos.png', dpi=150, bbox_inches='tight')
plt.show()


