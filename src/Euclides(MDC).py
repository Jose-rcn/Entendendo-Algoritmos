def sort(n1:float, n2:float)->list:
    """Ordena dois numeros"""
    if n1 >= n2:
        return [n1,n2]
    return [n2,n1]

def euclides(high:float,wheight:float)->float:
    '''Algoritmo que retorna o lado do maior quadrado que divide igualmente um terrenor retangular como mostrado no algoritmos de euclides'''
    maior = sort(high,wheight)[0]
    menor = sort(high,wheight)[1]

    if maior % menor == 0: # caso base
        return menor
    return euclides(maior % menor,menor) #caso recursivo
print(euclides(21,9))