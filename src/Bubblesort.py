#estudo sobre algoritmos de ordenação
lista = [10,8,12, 12, 1, 2, 44, 3, 2, 90, 12, 13, 2]

def bubble_sort(lista:list) -> list:
    lista_ordenada = lista.copy()
    for i in range(0, len(lista_ordenada,)): # itera sobre os elementos da lista
        for t in range(i +1, len(lista_ordenada)): # a cada elemento, itera sobre seus sucessores
            if lista_ordenada[i] > lista_ordenada[t]: # se o elemento a seguir for maior que o atual os dois trocam de lugar
                lista_ordenada[i], lista_ordenada[t] = lista_ordenada[t], lista_ordenada[i]
    return lista_ordenada
    #algoritmo com notação O(n^2) 

print(bubble_sort(lista))
print(lista)
