import numpy as np
import random
import matplotlib.pyplot as plt

K = 10 # Número de formigas
alpha = 1 # Influência do feromônio
beta = 1 # Influência da distância
max_iteracoes = 100
rho = 0.5 # Taxa de evaporação
Q = 1 # Feromonio liberado por cada formiga por iteração

formiga_escolhida = 4

# Grafo de busca
G = np.array([(0, 2, 0, 3, 6), (2, 0, 4, 3, 0), (0, 4, 0, 7, 3), (3, 3, 7, 0, 3), (6, 0, 3, 3, 0)])


dist_hist = []

ferom = np.ones((G.shape[0], G.shape[0])) # Matriz de feromônio, indica a quantidade de feromônio na aresta i, j.

def atualizaFerom():
    global ferom
    feromX = np.zeros((G.shape[0], G.shape[0])) # Matriz de feromonios provisória

    for k in range (0, K): # Para cada formiga
        Dferom = Q / formigas_dist[k] # Delta tal (quantidade de feromonio que a formiga vai colocar)

        for l in range(1, len(formigas_caminho[k])): # Iterar na rota da formiga k
            i = formigas_caminho[k][l-1]
            j = formigas_caminho[k][l]
            feromX[i][j] += Dferom # Inserindo o feromonio da formiga k na aresta ij da matriz provisória

    ferom = (1 - rho) * ferom + feromX # Atualizando a matriz de feromonio segundo a equação (2)    


def verificaEstag():
    if(len(dist_hist) > 10):
        if((dist_hist[-10: len(dist_hist) - 1] == dist_hist[-1]).all()):
            return 1
    
    return 0

def roleta(prob):
    r = random.random() # Define o valor aleatorio [0-1]
    contador = 0
    soma = 0
    
    while (soma <= r): # Enquanto a soma for menor do que o valor escolhido        
        soma += prob[contador] # probabilidade da aresta

        contador += 1 

    return contador - 1

atratividade = np.zeros((G.shape[0], G.shape[0]))
for i in range(0, G.shape[0]):
    for j in range(0, G.shape[0]):
        if(G[i][j] != 0):             
            atratividade[i][j] = 1 / G[i][j]

cont = 0
estag = 0
while cont < max_iteracoes and estag == 0:

    formigas_caminho = [[np.random.randint(0, G.shape[0])] for i in range(0, K)] # Lista de vertices do caminho atual das formigas
    formigas_dist = np.zeros(K) # Disitancia total do caminho atual das formigas
    
    for k in range(0, K): # iterar nas formigas (Para cada formiga)
        atratividade_k = np.copy(atratividade) # Cada formiga cria uma cópia da matriz de atratividade para mapear para onde já foi, colocando 0 de atratividade neste local, desta forma a probabilidade deste será 0

        if(k == formiga_escolhida):
            print(f'\n\n{"-"*80}\nIteração {cont}\n')

        for i in range(0, G.shape[0]):
            vi = formigas_caminho[k][i] # Vertice atual da formiga
            atratividade_k.T[vi] = 0 # Zerar a coluna do vertice atual, indicando que ele já foi alcançado
                
            if (np.sum(atratividade_k[vi]) == 0): # somatorio de atratividade = 0, significa que chegou no último vertice                        
                prox = formigas_caminho[k][0] # Volta para a primeira cidade
            else:
                prob = (ferom[vi] ** alpha * atratividade_k[vi] ** beta) / (ferom[vi] ** alpha).dot((atratividade_k[vi] ** beta).T) # Vetor de probabilidades das arestas partindo de vi
                            
                prox = roleta(prob)
                
                if(k == formiga_escolhida):
                    print(f'Vértice {vi}\n Probabilidades: {prob}\nVértice escolhido: {prox}\n')


            formigas_caminho[k].append(prox) # Adicionar o próximo vertice no caminho da formiga (Ir para o próximo vértice) 
            
            formigas_dist[k] += G[vi][prox] # Atualizar a distância total do caminho parcial da formiga.

    
    print(f'Caminho: {formigas_caminho[formiga_escolhida]}\nCusto do caminho: {formigas_dist[formiga_escolhida]}\n\n{"-"*80}')
            
    dist_hist.append(formigas_dist)
    atualizaFerom()
    estag = verificaEstag()

    cont += 1

    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    plt.clf()
    plt.imshow(ferom)    
    plt.title(f'Matriz de Feromônio da iteração {cont}')
    plt.xlabel("Vértice j")
    plt.ylabel("Vértice i")
    plt.colorbar()
    plt.pause(0.05)

print(f'\n\nSolução\nCaminho: {formigas_caminho[0]}\nCusto da solução: {formigas_dist[0]}\nTotal de iterações: {cont}')

plt.show()
