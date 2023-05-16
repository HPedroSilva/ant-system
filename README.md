# Ant System

Implementação do método Ant Colony Optimization (ACO), utilizando o algoritmo Ant System (AS)

Essa implementação foi elaborada como trablho para a disciplina Computação Evolutiva do Curso de Engenharia de Sistemas. Mais informações teóricas sobre o algoritmo estão disponíveis na apresentação: [Apresentação](https://docs.google.com/presentation/d/1oCK0AXxGpf-7CY_4ONQEj0xMJBodaYio/edit?usp=share_link&ouid=104123748249703012457&rtpof=true&sd=true)

O algoritmo está implementado de forma bastante simplificada, com parâmetros e grafo de busca inicial fixados no código, pois o foco era somente no algoritmo em si. Durante sua execução, esta implementação exibe um gráfico, em formato de matriz, representando o nível de feromônio em cada aresta, de forma a demonstrar a evolução da identificação do melhor caminho utilizando o AS. São exibidos também, para uma determinada formiga, em cada iteração do algoritmo, as probabilidades associadas a escolha cada vértice, o vértice atual e o vértice escolhido para a próxima iteração da formiga. Por fim, o algoritmo exibe a solução contendo: o caminho, o custo e o total de iterações.
