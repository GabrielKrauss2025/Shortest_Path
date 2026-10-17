# RELATÓRO - LISTA COMPUTACIONAL 2

**Período 2.2 - Otimização Linear**

Autores: André Felipe Oliveira, Davi Pestana, Felipe Ribeiro, Gabriel Krauss

**IMPA Tech**

## 1. Introdução

O objetivo dessa atividade é transformar a imagem de um labirinto em uma estrutura de grafo, com o intuito de resolver o problema de caminho mínimo entre a entrada e a saída. Com essa modelagem reduzimos o problema a apenas aplicar um algoritmo conhecido para esse problema em grafos, como o algoritmo Dijkstra.

Em nosso problema são permitidos apenas movimentos cardeais, sendo os movimentos diagonais desconsiderados. No nosso problema as arestas não possuem peso, com isso, o custo de cada caminho é apenas o seu deslocamento (custo 1).

![Figura 1 - Labirinto oiriginal](img/labirinto.png)

*Figura 1 - Labirinto oiriginal*

## 2. Tratamento da imagem

### 2.1. Criando a imagem binária

Inicialmente, carregamos a imagem e convertemos para a escala de cinza para tirar imperfeições dos pixels, após isso transformamos o resultado do processo em uma matriz, usando um valor de corte para binarizá-la. Com isso, recortamos o labirinto seguindo a seguinte regra:

![Figura 2 - Labirinto com pontos de entrada e saída](img/labirinto_binario_pontos.png)

*Figura 2 - Labirinto com pontos de entrada e saída*

Identificamos a entrada e saída do grafo tomando o primeiro pixel 0 da primeira e da última coluna, respectivamente, com uma tolerância para os pontos serem dentro do labirinto.

### 2.2. Criando as células e construção das arestas

Após isso, criamos uma grade de células, nomeando-as segundo o identificador indicado na atividade, sendo ele:

A partir disso, construímos as arestas analisando o ponto médio entre as coordenadas do centro de duas células vizinhas. Caso o pixel resultante seja 1 é uma região livre, então ligamos as duas com uma aresta, caso contrário o pixel é 0 então é uma parede não sendo feita uma aresta. Criamos o grafo com o identificador das células como vértices e o conjunto de arestas que obtemos ao verificar as células vizinhas.

Finalizamos com um total de 400 vértices e 399 arestas no grafo final.

![Figura 3 - Labirinto com grafo completo sobreposto](img/labirinto_grafo_completo.png)

*Figura 3 - Labirinto com grafo completo sobreposto*

## 3. Funcionamento do Dijkstra

O algoritmo de Dijkstra calcula as distâncias mínimas a partir de um vértice inicial em um grafo com pesos não negativos, sendo aplicável no nosso caso, tendo em vista que todas as arestas possuem peso 1.

Iniciamos o algoritmo definindo o vértice inicial, sendo no caso o vértice 1. Sua distância é definida como zero e as distâncias dos demais vértices como infinito. Além disso, também inicializamos o dicinário anterior, que será usado para guardar o pai de cada vértice.

Adicionamos o vérticie inicial a um heap-min auxiliar D, sendo a distância o parâmetro para ordenação. Enquanto D tiver elementos fazemos as seguintes ações:

- Pegamos a distância e o vértice de maior prioridade.
- Verificamos se a distância provisória é maior que a distância atual, caso seja não olhamos para seus vizinhos, do contrário, seguimos.
- Para cada vizinho do vérticie atual, caso a distância provisória + 1 seja menor que a atual distância para aquele vizinho atualizaremos a distância e adicionaremos o vértice atual como pai do vértice vizinho.
- Por fim, adicionamos o vizinho ao heap-min auxiliar D.

A execução termina quando não há mais vértices alcançáveis, isto é, quando o heap-min auxiliar D for vazio, retornando as distâncias de cada vértice e o pai de cada um deles.

## 4. O caminho mínimo

Tendo em vista que o Dijkstra retorna a distância e o pai de cada vértice, reconstruímos o caminho mínimo partindo do vértice final até o inicial pelos pais de cada um deles, sendo analisados sucessivamente. Assim, basta inverter a lista obtida e conseguimos listar todos os vértices que estão contidos no caminho mínimo em ordem, além de ao tomar dois vértices consecutivos obtemos as arestas que compõem o caminho.

Observe na imagem ao lado o caminho mínimo encontrado pelo algoritmo de Dijkstra.

![Figura 4 - Labirinto com caminho mínimo sobreposto](img/apenas_caminho_minimo.png)

*Figura 4 - Labirinto com caminho mínimo sobreposto*

## 5. Análise dos resultados

Ao representarmos o labirinto por um grafo possibilitamos um estudo formal da conectividade e do cálculo de rotas. A análise visual do grafo sobre a imagem original também é importante principalmente para verificar a corretude das funções, avaliando se porventura alguma aresta foi construída de maneira indevida.

Com isso, avaliamos experimentalmente a eficiência da modelagem do labirinto como um grafo, tendo sido determinado pelo algoritmo o menor caminho composto por 123 vértices e 122 arestas em um tempo de execução de apenas 0,0001725 segundos. Como as arestas não possuem pesos temos que o tamanho do caminho é o custo dele, totalizando um custo de 122 passos.

A relação entre as arestas e os vértices nos mostra uma trajetória simples e sem ciclos, além do tempo em microsegundos evidenciar que a abstração da imagem para uma estrutura discreta reduziu significativamente o custo computacional do problema.

![Figura 5 - Labirinto com caminho mínimo no grafo completo sobreposto](img/grafo_com_caminho_minimo.png)

*Figura 5 - Labirinto com caminho mínimo no grafo completo sobreposto*