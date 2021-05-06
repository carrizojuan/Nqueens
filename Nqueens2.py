#qondaq
#qonda
def validarFila(posreinas):
    for i in range(len(posreinas)):
        if posreinas.count(i) > 1:
            return False
    return True

def validarDiagonal(posreinas):
    diagonalocupadas = []
    for i in range(len(posreinas)):
        if ((posreinas[i] - (i+1)) and (posreinas[i] + i + 1)) in diagonalocupadas:
            return False
        else:
            diagonalocupadas.append(posreinas[i]-(i+1))
            diagonalocupadas.append(posreinas[i]+i+1)
    return True

def validarReinas(posreinas):
    return (validarFila(posreinas)  and validarDiagonal(posreinas))

print (validarReinas([4, 2, 7, 3, 6, 8, 5, 1]))
print (validarReinas([2, 5, 7, 4, 1, 8, 6, 3]))
print (validarReinas([5, 3, 1, 4, 2, 8, 6, 3]))
print (validarReinas([5, 8, 2, 4, 7, 1, 3, 6]))
print (validarReinas([4, 3, 1, 8, 1, 3, 5, 2]))