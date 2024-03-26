grafo = { #tabela hash de ligações realizadas no grafo
        'I': {'A' : 5, 'B' : 2},
        'A': {'C' : 4, 'D' : 2},
        'B': {'A' : 8, 'D' : 7},
        'C': {'F' : 3, 'D' : 6},
        'D': {'F' : 1},
        'F': {}
        }
pais ={ #tabela hash responsavel por armazenar o vertice-pai de outro vertice a partir do menor caminho para encontra-lo
    'A' : 'I',
    'B' : 'I',
    'C' : None,
    'D' : None,
    'F' : None,
}
infinito = float("inf")
custos = { #tabela onde serao atualizados os custos para se chegar em cada vertice
    'A' : 5,
    'B' : 2,
    'C' : infinito,
    'D' : infinito,
    'F' : infinito
}
processados = []
def ache_custo_mais_baixo(custos)-> str:
    menor = infinito
    vertice_mais_barato = None
    for vertice in custos:
        custo = custos[vertice]
        if custo < menor and vertice not in processados:
            menor = custo
            vertice_mais_barato = vertice
    return vertice_mais_barato
def impirimir_caminho(pais:dict):
    path = ['F']
    while 'I' not in path:
        index = len(path) - 1
        pai = pais[path[index]]
        path.append(pai)
    print(path[::-1])

def algoritmo_de_Djikstra(grafo:dict,custos,pais):
    vertice = ache_custo_mais_baixo(custos)
    while vertice is not None:
        custo_vertice =  custos[vertice]
        vizinhos = grafo[vertice]
        for i in vizinhos.keys():
            novo_custo = custo_vertice + vizinhos[i]
            if custos[i] > novo_custo:
                pais[i] = vertice
                custos[i] = novo_custo 
        processados.append(vertice)
        vertice = ache_custo_mais_baixo(custos)
    impirimir_caminho(pais)
algoritmo_de_Djikstra(grafo, custos, pais)