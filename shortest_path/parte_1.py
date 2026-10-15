from PIL import Image
import matplotlib.pyplot as plt
from heapq import heappop, heappush
import numpy as np
import time
import os

def carregar_labirinto(title):
    # carregar a imagem
    img = Image.open(title)

    # converter para a escala de cinza
    cinza = img.convert('L')

    # transforma em matriz
    M = np.array(cinza)

    # usa um valor de corte para transformar a matriz em binária
    # 0's representam paredes e 1's representam corredores
    M = (M > 128).astype(int)

    # recorta o labirinto
    linha = np.where((M == 0).any(axis=1))[0]
    coluna = np.where((M == 0).any(axis=0))[0]

    topo = linha.min()
    esq = coluna.min()

    M = M[topo:(linha.max() + 1), esq:(coluna.max() + 1)]

    return M, topo, esq

if __name__ == '__main__':
    os.makedirs('../img', exist_ok=True)
    img = Image.open('../img/labirinto.png')

    # apresenta a imagem original
    plt.figure()
    plt.axis('off')
    plt.imshow(img)
    plt.title('Imagem original')
    plt.show()


    # apresenta a imagem binária
    M, topo, esq = carregar_labirinto('../img/labirinto.png')
    plt.figure()
    plt.axis('off')
    plt.imshow(M, cmap='gray')
    plt.title('Imagem binária')
    plt.savefig('../img/labirinto_binario.png', dpi=500, bbox_inches='tight')

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
    plt.scatter((colunas - 1) - tol, (linha_saida.min() + linha_saida.max()) / 2, c='red', s = 35)

    print(f'Entrada: {(0, float((linha_entrada.min() + linha_entrada.max()) / 2))}\nSaída: {(colunas - 1, float((linha_saida.min() + linha_saida.max()) / 2))}')

    # salva a imagem em 'img'
    plt.savefig('../img/labirinto_binario_pontos.png', dpi=500, bbox_inches='tight')
    plt.show()