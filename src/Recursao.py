def fat(n:int)->int:
    """Algoritmo que usa recursão para calcular o fatorial de um numero inteiro"""
    if n == 1:
        return
    return n * fat(n-1)
print(fat(3))