def quicksort(lista:list)->list:
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        lista_menores = []
        lista_maiores = []
        for item in lista:
            if pivo > item:
                lista_menores.append(item)
            elif pivo < item:
                lista_maiores.append(item)
        return quicksort(lista_menores)+ [pivo] + quicksort(lista_maiores)
    
print(quicksort([12,13,34,11]))
        