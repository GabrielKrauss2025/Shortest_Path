from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# carrega a imagem
img = Image.open('labirinto.png')

# apresenta a imagem original
plt.figure()
plt.imshow(img)
plt.title('Imagem original do labirinto')
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
plt.imshow(M, cmap='gray')
linhas, colunas = M.shape
tol = 5
# entrada
linha_entrada = np.where(M[:, 0] == 1)[0]
if linha_entrada.size == 0:
    raise ValueError('Labirinto inválido')
print(f'Ponto de entrada: {(0, float((linha_entrada.min() + linha_entrada.max()) / 2))}')
plt.scatter(0 + tol, (linha_entrada.min() + linha_entrada.max()) / 2, c='green', s = 35)

# saída
linha_saida = np.where(M[:, -1] == 1)[0]
if linha_saida.size == 0:
    raise ValueError('Labirinto inválido')
print(f'Ponto de saída: {(colunas, float((linha_saida.min() + linha_saida.max()) / 2))}')
plt.scatter(colunas - tol, (linha_saida.min() + linha_saida.max()) / 2, c='red', s = 35)
plt.title('Imagem binária do labirinto')
plt.show()
