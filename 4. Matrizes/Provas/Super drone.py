"""
A Amazônia é grande e exuberante por natureza.
Para fazer um levantamento das espécies de árvores,
os cientistas desensolveram um super drone que é capaz de sobrevoar uma determinada região e catalogar quantas espécies diferentes de
árvores existem por quilômetro quadrado.
------------------

Sua tarefa é, dada uma lista de coordenadas no mapa onde está sendo feito o levantamento,
determine quantas espécies de árvores existem dentro daquelas áreas.
---------------------

Entrada

A entrada será primeiramente um inteiro ‘N’ (4 <= N <= 10), representando as dimensões do mapa.
Cada uma das ‘N’ linhas seguintes possuirá ‘N’ inteiros ‘Q’ (100 <= Q <= 1000), separados por espaço.

A seguir será dado um inteiro ‘C’ (1 <= C <= N*N), que representa o número de coordenadas a serem verificadas.

Por fim, serão dadas ‘C’ linhas, onde em cada uma serão dados dois inteiros ‘X’ e ‘Y’ (0 <= X, Y <= N-1),
representando as coordenadas a serem verificadas pelo drone,
sendo que ‘X’ representa determinada linha e ‘Y’ representa determinada coluna no mapa.

Cada coordenada no mapa representa uma região de 1 KM².

Cada inteiro ‘Q’ em cada posição do mapa indica o número de espécies de árvores naquela coordenada.
Não serão dadas duas coordenadas iguais a serem verificadas.
----------------

Saída

Você deverá imprimir a quantidade de espécies verificadas em todas as
coordenadas solicitadas no mapa.
--------------------------------------------
Entrada                         Saída
4                               500
100 200 300 400
100 200 300 400
400 300 200 100
400 300 200 100
3
0 2
2 3
3 3
"""

a = 0
b = 0
c = 0
d = 0
lista_soma = []

N = int(input())
matriz_mapa = []
for i in range(N):
    linha = [int(x) for x in input().split()]
    matriz_mapa.append(linha)

C = int(input())
matriz_cord = []
for i in range(C):
    a, b = input().split()

    a = int(a)
    b = int(b)

    for p in range(1):
        for p in range(1):
            lista_soma.append(matriz_mapa[a][b])

print(sum(lista_soma))